# MIG Claims Triage Rules

**Version:** 2,1 | **Owner:** Ana Martinez, Regional Claims Manager, Barcelona
**Last Updated:** 2025-01-15 | **Applies to:** Iberian Peninsula Operations

---

## 1. Category Assignment

The claim category is determined by the combination of `product_line` and `incident_type`.

| Product Line | Incident Type | Category |
|---|---|---|
| Motor | collision (with injury) | auto-bodily-injury |
| Motor | hit_and_run (with injury) | auto-bodily-injury |
| Motor | collision (no injury) | auto-property |
| Motor | hit_and_run (no injury) | auto-property |
| Motor | theft | auto-property |
| Motor | vandalism | auto-property |
| Motor | glass_damage | auto-property |
| Home | water_damage | home-water-damage |
| Home | storm_damage | home-water-damage |
| Home | fire | home-fire |
| Home | electrical_damage | home-fire |
| Home | theft | home-theft |
| Home | vandalism | home-theft |
| Health | medical_emergency | health-emergency |
| Health | hospitalization | health-emergency |
| Health | surgery | health-emergency |
| Health | outpatient_treatment | health-routine |
| Health | dental | health-routine |
| Health | physiotherapy | health-routine |
| Commercial | slip_and_fall | commercial-liability |
| Commercial | product_liability | commercial-liability |
| Commercial | professional_negligence | commercial-liability |
| Commercial | property_damage | commercial-property |
| Commercial | fire | commercial-property |
| Commercial | flood | commercial-property |
| Commercial | equipment_breakdown | commercial-property |

---

## 2. Priority Levels

Rules are evaluated top-to-bottom. The **first matching rule** wins.

### Critical (Response: 4 hours)
A claim is Critical if **any** of these conditions are true:
- Estimated amount > EUR 50.000
- Injury reported AND estimated amount > EUR 10.000
- Commercial fire claim (any amount)
- Medical emergency with estimated amount > EUR 15.000
- Any hospitalization claim

### High (Response: 24 hours)
A claim is High if **any** of these conditions are true:
- Estimated amount > EUR 20.000
- Injury reported (any amount)
- Any fire claim (Home or Commercial)
- Theft claim with estimated amount > EUR 10.000
- Any slip_and_fall, product_liability, or professional_negligence claim
- Category is auto-bodily-injury

### Medium (Response: 48 hours)
A claim is Medium if **any** of these conditions are true:
- Estimated amount between EUR 5.000 and EUR 20.000
- Any water_damage or storm_damage claim
- Police report filed

### Low (Response: 72 hours)
A claim is Low if **any** of these conditions are true:
- Estimated amount < EUR 5.000
- Any glass_damage, dental, physiotherapy, or outpatient_treatment claim

---

## 3. Handling Paths

### Fast-Track (Target: 5 business days)
- Low priority AND estimated amount < EUR 2.000
- Any glass_damage claim
- Dental, physiotherapy, or outpatient_treatment claim under EUR 3.000
- Water damage under EUR 5.000 with no fraud indicators

### Standard (Target: 15 business days)
- Low or Medium priority claims not eligible for fast-track
- Auto-property claims under EUR 20.000
- Home-water-damage claims under EUR 15.000
- Any health-routine claim (regardless of amount)

### Complex-Review (Target: 30 business days)
- High or Critical priority claims
- Estimated amount > EUR 20.000
- Any fire claim
- Any commercial-liability claim
- Auto-bodily-injury with estimated amount > EUR 15.000

### Fraud-Investigation (Target: 45 business days)
- Any fraud indicator triggered (see Section 5)
- Two or more fraud indicators mandate SIU referral

### Legal-Referral (Target: 10 business days legal review)
- Commercial-liability with injury reported
- Professional negligence claims
- Estimated amount > EUR 100.000
- Auto-bodily-injury with disputed liability

---

## 4. Team Assignment

| Team | Code | Handles | Capacity/Day |
|---|---|---|---|
| Motor Claims Unit | BCN-MOT | auto-property, auto-bodily-injury | 25 |
| Property Claims Unit | BCN-PROP | home-water-damage, home-fire, home-theft | 20 |
| Health Claims Unit | BCN-HLT | health-emergency, health-routine | 30 |
| Commercial Lines Unit | BCN-COM | commercial-liability, commercial-property | 10 |
| Special Investigations Unit | BCN-SIU | All (fraud-investigation path only) | 5 |
| Legal & Compliance | BCN-LEG | All (legal-referral path only) | 8 |

---

## 5. Fraud Indicators

| ID | Indicator | Severity |
|---|---|---|
| FI-001 | Multiple recent claims (2+ in 90 days) | High |
| FI-002 | New policy claim (within 90 days of inception) | Medium |
| FI-003 | Inflated estimate (>80% of insured value) | High |
| FI-004 | Delayed reporting (>30 days between incident and claim) | Medium |
| FI-005 | No police report for theft/vandalism | High |
| FI-006 | Inconsistent description | High |
| FI-007 | Holiday/weekend clustering | Low |
| FI-008 | Round number estimate (exact thousands >= EUR 5.000) | Low |
| FI-009 | Prior fraud history | Critical |
| FI-010 | Third-party only witness | Medium |

**Rule:** A single indicator raises a flag. Two or more indicators mandate SIU referral.

---

## 6. SLA Targets

| Priority | First Contact | Initial Assessment | Target Resolution | Max Resolution | Escalation After |
|---|---|---|---|---|---|
| Critical | 4 hours | 1 day | 15 days | 30 days | 10 days |
| High | 24 hours | 3 days | 20 days | 45 days | 15 days |
| Medium | 48 hours | 5 days | 30 days | 60 days | 25 days |
| Low | 72 hours | 7 days | 15 days | 30 days | 12 days |

---

## 7. Key Insights from Historical Data

Based on analysis of 160 historical claims:

- **Approval rate:** 71% (Approved: 47%, Partially Approved: 24%)
- **Denial rate:** 15%
- **Fraud rate:** 7,5% (12 out of 160 claims)
- **Withdrawal rate:** 6%
- **Average resolution:** 20,3 days
- **Complex-review claims** average 37 days to resolve
- **Fast-track claims** average 6,5 days to resolve
- **Fraud investigations** average 51 days to resolve
