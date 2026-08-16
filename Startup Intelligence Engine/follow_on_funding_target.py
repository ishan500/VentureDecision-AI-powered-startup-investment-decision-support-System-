import pandas as pd

# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"
)

# ==========================================================
# FOLLOW-ON FUNDING PROBABILITY
# STARTUP INTELLIGENCE ENGINE
# ==========================================================

df["Follow_On_Funding_Probability"] = (

      0.30 * df["Funding_Score"]

    + 0.25 * df["Investor_Confidence_Score"]

    + 0.20 * df["Financial_Health_Score"]

    + 0.15 * df["Growth_Score"]

    + 0.10 * df["Operational_Strength_Score"]

)


# ==========================================================
# ROUND SCORE
# ==========================================================

df["Follow_On_Funding_Probability"] = (
    df["Follow_On_Funding_Probability"].round(2)
)

# ==========================================================
# DISPLAY RESULTS
# ==========================================================

print("=" * 60)

print("Follow-On Funding Probability Created")

print()

print(df["Follow_On_Funding_Probability"].describe())

print("=" * 60)

# ==========================================================
# SAVE DATASET
# ==========================================================

df.to_csv(

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv",

    index=False

)

print("Dataset Updated Successfully!")