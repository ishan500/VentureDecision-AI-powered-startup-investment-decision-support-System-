
# ==========================================================
# VentureDecision
# GROWTH PREDICTION + PROBABILITY INFERENCE
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
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\Machine Learning\models\growth_potential.pkl"
    
)


# ==========================================================
# LOAD NEW FEATURE-ENGINEERED DATA
# ==========================================================

new_df = pd.read_csv(NEW_DATA_PATH)

print("New feature-engineered dataset loaded successfully.")

print(f"Number of startups: {len(new_df)}")


# ==========================================================
# CHECK FEATURES USED DURING TRAINING
# ==========================================================

model = joblib.load(MODEL_PATH)

print("\nTrained growth model loaded successfully.")

print("\nFeatures expected by the trained model:")

if hasattr(model, "feature_names_in_"):

    feature_columns = model.feature_names_in_.tolist()

    print(feature_columns)

else:

    print("Model does not store feature names.")

    feature_columns = [

    "Funding_Score",

    "Financial_Health_Score",

    # Remove "Growth_Score"

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
# PREDICTION
# ==========================================================

predicted_class = model.predict(X_new)


# ==========================================================
# PROBABILITY
# ==========================================================

if hasattr(model, "predict_proba"):

    predicted_probability = model.predict_proba(X_new)

    # Probability of class 1
    growth_probability = (

        predicted_probability[:, 1] * 100

    ).round(2)

else:

    growth_probability = None


# ==========================================================
# ADD RESULTS TO DATASET
# ==========================================================

new_df["Growth_Prediction"] = predicted_class


if growth_probability is not None:

    new_df["Growth_Probability"] = growth_probability


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

print("GROWTH PREDICTIONS GENERATED SUCCESSFULLY")

print("============================================================")


print(

    new_df[

        [

            "Startup_ID",

            "Startup_Name",

            "Growth_Prediction",

            "Growth_Probability"

        ]

    ].head(10)

)


print("\nUpdated file saved at:")

print(NEW_DATA_PATH)