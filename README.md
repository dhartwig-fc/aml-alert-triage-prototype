[← Back to Portfolio](https://dhartwig-fc.github.io)

[LinkedIn](https://www.linkedin.com/in/dan-hartwig-financial-crime) | [GitHub Profile](https://github.com/dhartwig-fc)

# aml-alert-triage-prototype

# AML Alert Triage Prototype
This is a small Python prototype demonstrating how transaction monitoring alerts can be risk-scored and summarised for investigator review.

## Context
This project is part of my development in Python, AI-enabled financial crime transformation and transaction monitoring analytics.

It is not intended to replace enterprise transaction monitoring platforms. It demonstrates how simple analytics and rule-based scoring can support alert prioritisation and investigator workflow design.

## Purpose
The objective is to show how basic Python logic can support Financial Crime Operations by:

- scoring alerts against AML risk indicators
- identifying high-risk jurisdictions
- detecting transaction spikes
- flagging new counterparties
- incorporating adverse media indicators
- generating investigator-style summaries
- prioritising higher-risk cases
- visualising alert risk scores

## Files
- AML_Alert_Triage_Prototype.ipynb - Jupyter notebook containing the prototype logic
- sample_transactions.csv - sample AML alert dataset
- Dashboard.png - example risk dashboard output
- README.md - project documentation

## Outputs
The prototype produces:

- AML risk score
- Alert status
- Risk reasons
- Prioritised alert queue
- Investigator summary
- Risk dashboard chart

## Example Output
Customer: Global Metals Ltd

Risk Score: 75
Alert Status: Medium

Risk Indicators:
- High Risk Country
- Unusual Transaction Value
- New Counterparty

Recommendation:
Escalate for enhanced investigation.

Investigator Summary:
Customer Global Metals Ltd generated an AML alert with a risk score of 75. Key risk indicators include high-risk jurisdiction exposure, transaction value significantly above customer baseline and a newly established counterparty relationship.

## Tools Used
- Python
- Pandas
- Matplotlib
- Jupyter Notebook

## Future Enhancements

### AI Investigator Copilot
Integrate a Large Language Model (LLM) to generate enhanced investigator narratives, case summaries and recommended next actions.

### Entity Resolution & Network Analytics
Incorporate Quantexa-style network analysis to identify hidden relationships between customers, counterparties and transactions.

### Dynamic Segmentation Risk Weighting
Replace static risk scores with configurable risk-weight models driven by customer, geography and behavioural attributes.

### Alert Prioritisation Engine
Introduce queue management logic to rank alerts based on risk severity, investigator capacity and SLA requirements.

### Adverse Media Intelligence
Integrate external adverse media and sanctions screening feeds to automatically enrich alerts.

### SAR Narrative Drafting
Generate Suspicious Activity Report (SAR) draft narratives to accelerate investigator workflow.

### Machine Learning Risk Models
Move from rule-based scoring to supervised learning models trained on historical investigation outcomes.

### Case Management Integration
Connect the prototype to transaction monitoring and case management platforms for end-to-end workflow automation.

### Executive Dashboard
Create a web-based dashboard showing:

- Alert volumes
- High-risk customers
- Alert ageing
- Investigator productivity
- Risk trends

- ## Disclaimer
This project is a learning prototype intended for demonstration purposes only.

It does not represent a production-grade AML monitoring solution and should not be used for regulatory decision-making. The scoring methodology is intentionally simplified to demonstrate Python-based risk assessment concepts.
