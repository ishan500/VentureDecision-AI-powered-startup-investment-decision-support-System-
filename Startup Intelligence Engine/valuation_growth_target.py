import pandas as pd

# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"
)

# ==========================================================
# VALUATION GROWTH PREDICTION
# VC INTELLIGENCE SCORING ENGINE
# ==========================================================

df["Valuation_Growth_Prediction"] = (

      0.30 * df["Growth_Score"]

    + 0.20 * df["Financial_Health_Score"]

    + 0.20 * df["Market_Opportunity_Score"]

    + 0.15 * df["Competitive_Strength_Score"]

    + 0.10 * df["Investor_Confidence_Score"]

    + 0.05 * df["Operational_Strength_Score"]

)

# ==========================================================
# ROUND SCORE
# ==========================================================

df["Valuation_Growth_Prediction"] = (
    df["Valuation_Growth_Prediction"]
    .round(2)
)

# ==========================================================
# DISPLAY RESULTS
# ==========================================================

print("=" * 60)

print("Valuation Growth Prediction Created")

print()

print(df["Valuation_Growth_Prediction"].describe())

print("=" * 60)

# ==========================================================
# SAVE DATASET
# ==========================================================

df.to_csv(

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv",

    index=False

)

print("Dataset Updated Successfully!")