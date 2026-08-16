# ==========================================================
# VentureDecision
# PORTFOLIO FIT MODEL INFERENCE
# MULTI-CLASS PREDICTION ON NEW STARTUPS
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
    r"\Machine Learning\models\portfolio_fit.pkl"
)


# ==========================================================
# LOAD NEW FEATURE-ENGINEERED DATA
# ==========================================================

new_df = pd.read_csv(NEW_DATA_PATH)

print("New feature-engineered dataset loaded successfully.")

print(f"Number of startups: {len(new_df)}")


# ==========================================================
# LOAD TRAINED MULTI-CLASS MODEL
# ==========================================================

model = joblib.load(MODEL_PATH)

print("\nTrained multi-class portfolio fit model loaded successfully.")


# ==========================================================
# GET EXACT FEATURES USED DURING TRAINING
# ==========================================================

feature_columns = model.feature_names_in_

print("\nNumber of features expected by model:")

print(len(feature_columns))


print("\nFeatures expected by model:")

print(feature_columns.tolist())


# ==========================================================
# PREPARE NEW DATA
# ==========================================================

# Convert categorical columns into dummy variables
X_new = pd.get_dummies(

    new_df,

    drop_first=True

)


# ==========================================================
# ALIGN NEW DATASET WITH TRAINING FEATURES
# ==========================================================

X_new = X_new.reindex(

    columns=feature_columns,

    fill_value=0

)


# ==========================================================
# HANDLE MISSING VALUES
# ==========================================================

X_new = X_new.fillna(

    X_new.median(numeric_only=True)

)

X_new = X_new.fillna(0)


print("\nX_new created successfully.")

print(f"X_new shape: {X_new.shape}")


# ==========================================================
# MULTI-CLASS PREDICTION
# ==========================================================

predicted_class = model.predict(X_new)


# ==========================================================
# PREDICT PROBABILITY FOR ALL CLASSES
# ==========================================================

predicted_probability = model.predict_proba(X_new)


# ==========================================================
# GET MODEL CLASSES
# ==========================================================

model_classes = model.classes_


print("\nModel classes:")

print(model_classes)


# ==========================================================
# GET CONFIDENCE OF PREDICTED CLASS
# ==========================================================

portfolio_fit_probability = (

    predicted_probability.max(axis=1) * 100

).round(2)


# ==========================================================
# ADD PREDICTION RESULTS
# ==========================================================

new_df["Portfolio_Fit_Prediction"] = predicted_class

new_df["Portfolio_Fit_Probability"] = (

    portfolio_fit_probability

)


# ==========================================================
# ADD PROBABILITY FOR EACH CLASS
# ==========================================================

for i, class_name in enumerate(model_classes):

    new_df[

        f"Portfolio_Fit_Class_{class_name}_Probability"

    ] = (

        predicted_probability[:, i] * 100

    ).round(2)


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

print("PORTFOLIO FIT MULTI-CLASS PREDICTIONS GENERATED SUCCESSFULLY")

print("============================================================")


display_columns = [

    "Startup_ID",

    "Startup_Name",

    "Portfolio_Fit_Prediction",

    "Portfolio_Fit_Probability"

]


for class_name in model_classes:

    display_columns.append(

        f"Portfolio_Fit_Class_{class_name}_Probability"

    )


print(

    new_df[display_columns].head(10)

)


print("\nUpdated file saved at:")

print(NEW_DATA_PATH)