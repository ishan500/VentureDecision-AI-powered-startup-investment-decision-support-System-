# ==========================================================
# DUE DILIGENCE SERVICE
# VentureIQ
# ==========================================================

from typing import Optional

from api.services.data_service import (
    get_startup_by_name
)

from api.services.ollama_service import (
    generate_natural_language_qa
)


# ==========================================================
# BUILD DUE DILIGENCE PROMPT
# ==========================================================

def build_due_diligence_prompt(

    startup_data: dict

):

    startup_name = startup_data.get(

        "Startup_Name",

        "Unknown Startup"

    )


    return f"""

You are an AI investment research assistant.

Generate a professional startup due diligence report
using ONLY the data provided below.

IMPORTANT RULES:

1. Do NOT invent any numbers.
2. Do NOT change any numerical value.
3. Do NOT convert currencies.
4. Do NOT change units such as million, billion, lakh,
   crore, percentage, or any other unit.
5. If a value is missing, write:
   "Not available in the provided dataset."
6. Do NOT assume information that is not present.
7. Do NOT create unsupported historical facts.
8. Clearly distinguish between:
   - Historical / factual data
   - ML predictions
   - Scores
   - Probabilities
   - Rule-based outputs
9. Use the exact values provided in the dataset.
10. Do not make investment claims that are not supported
    by the provided data.
11. Do not say that a startup will definitely succeed,
    fail, be acquired, or receive funding.
12. The report must be based only on the supplied data.

STARTUP DATA:

{startup_data}


GENERATE THE REPORT USING THE FOLLOWING STRUCTURE:

### Executive Summary

Provide a concise overview based only on the provided data.

### Company Overview

Include only available information such as:

- Startup name
- Sector
- Industry
- Founded year
- Location
- Business model
- Founders
- Current status

### Financial Analysis

Discuss only the available financial metrics.

Include:

- Revenue
- Revenue growth
- Profit or loss
- Gross margin
- Financial health score
- Other available financial metrics

### Funding Analysis

Discuss only the available funding information.

Include:

- Total funding raised
- Latest funding amount
- Number of funding rounds
- Funding stage
- Investors
- Last funding investor
- Funding readiness score

### Growth Analysis

Discuss the available growth metrics.

Include:

- Revenue growth
- Employee growth
- Employee count
- Customer growth
- Website traffic
- Monthly visits
- Monthly active users
- App downloads

Only include metrics that exist in the provided data.

### Market Opportunity

Discuss only the available market-related data.

Include:

- TAM
- Market size
- Market growth
- Market share
- Market opportunity score

### Competitive Position

Discuss:

- Competitive strength score
- Market leadership probability
- Competitive survival probability
- Other available competitive metrics

### Operational Analysis

Discuss:

- Operational strength score
- Employee metrics
- Customer metrics
- Efficiency metrics
- Other operational metrics

### Risk Analysis

Discuss:

- Risk score
- Failure probability
- Burn risk probability
- Red flags
- Other risk-related outputs

### Investment Readiness

Discuss:

- Funding readiness score
- Funding readiness label
- Funding requirement prediction
- Investor confidence score

### Exit Potential

Discuss:

- Acquisition probability
- Exit probability
- IPO probability
- Valuation growth prediction
- Other available exit-related metrics

### Key Red Flags

List only red flags supported by the provided data.

If no red flags are available, write:

"No specific red flags were identified in the provided dataset."

### Final Investment Recommendation

Provide a recommendation based only on the available
investment score, prediction outputs, risk metrics,
and other provided ML results.

Use the existing recommendation label if available.

Do not invent a new recommendation label.

### Overall Conclusion

Summarize the startup's overall position using only
the information provided in the dataset.

Do not introduce any new facts or numbers.

"""


# ==========================================================
# GENERATE DUE DILIGENCE REPORT
# ==========================================================

def generate_due_diligence_report(

    startup_name: str,

    dataset_type: str

):

    startup_data = get_startup_by_name(

        startup_name,

        dataset_type

    )


    if startup_data is None:

        return {

            "status": "error",

            "message": (

                f"Startup '{startup_name}' "

                f"not found in {dataset_type} dataset."

            )

        }


    prompt = build_due_diligence_prompt(

        startup_data

    )


    report = generate_natural_language_qa(

        prompt

    )


    return {

        "status": "success",

        "startup_name": startup_name,

        "dataset_type": dataset_type,

        "report": report

    }