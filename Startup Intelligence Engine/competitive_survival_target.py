import pandas as pd

# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"

)

# ==========================================================
# COMPETITIVE SURVIVAL PROBABILITY
# STARTUP INTELLIGENCE ENGINE
# ==========================================================

df["Competitive_Survival_Probability"] = (

      0.30 * df["Competitive_Strength_Score"]

    + 0.25 * df["Financial_Health_Score"]

    + 0.20 * df["Operational_Strength_Score"]

    + 0.15 * df["Growth_Score"]

    + 0.10 * df["Market_Opportunity_Score"]

)

# ==========================================================
# ROUND SCORE
# ==========================================================

df["Competitive_Survival_Probability"] = (

    df["Competitive_Survival_Probability"]

    .round(2)

)

# ==========================================================
# DISPLAY RESULTS
# ==========================================================

print("=" * 60)

print("Competitive Survival Probability Created")

print()

print(

    df["Competitive_Survival_Probability"].describe()

)

print("=" * 60)

# ==========================================================
# SAVE DATASET
# ==========================================================

df.to_csv(

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv",

    index=False

)

print("Dataset Updated Successfully!")