
# ==========================================================
# VentureDecision
# FUNDING REQUIREMENT MODEL INFERENCE
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
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\Machine Learning\models\funding_requirement.pkl"
)


# ==========================================================
# LOAD NEW FEATURE-ENGINEERED DATA
# ==========================================================

new_df = pd.read_csv(NEW_DATA_PATH)

print("New feature-engineered dataset loaded successfully.")

print(f"Number of startups: {len(new_df)}")


# ==========================================================
# LOAD TRAINED MODEL
# ==========================================================

model = joblib.load(MODEL_PATH)

print(
    "\nTrained multi-class funding requirement model "
    "loaded successfully."
)


# ==========================================================
# GET EXACT TRAINING FEATURES
# ==========================================================

feature_columns = model.feature_names_in_


print("\nNumber of features expected by model:")

print(len(feature_columns))


print("\nFeatures expected by model:")

print(feature_columns.tolist())


# ==========================================================
# PREPARE NEW DATA
# ==========================================================

X_new = pd.get_dummies(

    new_df,

    drop_first=True

)


# ==========================================================
# ALIGN FEATURES WITH TRAINING DATA
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
# MODEL CLASSES
# ==========================================================

model_classes = model.classes_


print("\nFunding Requirement Classes:")

print(model_classes)


# ==========================================================
# CONFIDENCE OF PREDICTION
# ==========================================================

funding_requirement_probability = (

    predicted_probability.max(axis=1) * 100

).round(2)


# ==========================================================
# ADD MAIN PREDICTION RESULTS
# ==========================================================

new_df["Funding_Requirement_Prediction"] = (

    predicted_class

)


new_df["Funding_Requirement_Probability"] = (

    funding_requirement_probability

)


# ==========================================================
# ADD PROBABILITY FOR EVERY CLASS
# ==========================================================

for i, class_name in enumerate(model_classes):

    new_df[

        f"Funding_Requirement_Class_{class_name}_Probability"

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

print(

    "FUNDING REQUIREMENT MULTI-CLASS PREDICTIONS "

    "GENERATED SUCCESSFULLY"

)

print("============================================================")


display_columns = [

    "Startup_ID",

    "Startup_Name",

    "Funding_Requirement_Prediction",

    "Funding_Requirement_Probability"

]


for class_name in model_classes:

    display_columns.append(

        f"Funding_Requirement_Class_{class_name}_Probability"

    )


print(

    new_df[display_columns].head(10)

)


print("\nUpdated file saved at:")

print(NEW_DATA_PATH)