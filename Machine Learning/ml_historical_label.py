import pandas as pd
import numpy as np

# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"
)

# ==========================================================
# EXIT LABEL
# ==========================================================

df["Exit_Label"] = np.where(
    df["Historical_Exit_Type"].isin(["IPO", "Acquisition"]),
    1,
    0
)

# ==========================================================
# IPO LABEL
# ==========================================================

df["IPO_Label"] = np.where(

    df["Historical_Exit_Type"].fillna("").str.upper() == "IPO",

    1,

    0

)

# ==========================================================
# ACQUISITION LABEL
# ==========================================================

df["Acquisition_Label"] = np.where(

    df["Historical_Exit_Type"].fillna("").str.lower() == "acquisition",

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
# VERIFY
# ==========================================================

print("="*60)

print("Exit Label")

print(df["Exit_Label"].value_counts())

print()

print("="*60)

print("IPO Label")

print(df["IPO_Label"].value_counts())

print()

print("="*60)

print("Acquisition Label")

print(df["Acquisition_Label"].value_counts())

print()

print("="*60)

print("Historical Labels Created Successfully!")