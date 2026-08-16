
import pandas as pd


# ==========================================================
# VentureDecision
# NEW STARTUPS
# VALUATION GROWTH PREDICTION
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
# VALUATION GROWTH PREDICTION
# ==========================================================

df["Valuation_Growth_Prediction"] = (

      0.30 * df["Growth_Score"]

    + 0.20 * df["Financial_Health_Score"]

    + 0.20 * df["Market_Opportunity_Score"]

    + 0.15 * df["Competitive_Strength_Score"]

    + 0.10 * df["Investor_Confidence_Score"]

    + 0.05 * df["Operational_Strength_Score"]

).round(2)


# ==========================================================
# DISPLAY RESULTS
# ==========================================================

print("=" * 60)

print(

    "VALUATION GROWTH PREDICTION GENERATED"

)

print("=" * 60)


print(

    df[

        [

            "Startup_ID",

            "Startup_Name",

            "Valuation_Growth_Prediction"

        ]

    ].head(10)

)


print()

print(

    df["Valuation_Growth_Prediction"].describe()

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