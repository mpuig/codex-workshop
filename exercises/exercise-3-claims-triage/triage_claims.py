"""
MIG Claims Triage Script
Applies business rules from business_rules.json to incoming_claims.csv
Produces triaged_claims.csv with category, priority, handling path, team, and justification
"""

import csv
import json
from datetime import datetime
from collections import Counter

# Load data
with open('data/incoming_claims.csv', 'r') as f:
    reader = csv.DictReader(f)
    claims = list(reader)

with open('data/business_rules.json', 'r') as f:
    rules = json.load(f)

# Build category lookup from rules
CATEGORY_MAP = {}
for rule in rules['category_mapping']['rules']:
    key_parts = [rule['product_line'], rule['incident_type']]
    injury = rule.get('injury_reported', None)
    if injury is not None:
        key = (rule['product_line'], rule['incident_type'], injury)
    else:
        key = (rule['product_line'], rule['incident_type'])
    CATEGORY_MAP[key] = rule['category']

# Team assignment lookup
TEAM_MAP = {}
for team in rules['team_assignment']['teams']:
    for cat in team['handles']:
        if cat != 'all categories':
            TEAM_MAP[cat] = {
                'team_name': team['team_name'],
                'team_code': team['team_code']
            }

# SLA lookup
SLA_MAP = {}
for sla in rules['sla_targets']['targets']:
    SLA_MAP[sla['priority']] = sla


def assign_category(claim):
    """Assign category based on product_line, incident_type, and injury_reported."""
    pl = claim['product_line']
    it = claim['incident_type']
    injury = claim['injury_reported']

    # Try specific key with injury first
    key_specific = (pl, it, injury)
    if key_specific in CATEGORY_MAP:
        return CATEGORY_MAP[key_specific]

    # Fall back to general key
    key_general = (pl, it)
    if key_general in CATEGORY_MAP:
        return CATEGORY_MAP[key_general]

    return 'uncategorized'


def assign_priority(claim, category):
    """Assign priority level based on business rules (first match wins)."""
    amount = float(claim['estimated_amount_eur'])
    injury = claim['injury_reported'] == 'Yes'
    incident = claim['incident_type']
    product = claim['product_line']

    reasons = []

    # Critical checks
    if amount > 50000:
        return 'Critical', f'Estimated amount EUR {amount:,.2f} exceeds 50.000 threshold'
    if injury and amount > 10000:
        return 'Critical', f'Injury reported with estimated amount EUR {amount:,.2f} (>10.000)'
    if incident == 'fire' and product == 'Commercial':
        return 'Critical', f'Commercial fire claim requires immediate attention'
    if incident == 'medical_emergency' and amount > 15000:
        return 'Critical', f'Medical emergency with amount EUR {amount:,.2f} (>15.000)'
    if incident == 'hospitalization':
        return 'Critical', f'Hospitalization claim requires immediate attention'

    # High checks
    if amount > 20000:
        return 'High', f'Estimated amount EUR {amount:,.2f} exceeds 20.000 threshold'
    if injury:
        return 'High', f'Injury reported (amount EUR {amount:,.2f})'
    if incident == 'fire':
        return 'High', f'Fire claim requires expedited handling'
    if incident == 'theft' and amount > 10000:
        return 'High', f'Theft claim with amount EUR {amount:,.2f} exceeds 10.000 threshold'
    if incident in ('slip_and_fall', 'product_liability', 'professional_negligence'):
        return 'High', f'Liability claim ({incident}) requires High priority'
    if category == 'auto-bodily-injury':
        return 'High', f'Auto bodily injury claim'

    # Medium checks
    if 5000 <= amount <= 20000:
        return 'Medium', f'Estimated amount EUR {amount:,.2f} in 5.000-20.000 range'
    if incident in ('water_damage', 'storm_damage'):
        return 'Medium', f'{incident.replace("_", " ").title()} claim assigned Medium priority'
    if claim['police_report_filed'] == 'Yes':
        return 'Medium', f'Police report filed; assigned Medium priority'

    # Low (default for small/routine claims)
    if amount < 5000:
        return 'Low', f'Estimated amount EUR {amount:,.2f} below 5.000 threshold'
    if incident in ('glass_damage', 'dental', 'physiotherapy', 'outpatient_treatment'):
        return 'Low', f'Routine {incident.replace("_", " ")} claim'

    return 'Medium', f'Default assignment based on claim characteristics'


