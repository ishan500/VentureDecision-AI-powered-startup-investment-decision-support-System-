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
# TARGET COLUMN
# ==========================================================

TARGET_COLUMN = "Success_Label"

MODEL_NAME = "success_probability.pkl"

# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(
    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"
)

# ==========================================================
# FEATURE COLUMNS
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

X = df[feature_columns]

y = df[TARGET_COLUMN]

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
# BEST MODEL TRACKER
# ==========================================================

# ==========================================================
# BEST MODEL TRACKER
# PRIMARY METRIC    = F1 SCORE
# SECONDARY METRIC = ACCURACY
# ==========================================================

best_model = None

best_model_name = ""

best_f1 = 0

best_accuracy = 0

EPSILON = 1e-6

# ==========================================================
# MODEL TRAINING
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

        prediction

    )

    recall = recall_score(

        y_test,

        prediction

    )

    f1 = f1_score(

        y_test,

        prediction

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

    print(f"F1 Score  : {f1:.3f}")

    print()

    print("Confusion Matrix")

    print(cm)

    print()


    # ======================================================
    # MODEL SELECTION
    # PRIMARY    = F1 SCORE
    # SECONDARY  = ACCURACY
    # ======================================================

    if (

        f1 > best_f1 + EPSILON

        or

        (

            abs(f1 - best_f1) <= EPSILON

            and

            accuracy > best_accuracy + EPSILON

        )

    ):

        best_f1 = f1

        best_accuracy = accuracy

        best_model = model

        best_model_name = name

# ==========================================================
# SAVE BEST MODEL
# ==========================================================

os.makedirs(

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\Machine Learning\models",

    exist_ok=True

)

joblib.dump(

    best_model,

    rf"C:\Users\Ishan  Singh\Desktop\VentureDecision\Machine Learning\models\{MODEL_NAME}"

)

# ==========================================================
# GENERATE PREDICTIONS FOR ENTIRE DATASET
# ==========================================================

df["Success_Probability"] = (

    best_model.predict_proba(X)[:, 1]

).round(3)


# ==========================================================
# SAVE UPDATED CSV
# ==========================================================

df.to_csv(

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv",

    index=False

)


print("Success Probability Predictions Saved to CSV")

print(

    df[[

        "Startup_ID",

        "Startup_Name",

        "Success_Probability"

    ]].head()

)


# ==========================================================
# FINAL RESULT
# ==========================================================

# ==========================================================
# FINAL RESULT
# ==========================================================

print("=" * 60)

print("Best Model Selected")

print(f"Model Name : {best_model_name}")

print(f"F1 Score   : {best_f1:.3f}")

print(f"Accuracy   : {best_accuracy:.3f}")

print()

print("Model Saved Successfully!")

print(

    rf"C:\Users\Ishan  Singh\Desktop\VentureDecision\Machine Learning\models\{MODEL_NAME}"

)

print("=" * 60)