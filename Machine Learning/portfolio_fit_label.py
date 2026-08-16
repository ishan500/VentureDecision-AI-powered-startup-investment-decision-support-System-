import pandas as pd

# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"
)

# ==========================================================
# CREATE PORTFOLIO FIT SCORE
# ==========================================================

df["Portfolio_Fit_Score"] = (

    0.30 * df["Investor_Confidence_Score"]

    +

    0.25 * df["Financial_Health_Score"]

    +

    0.20 * df["Operational_Strength_Score"]

    +

    0.15 * df["Competitive_Strength_Score"]

    +

    0.10 * df["Market_Opportunity_Score"]

)

# ==========================================================
# NORMALIZE SCORE (0-100)
# ==========================================================

minimum = df["Portfolio_Fit_Score"].min()

maximum = df["Portfolio_Fit_Score"].max()

df["Portfolio_Fit_Score"] = (

    (df["Portfolio_Fit_Score"] - minimum)

    /

    (maximum - minimum)

) * 100

# ==========================================================
# CALCULATE QUARTILES
# ==========================================================

q25 = df["Portfolio_Fit_Score"].quantile(0.25)

q50 = df["Portfolio_Fit_Score"].quantile(0.50)

q75 = df["Portfolio_Fit_Score"].quantile(0.75)

print("=" * 60)

print("Portfolio Fit Thresholds")

print(f"25% : {q25:.2f}")

print(f"50% : {q50:.2f}")

print(f"75% : {q75:.2f}")

print("=" * 60)

# ==========================================================
# CREATE LABEL
# ==========================================================

df["Portfolio_Fit_Label"] = 0

df.loc[
    df["Portfolio_Fit_Score"] > q25,
    "Portfolio_Fit_Label"
] = 1

df.loc[
    df["Portfolio_Fit_Score"] > q50,
    "Portfolio_Fit_Label"
] = 2

df.loc[
    df["Portfolio_Fit_Score"] > q75,
    "Portfolio_Fit_Label"
] = 3

# ==========================================================
# LABEL NAMES
# ==========================================================

portfolio_names = {

    0: "Poor Fit",

    1: "Moderate Fit",

    2: "Good Fit",

    3: "Excellent Fit"

}

df["Portfolio_Fit_Name"] = df["Portfolio_Fit_Label"].map(
    portfolio_names
)

# ==========================================================
# SAVE DATASET
# ==========================================================

df.to_csv(

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv",

    index=False

)

# ==========================================================
# OUTPUT
# ==========================================================

print("=" * 60)

print("Portfolio Fit Distribution")

print(df["Portfolio_Fit_Label"].value_counts().sort_index())

print()

print("Portfolio Fit Distribution (%)")

print(

    (

        df["Portfolio_Fit_Label"]

        .value_counts(normalize=True)

        .sort_index()

        * 100

    ).round(2)

)

print("=" * 60)

print("Dataset Updated Successfully!")