
import pandas as pd


# ==========================================================
# VENTUREDECISION
# NEW STARTUPS
# COMPETITIVE SURVIVAL SCORING ENGINE
# ==========================================================


# ==========================================================
# PATH
# ==========================================================

NEW_DATA_PATH = (

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision"

    r"\data\processed\new_feature_engineered_startups.csv"

)


# ==========================================================
# LOAD NEW DATASET
# ==========================================================

df = pd.read_csv(

    NEW_DATA_PATH

)


print(

    "New feature-engineered dataset loaded successfully."

)

print(

    f"Number of startups: {len(df)}"

)


# ==========================================================
# COMPETITIVE SURVIVAL PROBABILITY
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

print(

    "COMPETITIVE SURVIVAL PROBABILITY GENERATED"

)

print("=" * 60)


print(

    df[

        [

            "Startup_ID",

            "Startup_Name",

            "Competitive_Survival_Probability"

        ]

    ].head(10)

)


print()

print(

    df["Competitive_Survival_Probability"].describe()

)


# ==========================================================
# SAVE UPDATED NEW DATASET
# ==========================================================

df.to_csv(

    NEW_DATA_PATH,

    index=False

)


print("=" * 60)

print(

    "New dataset updated successfully."

)

print(

    NEW_DATA_PATH

)

print("=" * 60)