# Mediterranean Insurance Group
## Quarterly Claims Report
### [QUARTER] [YEAR]

---

**Prepared by:** Actuarial Analytics Team, Marseille Office
**Distribution:** Executive Committee, Regional Directors, Head of Claims
**Classification:** Internal -- Confidential
**Report Date:** [DATE]

---

## 1. Executive Summary

_Provide a concise overview (3-5 sentences) of the quarter's claims performance. Highlight the most significant changes versus the prior quarter and the same quarter last year. Call out any items that require immediate management attention._

[EXECUTIVE_SUMMARY]

---

## 2. Key Performance Indicators

### KPI Definitions

| KPI | Formula | Target |
|-----|---------|--------|
| Total Claims Count | Count of all claims filed in the quarter | Monitoring |
| Total Reported Amount | SUM(reported_amount_eur) for the quarter | Monitoring |
| Total Paid Amount | SUM(paid_amount_eur) for the quarter | Monitoring |
| Total Reserves | SUM(reserved_amount_eur) for open/reserved claims | Monitoring |
| Average Claim Cost | Total Paid Amount / Count of claims with status = 'Paid' | Varies by product |
| Loss Ratio | Total Paid Amount / Total Reported Amount | See targets below |
| Settlement Rate | Count of 'Paid' claims / Total Claims Count | > 60% |
| Denial Rate | Count of 'Denied' claims / Total Claims Count | < 10% |
| Average Resolution Days | AVG(resolution_days) for settled claims (non-null) | < 45 days |
| Open Claims Ratio | Count of 'Open' + 'Reserved' claims / Total Claims Count | < 30% |
| Fraud Detection Rate | Count of 'Suspected' + 'Confirmed' fraud / Total Claims Count | Monitoring |

### Loss Ratio Targets by Product Line

| Product Line | Target Loss Ratio | Acceptable Range |
|-------------|-------------------|------------------|
| Motor | 65% | 60% -- 72% |
| Home | 55% | 48% -- 62% |
| Health | 70% | 63% -- 78% |
| Commercial | 50% | 42% -- 58% |
| Life | 40% | 33% -- 48% |

### KPI Dashboard

| KPI | Current Quarter | Prior Quarter | QoQ Change (%) | Same Quarter Last Year | YoY Change (%) |
|-----|----------------|---------------|----------------|----------------------|----------------|
| Total Claims | [VALUE] | [VALUE] | [CHANGE] | [VALUE] | [CHANGE] |
| Total Reported (EUR) | [VALUE] | [VALUE] | [CHANGE] | [VALUE] | [CHANGE] |
| Total Paid (EUR) | [VALUE] | [VALUE] | [CHANGE] | [VALUE] | [CHANGE] |
| Average Claim Cost (EUR) | [VALUE] | [VALUE] | [CHANGE] | [VALUE] | [CHANGE] |
| Loss Ratio | [VALUE] | [VALUE] | [CHANGE] | [VALUE] | [CHANGE] |
| Settlement Rate | [VALUE] | [VALUE] | [CHANGE] | [VALUE] | [CHANGE] |
| Denial Rate | [VALUE] | [VALUE] | [CHANGE] | [VALUE] | [CHANGE] |
| Avg Resolution Days | [VALUE] | [VALUE] | [CHANGE] | [VALUE] | [CHANGE] |

---

## 3. Trend Analysis

### Quarter-over-Quarter Trends

_Analyse the movement of key metrics from the prior quarter to the current quarter. Explain seasonal effects, market conditions, or operational changes that may have driven the trends._

[QOQ_TREND_ANALYSIS]

### Year-over-Year Trends

_Compare the current quarter to the same quarter in the prior year. Identify structural changes versus seasonal patterns._

[YOY_TREND_ANALYSIS]

### Four-Quarter Rolling View

_Provide a summary table showing the last four quarters side by side for the main KPIs._

| KPI | Q1 | Q2 | Q3 | Q4 |
|-----|----|----|----|----|
| Claims Count | [VALUE] | [VALUE] | [VALUE] | [VALUE] |
| Total Paid (EUR) | [VALUE] | [VALUE] | [VALUE] | [VALUE] |
| Loss Ratio | [VALUE] | [VALUE] | [VALUE] | [VALUE] |
| Avg Resolution Days | [VALUE] | [VALUE] | [VALUE] | [VALUE] |

---

## 4. Product Line Breakdown

_For each product line, show key metrics and provide brief commentary on performance._

| Product Line | Claims Count | Total Reported (EUR) | Total Paid (EUR) | Avg Claim Cost (EUR) | Loss Ratio | vs Target |
|-------------|-------------|---------------------|------------------|---------------------|------------|-----------|
| Motor | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [STATUS] |
| Home | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [STATUS] |
| Health | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [STATUS] |
| Commercial | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [STATUS] |
| Life | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [STATUS] |

