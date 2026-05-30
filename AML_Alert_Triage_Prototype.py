import pandas as pd


# In[ ]:


import pandas as pd

data = [
    {
        "Customer": "ABC Imports",
        "RiskRating": "Low",
        "Country": "UK",
        "Counterparty": "Supplier A",
        "Amount": 950,
        "UsualAverage": 1200,
        "NewCounterparty": "No",
        "AdverseMedia": "No"
    },
    {
        "Customer": "Global Metals Ltd",
        "RiskRating": "Medium",
        "Country": "UAE",
        "Counterparty": "Al Noor Trading",
        "Amount": 45000,
        "UsualAverage": 9000,
        "NewCounterparty": "Yes",
        "AdverseMedia": "No"
    },
    {
        "Customer": "Delta Commodities",
        "RiskRating": "High",
        "Country": "Russia",
        "Counterparty": "Volga Trade",
        "Amount": 38000,
        "UsualAverage": 8000,
        "NewCounterparty": "Yes",
        "AdverseMedia": "Yes"
    }
]

df = pd.DataFrame(data)
df


# In[ ]:


high_risk_countries = [
    "Russia",
    "Iran",
    "North Korea",
    "Turkey",
    "UAE"
]

def calculate_risk(row):

    score = 0
    reasons = []

    if row["Country"] in high_risk_countries:
        score += 30
        reasons.append("High Risk Country")

    if row["Amount"] > row["UsualAverage"] * 3:
        score += 25
        reasons.append("Unusual Transaction Value")

    if row["NewCounterparty"] == "Yes":
        score += 20
        reasons.append("New Counterparty")

    if row["AdverseMedia"] == "Yes":
        score += 25
        reasons.append("Adverse Media")

    if row["RiskRating"] == "High":
        score += 15
        reasons.append("High Customer Risk")

    return score, reasons


# In[ ]:


df[["RiskScore","RiskReasons"]] = df.apply(
    lambda row: pd.Series(calculate_risk(row)),
    axis=1
)

df


# In[ ]:


def investigator_summary(row):

    return f"""
Customer: {row['Customer']}

Risk Score: {row['RiskScore']}

Risk Indicators:
{', '.join(row['RiskReasons'])}

Investigator Recommendation:
Review transaction activity and perform Enhanced Due Diligence due to identified risk indicators.
"""


# In[ ]:


df["InvestigatorSummary"] = df.apply(
    investigator_summary,
    axis=1
)

df[["Customer","RiskScore","InvestigatorSummary"]]


# In[ ]:


for summary in df["InvestigatorSummary"]:
    print(summary)
    print("-" * 60)


# In[ ]:


df[["Customer", "RiskScore", "RiskReasons"]]


# In[ ]:


def risk_level(score):
    if score >= 90:
        return "High"
    elif score >= 50:
        return "Medium"
    else:
        return "Low"

df["RiskLevel"] = df["RiskScore"].apply(risk_level)

df[["Customer", "RiskScore", "RiskLevel", "RiskReasons"]]


# In[ ]:


df.sort_values("RiskScore", ascending=False)


# In[ ]:


import matplotlib.pyplot as plt

# Sort highest-risk customers first
risk_dashboard = df.sort_values("RiskScore", ascending=False)

# Create bar chart
risk_dashboard.plot(
    x="Customer",
    y="RiskScore",
    kind="bar",
    legend=False,
    figsize=(8, 5)
)

plt.title("AML Alert Risk Score Dashboard")
plt.xlabel("Customer")
plt.ylabel("Risk Score")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# In[ ]:


def risk_status(score):

    if score >= 100:
        return "🔴 Critical"

    elif score >= 50:
        return "🟠 Medium"

    else:
        return "🟢 Low"

df["AlertStatus"] = df["RiskScore"].apply(risk_status)

df[["Customer","RiskScore","AlertStatus"]]


# In[ ]:


risk_dashboard[["Customer", "RiskScore", "RiskLevel", "RiskReasons"]]


# In[ ]:


risk_dashboard = df.sort_values(
    "RiskScore",
    ascending=False
)


# In[ ]:


for index, row in risk_dashboard.iterrows():

    print("=" * 60)

    print(row["Customer"])

    print("Risk Score:", row["RiskScore"])

    print("Status:", row["AlertStatus"])

    print("Indicators:")

    for reason in row["RiskReasons"]:
        print("-", reason)

    print()


# In[ ]:


df.to_csv("sample_transactions.csv", index=False)


# In[ ]:


with open("output_sample.txt", "w") as file:
    for index, row in risk_dashboard.iterrows():
        file.write("=" * 60 + "\n")
        file.write(f"Customer: {row['Customer']}\n")
        file.write(f"Risk Score: {row['RiskScore']}\n")
        file.write(f"Status: {row['AlertStatus']}\n")
        file.write("Indicators:\n")

        for reason in row["RiskReasons"]:
            file.write(f"- {reason}\n")

        file.write("\n")


# In[ ]:


readme_text = """# AML Alert Triage Prototype

This is a Python proof-of-concept demonstrating how transaction monitoring alerts can be risk-scored, prioritised and summarised for investigator review.

## Purpose

The prototype explores how Python and AI-assisted analytics can support Financial Crime Operations by:

- scoring alerts against AML risk indicators
- prioritising higher-risk cases
- generating investigator-style summaries
- visualising alert risk scores

## Risk Indicators Used

- High-risk jurisdiction
- Unusual transaction value
- New counterparty
- Adverse media
- Customer risk rating

## Outputs

The prototype produces:

- AML risk score
- Alert status
- Risk reasons
- Prioritised alert queue
- Investigator summary
- Risk dashboard chart

## Tools Used

- Python
- Pandas
- Matplotlib
- Jupyter Notebook

## Context

This project was created as part of my development in Python, Financial Crime analytics and AI-enabled Transaction Monitoring use cases.

It is not intended to replace enterprise TM platforms. It demonstrates how AML domain logic can be translated into a working analytics prototype.
"""

with open("README.md", "w") as file:
    file.write(readme_text)


# In[ ]:


import os
print(os.getcwd())


# In[ ]:




