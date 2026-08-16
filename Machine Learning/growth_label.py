import pandas as pd
import numpy as np

# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"
)

# ==========================================================
# GROWTH LABEL
# Top 25% Growth Score = High Growth Potential
# ==========================================================

growth_threshold = df["Growth_Score"].quantile(0.75)

print("=" * 60)
print(f"Growth Threshold : {growth_threshold:.2f}")
print("=" * 60)

df["Growth_Label"] = np.where(

    df["Growth_Score"] >= growth_threshold,

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

print("Growth Label Distribution")

print(df["Growth_Label"].value_counts())

print("\nDataset Updated Successfully!")