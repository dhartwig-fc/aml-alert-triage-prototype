# aml-alert-triage-prototype
AML triage prototype
# AML Alert Triage Prototype

This is a small Python prototype demonstrating how transaction monitoring alerts can be risk-scored and summarised for investigator review.

## Purpose

The objective is to show how basic Python logic can support Financial Crime Operations by:

- identifying high-risk jurisdictions
- detecting transaction spikes
- flagging new counterparties
- incorporating adverse media indicators
- generating investigator-style summaries

## Context

This project is part of my development in Python, AI-enabled financial crime transformation and transaction monitoring analytics.

It is not intended to replace enterprise transaction monitoring platforms. It demonstrates how simple analytics and rule-based scoring can support alert prioritisation and investigator workflow design.

## Files

- `sample_transactions.csv` — sample transaction dataset
- `aml_alert_triage.py` — Python risk scoring prototype
- `output_sample.txt` — example output from the prototype

## Example Output

Customer: Global Metals Ltd  
Risk Score: 75  
Recommendation: Escalate for enhanced investigation  

Investigator Summary:  
Customer Global Metals Ltd generated an AML alert with a risk score of 75. Key risk indicators include high-risk jurisdiction exposure, transaction value significantly above customer baseline and new counterparty relationship.

## Future Enhancements

- Add pandas for data analysis
- Add charts for alert prioritisation
- Add AI-generated investigation summaries
- Add Quantexa-style network relationship indicators
- Add SAR drafting support
