import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split

from sklearn.metrics import (

    accuracy_score,

    precision_score,

    recall_score,

    f1_score,

    confusion_matrix

)

from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier

# ==========================================================
# TARGET
# ==========================================================

TARGET_COLUMN = "Funding_Requirement_Label"

MODEL_NAME = "funding_requirement.pkl"

# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"

)

# ==========================================================
# FEATURES
# ==========================================================

feature_columns = [

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

X = df[feature_columns]

y = df[TARGET_COLUMN]

# ==========================================================
# CHECK DISTRIBUTION
# ==========================================================

print("="*60)

print(df[TARGET_COLUMN].value_counts())

print("="*60)

# ==========================================================
# TRAIN TEST SPLIT
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

# ==========================================================
# MODELS
# ==========================================================

models = {

    "Logistic Regression": LogisticRegression(

        max_iter=1000

    ),

    "Random Forest": RandomForestClassifier(

        n_estimators=300,

        random_state=42

    ),

    "XGBoost": XGBClassifier(

        n_estimators=300,

        learning_rate=0.05,

        max_depth=5,

        subsample=0.8,

        colsample_bytree=0.8,

        random_state=42,

        eval_metric="logloss"

    )

}

# ==========================================================
# MODEL PRIORITY
# Lower number = Higher priority
# ==========================================================

model_priority = {

    "Logistic Regression": 1,

    "Random Forest": 2,

    "XGBoost": 3

}

# ==========================================================
# BEST MODEL VARIABLES
# ==========================================================

best_model = None

best_model_name = ""

best_accuracy = 0

best_f1 = 0


# ==========================================================
# FLOAT COMPARISON TOLERANCE
# ==========================================================

EPSILON = 1e-6

# ==========================================================
# TRAINING
# ==========================================================

# ==========================================================
# TRAINING
# ==========================================================

for name, model in models.items():

    model.fit(

        X_train,

        y_train

    )

    prediction = model.predict(

        X_test

    )

    accuracy = accuracy_score(

        y_test,

        prediction

    )

    precision = precision_score(

        y_test,

        prediction,

        zero_division=0

    )

    recall = recall_score(

        y_test,

        prediction,

        zero_division=0

    )

    f1 = f1_score(

        y_test,

        prediction,

        average="weighted",

        zero_division=0

    )

    cm = confusion_matrix(

        y_test,

        prediction

    )

    print("=" * 60)

    print(name)

    print(f"Accuracy  : {accuracy:.3f}")

    print(f"Precision : {precision:.3f}")

    print(f"Recall    : {recall:.3f}")

    print(f"Weighted F1 : {f1:.3f}")

    print()

    print("Confusion Matrix")

    print(cm)

    print()

    # ======================================================
    # MODEL SELECTION
    # ======================================================

    if (

        accuracy > best_accuracy + EPSILON

        or

        (

            abs(accuracy - best_accuracy) <= EPSILON

            and

            f1 > best_f1 + EPSILON

        )

        or

        (

            abs(accuracy - best_accuracy) <= EPSILON

            and

            abs(f1 - best_f1) <= EPSILON

            and

            model_priority[name] < model_priority.get(best_model_name, 999)

        )

    ):

        best_accuracy = accuracy

        best_f1 = f1

        best_model = model

        best_model_name = name


# ==========================================================
# BEST MODEL
# ==========================================================

print("=" * 60)

print("Best Model Selected")

print(best_model_name)

print(f"Accuracy : {best_accuracy:.3f}")

print(f"Weighted F1 : {best_f1:.3f}")

joblib.dump(

    best_model,

    rf"C:\Users\Ishan  Singh\Desktop\VentureDecision\Machine Learning\models\{MODEL_NAME}"

)

print()

print("Model Saved Successfully")


# ==========================================================
# GENERATE PREDICTIONS FOR ENTIRE DATASET
# ==========================================================

# Predicted Class

df["Predicted_Funding_Requirement"] = best_model.predict(X)

# Prediction Probability (%)

df["Funding_Requirement_Probability"] = (

    best_model.predict_proba(X)[:,1] * 100

).round(2)

# ==========================================================
# OPTIONAL : CONVERT TO READABLE NAME
# ==========================================================

funding_requirement_mapping = {

    0: "Low Funding Required",

    1: "High Funding Required"

}

df["Predicted_Funding_Requirement_Name"] = (

    df["Predicted_Funding_Requirement"].map(

        funding_requirement_mapping

    )

)

# ==========================================================
# SAVE UPDATED CSV
# ==========================================================

df.to_csv(

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv",

    index=False

)

print()

print("Funding Requirement Predictions Saved Successfully")