### Sub-Product Detail

_Break down the top 3 product lines by sub-product for additional granularity._

[SUB_PRODUCT_TABLE]

---

## 5. Regional Breakdown

_Analyse claims performance by country and region._

| Country | Region | Claims Count | Total Paid (EUR) | Avg Claim Cost (EUR) | Loss Ratio | Avg Resolution Days |
|---------|--------|-------------|------------------|---------------------|------------|-------------------|
| Spain | [REGION] | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] |
| France | [REGION] | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] |
| Italy | [REGION] | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] |
| Portugal | [REGION] | [VALUE] | [VALUE] | [VALUE] | [VALUE] | [VALUE] |

### Regional Commentary

_Highlight any regions with outlier performance -- either notably good or concerning._

[REGIONAL_COMMENTARY]

---

## 6. Top 10 Largest Claims

_List the ten highest-value claims for the quarter by reported amount._

| Rank | Claim ID | Date | Product Line | Region | Country | Claim Type | Reported Amount (EUR) | Paid Amount (EUR) | Status | Fraud Flag |
|------|----------|------|-------------|--------|---------|------------|----------------------|-------------------|--------|-----------|
| 1 | [ID] | [DATE] | [PRODUCT] | [REGION] | [COUNTRY] | [TYPE] | [AMOUNT] | [AMOUNT] | [STATUS] | [FLAG] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

### Large Claims Commentary

_Discuss any claims above EUR 50,000 and their potential impact on reserves and reinsurance._

[LARGE_CLAIMS_COMMENTARY]

---

## 7. Fraud Detection Summary

### Overview

| Metric | Count | Amount (EUR) | % of Total Claims |
|--------|-------|-------------|-------------------|
| Confirmed Fraud | [VALUE] | [VALUE] | [VALUE] |
| Suspected Fraud | [VALUE] | [VALUE] | [VALUE] |
| Clean | [VALUE] | [VALUE] | [VALUE] |

### Fraud by Product Line

| Product Line | Confirmed | Suspected | Total Flagged | Flag Rate |
|-------------|-----------|-----------|---------------|-----------|
| Motor | [VALUE] | [VALUE] | [VALUE] | [VALUE] |
| Home | [VALUE] | [VALUE] | [VALUE] | [VALUE] |
| Health | [VALUE] | [VALUE] | [VALUE] | [VALUE] |
| Commercial | [VALUE] | [VALUE] | [VALUE] | [VALUE] |
| Life | [VALUE] | [VALUE] | [VALUE] | [VALUE] |

### Fraud Commentary

_Discuss fraud trends, common patterns, and effectiveness of detection measures._

[FRAUD_COMMENTARY]

---

## 8. Recommendations

_Provide 3-5 actionable recommendations based on the data analysis. Each recommendation should reference specific data points from the report._

### Priority Actions

1. **[RECOMMENDATION_TITLE]**
   - **Evidence:** [Data point from the report]
   - **Suggested action:** [Specific action]
   - **Expected impact:** [Quantified benefit]

2. **[RECOMMENDATION_TITLE]**
   - **Evidence:** [Data point from the report]
   - **Suggested action:** [Specific action]
   - **Expected impact:** [Quantified benefit]

3. **[RECOMMENDATION_TITLE]**
   - **Evidence:** [Data point from the report]
   - **Suggested action:** [Specific action]
   - **Expected impact:** [Quantified benefit]

---

## Appendix

### A. Data Quality Notes

_Document any data quality issues discovered during report generation (missing values, anomalies, etc.)._

[DATA_QUALITY_NOTES]

### B. Methodology

- **Loss Ratio Calculation:** Total Paid Amount / Total Reported Amount (gross basis).
- **Trend Calculations:** QoQ = (Current Quarter - Prior Quarter) / Prior Quarter * 100. YoY = (Current Quarter - Same Quarter Last Year) / Same Quarter Last Year * 100.
- **Averages:** Arithmetic mean unless otherwise stated. Excludes null/zero values where appropriate.
- **Fraud Rates:** Based on fraud_flag field. "Suspected" includes claims under active investigation. "Confirmed" includes claims where fraud has been formally determined.

### C. Glossary

| Term | Definition |
|------|-----------|
| Reported Amount | Initial estimated value of the claim at time of filing |
| Paid Amount | Actual disbursement made to the policyholder or third party |
| Reserved Amount | Funds set aside for claims not yet settled |
| Loss Ratio | Ratio of paid claims to reported claims (gross) |
| Resolution Days | Calendar days from claim filing to final settlement |
| QoQ | Quarter-over-Quarter comparison |
| YoY | Year-over-Year comparison |

---

_End of report template. All [PLACEHOLDER] values to be replaced with actual data during report generation._
