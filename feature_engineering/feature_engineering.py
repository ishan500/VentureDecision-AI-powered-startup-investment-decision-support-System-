# VentureDecision
import pandas as pd 
from normalization import *
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()



startup = pd.read_csv(r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\startup_information.csv")
funding = pd.read_csv(r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\funding_financial.csv")
growth = pd.read_csv(r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\growth_market.csv")
news = pd.read_csv(r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\news_sentiment.csv")
exit_history = pd.read_csv(r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\exit_history.csv")
print("All datasets loaded successfully.\n")

# Inspecting Dataset
datasets = {
    "Startup Information": startup,
    "Funding Financial": funding,
    "Growth Market": growth,
    "News Sentiment": news,
    "Exit History": exit_history
}

for name, df in datasets.items():

    print("=" * 70)
    print(name.upper())
    print("=" * 70)

    print("\nShape")
    print(df.shape)

    print("\nColumns")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nFirst Five Rows")
    print(df.head())

    print("\n")

# merge dataframes and remove duplicate colloumns 
funding = funding.drop(columns=["Startup_Name"])
growth = growth.drop(columns=["Startup_Name"])
news = news.drop(columns=["Startup_Name"])
exit_history = exit_history.drop(columns=["Startup_Name"])

merged_df = startup.merge(funding, on="Startup_ID")
merged_df = merged_df.merge(growth, on="Startup_ID")
merged_df = merged_df.merge(news, on="Startup_ID")
merged_df = merged_df.merge(exit_history, on="Startup_ID")

print("Datasets merged successfully.\n")

print("Merged Dataset Shape")
print(merged_df.shape)

print("\nMerged Dataset Preview")
print(merged_df.head())

print("\nMerged Dataset Columns")
print(merged_df.columns.tolist())

print("\nMissing Values After Merge")
print(merged_df.isnull().sum())



merged_df["Valuation"] = merged_df["Valuation"].apply(normalize_currency)

merged_df["Revenue"] = merged_df["Revenue"].apply(normalize_revenue)
merged_df["Gross_Margin"] = merged_df["Gross_Margin"].apply(normalize_percentage)

merged_df["Monthly_Visits"] = merged_df["Monthly_Visits"].apply(normalize_traffic)

merged_df["App_Downloads"] = merged_df["App_Downloads"].apply(normalize_downloads)

merged_df["App_Rating"] = merged_df["App_Rating"].apply(normalize_rating)

merged_df["App_Reviews_Count"] = merged_df["App_Reviews_Count"].apply(normalize_reviews)

merged_df["Total_Funding_Raised"] = merged_df["Total_Funding_Raised"].apply(normalize_funding)

merged_df["Latest_Funding_Amount"] = merged_df["Latest_Funding_Amount"].apply(normalize_funding)
merged_df["Profit_or_Loss"] = merged_df["Profit_or_Loss"].apply(normalize_profit_loss)

merged_df["TAM"] = merged_df["TAM"].apply(normalize_tam)
merged_df["Employee_Count"] = merged_df["Employee_Count"].apply(normalize_employee_count)
merged_df["TAM_Growth_Rate"] = merged_df["TAM_Growth_Rate"].apply(normalize_percentage)





# Verify 
print(
    merged_df[
        [
            "Total_Funding_Raised",
    "Latest_Funding_Amount",
    "Valuation",
    "Revenue"
    
    

        ]
    ].head(10)
)

# Score Calculation
# Funding Score 
funding_features = merged_df[[
    "Total_Funding_Raised",
    "Latest_Funding_Amount",
    "Number_of_Funding_Rounds"
]].fillna(0)

funding_scaled = scaler.fit_transform(funding_features)

merged_df["Funding_Score"] = (
    funding_scaled[:, 0] * 0.45 +
    funding_scaled[:, 1] * 0.35 +
    funding_scaled[:, 2] * 0.20
) * 100

# Financial Health Score 
financial_features = merged_df[[
    "Revenue",
    "Profit_or_Loss",
    "Gross_Margin"
]].fillna(0)

financial_scaled = scaler.fit_transform(financial_features)

merged_df["Financial_Health_Score"] = (
    financial_scaled[:, 0] * 0.50 +
    financial_scaled[:, 1] * 0.20 +
    financial_scaled[:, 2] * 0.30
) * 100

# Growth Score 
growth_features = merged_df[[
    "Employee_Count",
    "Monthly_Visits",
    "App_Downloads",
    "Google_Trends_Score"
]].fillna(0)

growth_scaled = scaler.fit_transform(growth_features)

merged_df["Growth_Score"] = (
    growth_scaled[:, 0] * 0.20 +
    growth_scaled[:, 1] * 0.35 +
    growth_scaled[:, 2] * 0.30 +
    growth_scaled[:, 3] * 0.15
) * 100

# Market Oppertunity Score 
market_features = merged_df[[
    "TAM",
    "TAM_Growth_Rate"
]].fillna(0)

market_scaled = scaler.fit_transform(market_features)

merged_df["Market_Opportunity_Score"] = (
    market_scaled[:, 0] * 0.70 +
    market_scaled[:, 1] * 0.30
) * 100

# Popularity Score 
popularity_features = merged_df[[
    "Monthly_Visits",
    "App_Downloads",
    "App_Rating",
    "App_Reviews_Count"
]].fillna(0)

popularity_scaled = scaler.fit_transform(popularity_features)

merged_df["Popularity_Score"] = (
    popularity_scaled[:, 0] * 0.30 +
    popularity_scaled[:, 1] * 0.30 +
    popularity_scaled[:, 2] * 0.20 +
    popularity_scaled[:, 3] * 0.20
) * 100

# Media Buzz Score
media_features = merged_df[[
    "Total_News_Count",
    "Positive_News_Count"
]].fillna(0)

media_scaled = scaler.fit_transform(media_features)

merged_df["Media_Buzz_Score"] = (
    media_scaled[:, 0] * 0.70 +
    media_scaled[:, 1] * 0.30
) * 100

# Sentiment Score
merged_df["Sentiment_Score"] = (
    (
        merged_df["Positive_News_Count"]
        - merged_df["Negative_News_Count"]
    )
    /
    (
        merged_df["Total_News_Count"] + 1
    )
) * 100

# Exit Score
exit_features = merged_df[[
    "Exit_Valuation_USD_Million",
    "Years_to_Exit"
]].fillna(0)

exit_scaled = scaler.fit_transform(exit_features)

merged_df["Exit_Score"] = (
    exit_scaled[:, 0] * 0.70 +
    (1 - exit_scaled[:, 1]) * 0.30
) * 100

# Startup Maturity Score
current_year = 2026

merged_df["Startup_Age"] = current_year - merged_df["founded_year"]

maturity_features = merged_df[[
    "Startup_Age",
    "Employee_Count",
    "Revenue"
]].fillna(0)

maturity_scaled = scaler.fit_transform(maturity_features)

merged_df["Startup_Maturity_Score"] = (
    maturity_scaled[:, 0] * 0.30 +
    maturity_scaled[:, 1] * 0.30 +
    maturity_scaled[:, 2] * 0.40
) * 100

# Investor Confidence Score
investor_features = merged_df[[
    "Funding_Score",
    "Valuation",
    "Number_of_Funding_Rounds"
]].fillna(0)

investor_scaled = scaler.fit_transform(investor_features)

merged_df["Investor_Confidence_Score"] = (
    investor_scaled[:, 0] * 0.40 +
    investor_scaled[:, 1] * 0.40 +
    investor_scaled[:, 2] * 0.20
) * 100

# Operational Strength Score
operational_features = merged_df[[
    "Revenue",
    "Profit_or_Loss",
    "Gross_Margin",
    "Employee_Count"
]].fillna(0)

operational_scaled = scaler.fit_transform(operational_features)

merged_df["Operational_Strength_Score"] = (
    operational_scaled[:, 0] * 0.30 +
    operational_scaled[:, 1] * 0.20 +
    operational_scaled[:, 2] * 0.30 +
    operational_scaled[:, 3] * 0.20
) * 100

# Competitive Strength Score
competitive_features = merged_df[[
    "Growth_Score",
    "Market_Opportunity_Score",
    "Popularity_Score",
    "Funding_Score"
]].fillna(0)

competitive_scaled = scaler.fit_transform(competitive_features)

merged_df["Competitive_Strength_Score"] = (
    competitive_scaled[:, 0] * 0.30 +
    competitive_scaled[:, 1] * 0.30 +
    competitive_scaled[:, 2] * 0.20 +
    competitive_scaled[:, 3] * 0.20
) * 100

# Valuation Score
valuation_features = merged_df[[
    "Valuation",
    "Revenue",
    "Funding_Score"
]].fillna(0)

valuation_scaled = scaler.fit_transform(valuation_features)

merged_df["Valuation_Score"] = (
    valuation_scaled[:, 0] * 0.50 +
    valuation_scaled[:, 1] * 0.30 +
    valuation_scaled[:, 2] * 0.20
) * 100

# Overall Startup Score
overall_features = merged_df[[
    "Funding_Score",
    "Financial_Health_Score",
    "Growth_Score",
    "Market_Opportunity_Score",
    "Popularity_Score",
    "Media_Buzz_Score",
    "Sentiment_Score",
    "Exit_Score",
    "Startup_Maturity_Score",
    "Investor_Confidence_Score",
    "Operational_Strength_Score",
    "Competitive_Strength_Score",
    "Valuation_Score"
]].fillna(0)

overall_scaled = scaler.fit_transform(overall_features)

weights = [
    0.10,  # Funding
    0.10,  # Financial
    0.10,  # Growth
    0.10,  # Market
    0.07,  # Popularity
    0.05,  # Media Buzz
    0.05,  # Sentiment
    0.08,  # Exit
    0.08,  # Maturity
    0.08,  # Investor Confidence
    0.08,  # Operational Strength
    0.06,  # Competitive Strength
    0.05   # Valuation
]

merged_df["Overall_Startup_Score"] = (
    overall_scaled * weights
).sum(axis=1) * 100
# Verify First Five 
print("\nFINAL FEATURE ENGINEERING SCORES\n")

print(
    merged_df[
        [
            "Startup_Name",
            "Funding_Score",
            "Financial_Health_Score",
            "Growth_Score",
            "Market_Opportunity_Score",
            "Popularity_Score",
            "Media_Buzz_Score",
            "Sentiment_Score",
            "Exit_Score",
            "Startup_Maturity_Score",
            "Investor_Confidence_Score",
            "Operational_Strength_Score",
            "Competitive_Strength_Score",
            "Valuation_Score",
            "Overall_Startup_Score"
        ]
    ].head(10)
)

# SAVE FEATURE ENGINEERED DATASET

merged_df.to_csv(
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\feature_engineered_startups.csv",
    index=False
)

print("\n==========================================")
print("Feature Engineered Dataset Saved Successfully!")
print("Location:")
print(r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\feature_engineered_startups.csv")
print("==========================================")