def check_fraud_indicators(claim, all_claims):
    """Check for fraud indicators and return list of triggered indicators."""
    indicators = []
    amount = float(claim['estimated_amount_eur'])
    incident = claim['incident_type']

    # FI-001: Multiple recent claims (2+ from same policyholder)
    name = claim['policyholder_name']
    claim_date = datetime.strptime(claim['claim_date'], '%Y-%m-%d')
    same_claimant = [
        c for c in all_claims
        if c['policyholder_name'] == name and c['claim_id'] != claim['claim_id']
    ]
    recent_claims = [
        c for c in same_claimant
        if abs((claim_date - datetime.strptime(c['claim_date'], '%Y-%m-%d')).days) <= 90
    ]
    if len(recent_claims) >= 1:  # 2+ total including current
        indicators.append(('FI-001', 'High', f'Multiple claims: {len(recent_claims)+1} claims within 90 days'))

    # FI-004: Delayed reporting (>30 days)
    incident_date = datetime.strptime(claim['incident_date'], '%Y-%m-%d')
    delay = (claim_date - incident_date).days
    if delay > 30:
        indicators.append(('FI-004', 'Medium', f'Delayed reporting: {delay} days between incident and claim'))

    # FI-005: No police report for theft/vandalism
    if incident in ('theft', 'vandalism') and claim['police_report_filed'] == 'No':
        indicators.append(('FI-005', 'High', f'No police report filed for {incident} claim'))

    # FI-008: Round number estimate
    if amount >= 5000 and amount == int(amount) and amount % 1000 == 0:
        indicators.append(('FI-008', 'Low', f'Suspiciously round estimate: EUR {amount:,.0f}'))

    return indicators


def assign_handling_path(claim, category, priority, fraud_indicators):
    """Determine the handling path based on category, priority, fraud, and claim details."""
    amount = float(claim['estimated_amount_eur'])
    incident = claim['incident_type']
    injury = claim['injury_reported'] == 'Yes'

    # Fraud investigation takes precedence if 2+ indicators
    if len(fraud_indicators) >= 2:
        return 'fraud-investigation', f'SIU referral: {len(fraud_indicators)} fraud indicators triggered'

    # Legal referral checks
    if category == 'commercial-liability' and injury:
        return 'legal-referral', 'Commercial liability with injury requires legal review'
    if incident == 'professional_negligence':
        return 'legal-referral', 'Professional negligence claim requires legal review'
    if amount > 100000:
        return 'legal-referral', f'Amount EUR {amount:,.2f} exceeds 100.000; legal review required'

    # Fast-track checks
    if priority == 'Low' and amount < 2000:
        return 'fast-track', f'Low priority, amount EUR {amount:,.2f} under 2.000 threshold'
    if incident == 'glass_damage':
        return 'fast-track', 'Glass damage claim eligible for fast-track'
    if incident in ('dental', 'physiotherapy', 'outpatient_treatment') and amount < 3000:
        return 'fast-track', f'Routine {incident.replace("_", " ")} under EUR 3.000'
    if incident in ('water_damage',) and amount < 5000 and len(fraud_indicators) == 0:
        return 'fast-track', f'Water damage under EUR 5.000 with no fraud indicators'

    # Complex-review checks
    if priority in ('High', 'Critical'):
        return 'complex-review', f'{priority} priority claim requires senior review'
    if amount > 20000:
        return 'complex-review', f'Amount EUR {amount:,.2f} exceeds 20.000; complex review needed'
    if incident == 'fire':
        return 'complex-review', 'Fire claim requires complex review'
    if category == 'commercial-liability':
        return 'complex-review', 'Commercial liability claim requires complex review'
    if category == 'auto-bodily-injury' and amount > 15000:
        return 'complex-review', 'Auto bodily injury over EUR 15.000 requires complex review'

    # Standard (default)
    return 'standard', 'Standard processing path'


