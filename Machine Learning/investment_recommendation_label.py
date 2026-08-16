import pandas as pd

# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"
)

# ==========================================================
# INVESTMENT SCORE
# ==========================================================

df["Investment_Score"] = (

    0.25 * df["Overall_Startup_Score"]

    + 0.20 * df["Financial_Health_Score"]

    + 0.20 * df["Growth_Score"]

    + 0.15 * df["Investor_Confidence_Score"]

    + 0.10 * df["Operational_Strength_Score"]

    + 0.10 * df["Market_Opportunity_Score"]

)

# ==========================================================
# THRESHOLDS
# ==========================================================

q25 = df["Investment_Score"].quantile(0.25)
q50 = df["Investment_Score"].quantile(0.50)
q75 = df["Investment_Score"].quantile(0.75)

print("=" * 60)

print("Investment Recommendation Thresholds")

print(f"25% : {q25:.2f}")
print(f"50% : {q50:.2f}")
print(f"75% : {q75:.2f}")

print("=" * 60)

# ==========================================================
# LABEL CREATION
# ==========================================================

def recommendation(score):

    if score <= q25:
        return 0          # Reject

    elif score <= q50:
        return 1          # Watchlist

    elif score <= q75:
        return 2          # Invest

    else:
        return 3          # Strong Invest

df["Investment_Recommendation_Label"] = df["Investment_Score"].apply(recommendation)

# ==========================================================
# LABEL NAMES
# ==========================================================

label_map = {

    0: "Reject",

    1: "Watchlist",

    2: "Invest",

    3: "Strong Invest"

}

df["Investment_Recommendation_Name"] = df[
    "Investment_Recommendation_Label"
].map(label_map)

# ==========================================================
# SAVE
# ==========================================================

df.to_csv(
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv",
    index=False
)

print("=" * 60)

print("Investment Recommendation Distribution")

print(
    df["Investment_Recommendation_Label"].value_counts().sort_index()
)

print()

print("Investment Recommendation Distribution (%)")

print(
    (df["Investment_Recommendation_Label"]
     .value_counts(normalize=True)
     .sort_index() * 100).round(2)
)

print("=" * 60)

print("Dataset Updated Successfully!")