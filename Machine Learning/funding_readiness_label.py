import pandas as pd

# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"
)

# ==========================================================
# FUNDING READINESS SCORE
# ==========================================================

df["Funding_Readiness_Score"] = (

    0.25 * df["Financial_Health_Score"]

    + 0.20 * df["Operational_Strength_Score"]

    + 0.20 * df["Investor_Confidence_Score"]

    + 0.15 * df["Growth_Score"]

    + 0.10 * df["Market_Opportunity_Score"]

    + 0.10 * df["Overall_Startup_Score"]

)

# ==========================================================
# THRESHOLDS
# ==========================================================

q25 = df["Funding_Readiness_Score"].quantile(0.25)
q50 = df["Funding_Readiness_Score"].quantile(0.50)
q75 = df["Funding_Readiness_Score"].quantile(0.75)

print("=" * 60)

print("Funding Readiness Thresholds")

print(f"25% : {q25:.2f}")
print(f"50% : {q50:.2f}")
print(f"75% : {q75:.2f}")

print("=" * 60)

# ==========================================================
# LABEL CREATION
# ==========================================================

def readiness(score):

    if score <= q25:
        return 0      # Not Ready

    elif score <= q50:
        return 1      # Early Preparation

    elif score <= q75:
        return 2      # Ready

    else:
        return 3      # Highly Ready

df["Funding_Readiness_Label"] = df["Funding_Readiness_Score"].apply(readiness)

# ==========================================================
# LABEL NAMES
# ==========================================================

label_map = {

    0: "Not Ready",

    1: "Early Preparation",

    2: "Ready",

    3: "Highly Ready"

}

df["Funding_Readiness_Name"] = df["Funding_Readiness_Label"].map(label_map)

# ==========================================================
# SAVE
# ==========================================================

df.to_csv(
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv",
    index=False
)

print("=" * 60)

print("Funding Readiness Distribution")

print(df["Funding_Readiness_Label"].value_counts().sort_index())

print()

print("Funding Readiness Distribution (%)")

print(

    (df["Funding_Readiness_Label"]
        .value_counts(normalize=True)
        .sort_index() * 100).round(2)

)

print("=" * 60)

print("Dataset Updated Successfully!")