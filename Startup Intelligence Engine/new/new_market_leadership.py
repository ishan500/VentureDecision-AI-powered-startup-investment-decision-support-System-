import pandas as pd


# ==========================================================
# VentureDecision
# NEW STARTUPS
# MARKET LEADERSHIP PROBABILITY
# STARTUP INTELLIGENCE ENGINE
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
# MARKET LEADERSHIP PROBABILITY
# ==========================================================

df["Market_Leadership_Probability"] = (

      0.30 * df["Market_Opportunity_Score"]

    + 0.25 * df["Competitive_Strength_Score"]

    + 0.20 * df["Growth_Score"]

    + 0.15 * df["Popularity_Score"]

    + 0.10 * df["Investor_Confidence_Score"]

).round(2)


# ==========================================================
# DISPLAY RESULTS
# ==========================================================

print("=" * 60)

print(

    "MARKET LEADERSHIP PROBABILITY GENERATED"

)

print("=" * 60)


print(

    df[

        [

            "Startup_ID",

            "Startup_Name",

            "Market_Leadership_Probability"

        ]

    ].head(10)

)


print()

print(

    df["Market_Leadership_Probability"].describe()

)


# ==========================================================
# SAVE UPDATED DATASET
# ==========================================================

df.to_csv(

    NEW_DATA_PATH,

    index=False

)


print("=" * 60)

print(

    "NEW DATASET UPDATED SUCCESSFULLY"

)

print(

    NEW_DATA_PATH

)

print("=" * 60)