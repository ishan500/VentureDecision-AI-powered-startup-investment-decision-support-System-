import pandas as pd
import numpy as np

# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"
)

# ==========================================================
# RISK INDEX
# Higher value = Lower Risk
# ==========================================================

risk_index = (

    df["Financial_Health_Score"] * 0.30 +

    df["Funding_Score"] * 0.20 +

    df["Operational_Strength_Score"] * 0.20 +

    df["Investor_Confidence_Score"] * 0.15 +

    df["Sentiment_Score"] * 0.10 +

    df["Competitive_Strength_Score"] * 0.05

)

# ==========================================================
# RISK LABEL
#
# 1 = High Risk
# 0 = Low Risk
# ==========================================================

threshold = risk_index.quantile(0.30)

df["Risk_Label"] = np.where(

    risk_index < threshold,

    1,

    0

)

# ==========================================================
# SAVE
# ==========================================================

df.to_csv(

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv",

    index=False

)

print("="*60)

print("Risk Label Distribution")

print(df["Risk_Label"].value_counts())

print("\nDataset Updated Successfully")