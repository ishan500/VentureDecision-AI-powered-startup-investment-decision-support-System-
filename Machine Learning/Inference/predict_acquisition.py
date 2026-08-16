
# ==========================================================
# VentureDecision
# ACQUISITION MODEL INFERENCE
# PREDICTION ON NEW STARTUPS
# ==========================================================

import pandas as pd
import joblib


# ==========================================================
# PATHS
# ==========================================================

NEW_DATA_PATH = (
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision"
    r"\data\processed\new_feature_engineered_startups.csv"
)

MODEL_PATH = (
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision"
    r"\Machine Learning\models\acquisition_probability.pkl"
)


# ==========================================================
# LOAD NEW FEATURE-ENGINEERED DATA
# ==========================================================

new_df = pd.read_csv(NEW_DATA_PATH)

print("New feature-engineered dataset loaded successfully.")

print(f"Number of startups: {len(new_df)}")


# ==========================================================
# SAME FEATURES USED DURING MODEL TRAINING
# ==========================================================

feature_columns = [

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

]


# ==========================================================
# CREATE X_NEW
# ==========================================================

X_new = new_df[feature_columns]

print("\nX_new created successfully.")

print(f"X_new shape: {X_new.shape}")


# ==========================================================
# LOAD TRAINED MODEL
# ==========================================================

model = joblib.load(MODEL_PATH)

print("\nTrained acquisition probability model loaded successfully.")


# ==========================================================
# PREDICTION
# ==========================================================

# Predicted acquisition class
predicted_class = model.predict(X_new)


# ==========================================================
# PREDICTED ACQUISITION PROBABILITY
# ==========================================================

predicted_probability = model.predict_proba(X_new)


# Probability of acquisition = class 1

acquisition_probability = (

    predicted_probability[:, 1] * 100

).round(2)


# ==========================================================
# ADD PREDICTION RESULTS TO DATASET
# ==========================================================

new_df["Acquisition_Prediction"] = predicted_class


new_df["Acquisition_Probability"] = acquisition_probability


# ==========================================================
# SAVE UPDATED DATASET
# ==========================================================

new_df.to_csv(

    NEW_DATA_PATH,

    index=False

)


# ==========================================================
# DISPLAY RESULTS
# ==========================================================

print("\n============================================================")

print("ACQUISITION PREDICTIONS GENERATED SUCCESSFULLY")

print("============================================================")


print(

    new_df[

        [

            "Startup_ID",

            "Startup_Name",

            "Acquisition_Prediction",

            "Acquisition_Probability"

        ]

    ].head(10)

)


print("\nUpdated file saved at:")

print(NEW_DATA_PATH)