import pandas as pd
import numpy as np

# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"
)

# ==========================================================
# THRESHOLDS
# ==========================================================

funding_threshold = df["Funding_Score"].median()

financial_threshold = df["Financial_Health_Score"].median()

growth_threshold = df["Growth_Score"].quantile(0.75)

market_threshold = df["Market_Opportunity_Score"].quantile(0.75)

# ==========================================================
# CONDITIONS
# ==========================================================

condition_1 = df["Funding_Score"] < funding_threshold

condition_2 = df["Financial_Health_Score"] < financial_threshold

condition_3 = df["Growth_Score"] >= growth_threshold

condition_4 = df["Market_Opportunity_Score"] >= market_threshold

# ==========================================================
# FUNDING REQUIREMENT LABEL
# Need funding if at least TWO conditions are true
# ==========================================================

conditions_met = (

    condition_1.astype(int)

    + condition_2.astype(int)

    + condition_3.astype(int)

    + condition_4.astype(int)

)

df["Funding_Requirement_Label"] = np.where(

    conditions_met >= 2,

    1,

    0

)

# ==========================================================
# SAVE DATASET
# ==========================================================

df.to_csv(

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv",

    index=False

)

# ==========================================================
# VERIFY
# ==========================================================

print("=" * 60)

print("Funding Requirement Label Distribution")

print(df["Funding_Requirement_Label"].value_counts())

print("=" * 60)

print("Dataset Updated Successfully")