
# ==========================================================
# VentureDecision
# EXIT MODEL INFERENCE
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
    r"\Machine Learning\models\exit_probability.pkl"
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
# CHECK REQUIRED FEATURES
# ==========================================================

missing_features = [

    feature

    for feature in feature_columns

    if feature not in new_df.columns

]


if missing_features:

    raise ValueError(

        f"Missing features in new dataset: {missing_features}"

    )


# ==========================================================
# CREATE X_NEW
# ==========================================================

X_new = new_df[feature_columns]

print("\nX_new created successfully.")

print(f"X_new shape: {X_new.shape}")


# ==========================================================
# LOAD TRAINED EXIT MODEL
# ==========================================================

model = joblib.load(MODEL_PATH)

print("\nTrained Exit Probability model loaded successfully.")


# ==========================================================
# PREDICTION
# ==========================================================

# Predicted Exit class

predicted_class = model.predict(X_new)


# ==========================================================
# PREDICTED EXIT PROBABILITY
# ==========================================================

predicted_probability = model.predict_proba(X_new)


# Probability of Exit = class 1

exit_probability = (

    predicted_probability[:, 1] * 100

).round(2)


# ==========================================================
# ADD PREDICTION RESULTS TO DATASET
# ==========================================================

new_df["Exit_Prediction"] = predicted_class

new_df["Exit_Probability"] = exit_probability


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

print("EXIT PREDICTIONS GENERATED SUCCESSFULLY")

print("============================================================")


print(

    new_df[

        [

            "Startup_ID",

            "Startup_Name",

            "Exit_Prediction",

            "Exit_Probability"

        ]

    ].head(10)

)


print("\nUpdated file saved at:")

print(NEW_DATA_PATH)