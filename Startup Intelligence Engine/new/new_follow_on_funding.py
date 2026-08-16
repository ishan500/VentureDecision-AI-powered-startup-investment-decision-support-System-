import pandas as pd


# ==========================================================
# VentureDecision
# NEW STARTUPS
# FOLLOW-ON FUNDING SCORING ENGINE
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
# FOLLOW-ON FUNDING PROBABILITY
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

    df["Follow_On_Funding_Probability"]

    .round(2)

)


# ==========================================================
# DISPLAY RESULTS
# ==========================================================

print("=" * 60)

print(

    "FOLLOW-ON FUNDING PROBABILITY GENERATED"

)

print("=" * 60)


print(

    df[

        [

            "Startup_ID",

            "Startup_Name",

            "Follow_On_Funding_Probability"

        ]

    ].head(10)

)


print()

print(

    df["Follow_On_Funding_Probability"].describe()

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