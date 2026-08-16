import pandas as pd

# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"
)

# ==========================================================
# HANDLE MISSING VALUES
# ==========================================================

numeric_cols = [

    "Financial_Health_Score",

    "Funding_Score",

    "Growth_Score",

    "Operational_Strength_Score",

    "Revenue",

    "Profit_or_Loss",

    "Gross_Margin",

    "Startup_Age"

]

df[numeric_cols] = df[numeric_cols].fillna(
    df[numeric_cols].median()
)

# ==========================================================
# NORMALIZE NUMERIC FEATURES
# ==========================================================

def normalize(series):

    return (

        (series - series.min())

        /

        (series.max() - series.min() + 1e-9)

    ) * 100


df["Revenue_Normalized"] = normalize(df["Revenue"])

df["Profit_Normalized"] = normalize(df["Profit_or_Loss"])

df["Margin_Normalized"] = normalize(df["Gross_Margin"])

# ==========================================================
# BURN RISK SCORE
# Higher Score = Higher Burn Risk
# ==========================================================

df["Burn_Risk_Score"] = (

      0.30 * (100 - df["Financial_Health_Score"])

    + 0.20 * (100 - df["Funding_Score"])

    + 0.15 * (100 - df["Profit_Normalized"])

    + 0.10 * (100 - df["Margin_Normalized"])

    + 0.10 * (100 - df["Revenue_Normalized"])

    + 0.10 * (100 - df["Growth_Score"])

    + 0.05 * (100 - df["Operational_Strength_Score"])

)

# ==========================================================
# THRESHOLDS
# ==========================================================

q25 = df["Burn_Risk_Score"].quantile(0.25)

q50 = df["Burn_Risk_Score"].quantile(0.50)

q75 = df["Burn_Risk_Score"].quantile(0.75)

print("=" * 60)

print("Burn Risk Thresholds")

print(f"25% : {q25:.2f}")

print(f"50% : {q50:.2f}")

print(f"75% : {q75:.2f}")

print("=" * 60)

# ==========================================================
# LABEL CREATION
# ==========================================================

def burn_risk(score):

    if score <= q25:

        return 0

    elif score <= q50:

        return 1

    elif score <= q75:

        return 2

    else:

        return 3


df["Burn_Risk_Label"] = df["Burn_Risk_Score"].apply(burn_risk)

# ==========================================================
# LABEL NAMES
# ==========================================================

label_map = {

    0: "Low Risk",

    1: "Moderate Risk",

    2: "High Risk",

    3: "Critical Risk"

}

df["Burn_Risk_Name"] = df["Burn_Risk_Label"].map(label_map)

# ==========================================================
# SAVE DATASET
# ==========================================================

df.to_csv(

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv",

    index=False

)

print("=" * 60)

print("Burn Risk Distribution")

print(

    df["Burn_Risk_Label"].value_counts().sort_index()

)

print()

print("Burn Risk Distribution (%)")

print(

    (df["Burn_Risk_Label"]

        .value_counts(normalize=True)

        .sort_index() * 100).round(2)

)

print("=" * 60)

print("Dataset Updated Successfully!")