import pandas as pd
import numpy as np

# ==========================================================
# LOAD FEATURE ENGINEERED DATASET
# ==========================================================

df = pd.read_csv(
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"
)

# ==========================================================
# CHECK SCORE DISTRIBUTION
# ==========================================================

print("=" * 60)
print("Overall Startup Score")
print(df["Overall_Startup_Score"].describe())

print("\nValuation Score")
print(df["Valuation_Score"].describe())

print("\nGrowth Score")
print(df["Growth_Score"].describe())

print("\nFunding Score")
print(df["Funding_Score"].describe())

# ==========================================================
# STARTUP CATEGORY
# ==========================================================

df["Startup_Category"] = np.select(

    [

        df["Overall_Startup_Score"] >= 50,

        (df["Overall_Startup_Score"] >= 36) &
        (df["Overall_Startup_Score"] < 50),

        (df["Overall_Startup_Score"] >= 21) &
        (df["Overall_Startup_Score"] < 36),

        df["Overall_Startup_Score"] < 21

    ],

    [

        "Excellent",

        "Good",

        "Average",

        "Weak"

    ],

    default="Weak"

)

# ==========================================================
# SUCCESS LABEL
# Startups with Overall Startup Score >= 36 are considered successful
# ==========================================================

df["Success_Label"] = np.where(

    df["Overall_Startup_Score"] >= 36,

    1,

    0

)

# ==========================================================
# UNICORN LABEL
# Based on valuation, growth and funding together
# ==========================================================

df["Unicorn_Label"] = np.where(

    (df["Valuation_Score"] >= 17) &

    (df["Growth_Score"] >= 32) &

    (df["Funding_Score"] >= 15),

    1,

    0

)

# ==========================================================
# SAVE DATASET
# ==========================================================

df.to_csv(

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv",

    index=False

)

# ==========================================================
# VERIFY LABELS
# ==========================================================

print("\n")
print("=" * 60)

print("Startup Category Distribution")

print(df["Startup_Category"].value_counts())

print("\n")

print("=" * 60)

print("Success Label Distribution")

print(df["Success_Label"].value_counts(normalize=True) * 100)
print("\n")

print("=" * 60)

print("Unicorn Label Distribution")

print(df["Unicorn_Label"].value_counts())

print("\n")

print("=" * 60)

print("Dataset Updated Successfully")