def assign_team(category, handling_path):
    """Assign claim to appropriate team based on category and handling path."""
    if handling_path == 'fraud-investigation':
        return 'Special Investigations Unit', 'BCN-SIU'
    if handling_path == 'legal-referral':
        return 'Legal & Compliance', 'BCN-LEG'
    if category in TEAM_MAP:
        return TEAM_MAP[category]['team_name'], TEAM_MAP[category]['team_code']
    return 'Unassigned', 'N/A'


def estimate_resolution_days(handling_path, priority):
    """Estimate resolution days based on handling path and historical data."""
    path_estimates = {
        'fast-track': 5,
        'standard': 15,
        'complex-review': 30,
        'fraud-investigation': 45,
        'legal-referral': 30
    }
    base = path_estimates.get(handling_path, 15)

    # Adjust by priority
    if priority == 'Critical':
        base = min(base, 15)  # Critical claims get expedited
    elif priority == 'Low':
        base = max(base, 7)  # Low priority still takes minimum time

    return base


# Process all claims
results = []
for claim in claims:
    category = assign_category(claim)
    priority, priority_reason = assign_priority(claim, category)
    fraud_indicators = check_fraud_indicators(claim, claims)
    handling_path, path_reason = assign_handling_path(claim, category, priority, fraud_indicators)
    team_name, team_code = assign_team(category, handling_path)
    est_days = estimate_resolution_days(handling_path, priority)

    # Build justification
    justification_parts = [priority_reason]
    if fraud_indicators:
        fi_names = [f'{fi[0]}: {fi[2]}' for fi in fraud_indicators]
        justification_parts.append('Fraud flags: ' + '; '.join(fi_names))
    justification_parts.append(f'Path: {path_reason}')
    justification = ' | '.join(justification_parts)

    result = dict(claim)
    result['assigned_category'] = category
    result['priority_level'] = priority
    result['handling_path'] = handling_path
    result['assigned_team'] = f'{team_name} ({team_code})'
    result['estimated_resolution_days'] = est_days
    result['justification'] = justification
    results.append(result)

# Write output
fieldnames = list(claims[0].keys()) + [
    'assigned_category', 'priority_level', 'handling_path',
    'assigned_team', 'estimated_resolution_days', 'justification'
]

with open('triaged_claims.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

# Print summary statistics
print('=' * 60)
print('MIG CLAIMS TRIAGE - SUMMARY REPORT')
print('=' * 60)
print(f'Total claims processed: {len(results)}')
print()

# Priority distribution
print('PRIORITY DISTRIBUTION:')
priority_counts = Counter(r['priority_level'] for r in results)
for p in ['Critical', 'High', 'Medium', 'Low']:
    count = priority_counts.get(p, 0)
    pct = count / len(results) * 100
    print(f'  {p:10s}: {count:4d} ({pct:5.1f}%)')

print()
print('CATEGORY DISTRIBUTION:')
cat_counts = Counter(r['assigned_category'] for r in results)
for cat, count in cat_counts.most_common():
    pct = count / len(results) * 100
    print(f'  {cat:25s}: {count:4d} ({pct:5.1f}%)')

print()
print('HANDLING PATH DISTRIBUTION:')
path_counts = Counter(r['handling_path'] for r in results)
for path, count in path_counts.most_common():
    pct = count / len(results) * 100
    print(f'  {path:25s}: {count:4d} ({pct:5.1f}%)')

print()
print('TEAM WORKLOAD:')
team_counts = Counter(r['assigned_team'] for r in results)
for team, count in team_counts.most_common():
    print(f'  {team:45s}: {count:4d}')

print()
print('FRAUD INVESTIGATION REFERRALS:')
fraud_claims = [r for r in results if r['handling_path'] == 'fraud-investigation']
print(f'  Total fraud referrals: {len(fraud_claims)}')
for fc in fraud_claims:
    print(f'  - {fc["claim_id"]} ({fc["policyholder_name"]}): {fc["justification"][:100]}...')

print()
print('CRITICAL CLAIMS REQUIRING IMMEDIATE ATTENTION:')
critical_claims = [r for r in results if r['priority_level'] == 'Critical']
for cc in critical_claims:
    amount = float(cc['estimated_amount_eur'])
    print(f'  - {cc["claim_id"]} | {cc["assigned_category"]:25s} | EUR {amount:>12,.2f} | {cc["handling_path"]}')

print()
print(f'Output saved to: triaged_claims.csv')
