import pandas as pd

# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"
)

# ==========================================================
# STAGE SCORE (0–100)
# ==========================================================

df["Stage_Score"] = (

    0.30 * df["Funding_Score"]

    + 0.25 * df["Operational_Strength_Score"]

    + 0.20 * df["Investor_Confidence_Score"]

    + 0.15 * df["Financial_Health_Score"]

    + 0.10 * df["Startup_Maturity_Score"]

)

# ==========================================================
# NORMALIZE TO 0–100
# ==========================================================

minimum = df["Stage_Score"].min()

maximum = df["Stage_Score"].max()

df["Stage_Score"] = (

    (df["Stage_Score"] - minimum)

    /

    (maximum - minimum)

) * 100

# ==========================================================
# CREATE FUNDING STAGE LABEL
# ==========================================================

df["Funding_Stage_Label"] = 0

df.loc[
    df["Stage_Score"] >= 25,
    "Funding_Stage_Label"
] = 1

df.loc[
    df["Stage_Score"] >= 50,
    "Funding_Stage_Label"
] = 2

df.loc[
    df["Stage_Score"] >= 75,
    "Funding_Stage_Label"
] = 3

# ==========================================================
# OPTIONAL STAGE NAME
# ==========================================================

stage_names = {

    0: "Seed",

    1: "Pre-Series A",

    2: "Series A",

    3: "Series B+"

}

df["Funding_Stage_Name"] = df["Funding_Stage_Label"].map(stage_names)

# ==========================================================
# CHECK DISTRIBUTION
# ==========================================================

print("=" * 60)

print("Funding Stage Distribution")

print(df["Funding_Stage_Name"].value_counts())

print("=" * 60)



df.to_csv(

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv",

    index=False

)

print("="*60)

print("Funding Stage Distribution")

print(df["Funding_Stage_Label"].value_counts().sort_index())