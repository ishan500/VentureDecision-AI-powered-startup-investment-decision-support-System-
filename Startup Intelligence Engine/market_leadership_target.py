import pandas as pd

# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"

)

# ==========================================================
# MARKET LEADERSHIP PROBABILITY
# STARTUP INTELLIGENCE ENGINE
# ==========================================================

df["Market_Leadership_Probability"] = (

      0.30 * df["Market_Opportunity_Score"]

    + 0.25 * df["Competitive_Strength_Score"]

    + 0.20 * df["Growth_Score"]

    + 0.15 * df["Popularity_Score"]

    + 0.10 * df["Investor_Confidence_Score"]

)

# ==========================================================
# ROUND SCORE
# ==========================================================

df["Market_Leadership_Probability"] = (

    df["Market_Leadership_Probability"]

    .round(2)

)

# ==========================================================
# DISPLAY RESULTS
# ==========================================================

print("=" * 60)

print("Market Leadership Probability Created")

print()

print(

    df["Market_Leadership_Probability"].describe()

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