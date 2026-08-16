import pandas as pd

df = pd.read_csv(
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"
)

print(
    df[["Portfolio_Fit_Label",
        "Portfolio_Fit_Name"]]
    .drop_duplicates()
    .sort_values("Portfolio_Fit_Label")
)