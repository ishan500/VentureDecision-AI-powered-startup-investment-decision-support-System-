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

TARGET_COLUMN = "IPO_Label"

MODEL_NAME = "ipo_probability.pkl"

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
# BEST MODEL VARIABLES
# ==========================================================

best_model = None

best_model_name = ""

best_precision = 0

best_f1 = 0

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

        zero_division=0

    )

    cm = confusion_matrix(

        y_test,

        prediction

    )

    print("="*60)

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
    # PRIMARY = PRECISION
    # SECONDARY = F1
    # ======================================================

    if (

        precision > best_precision

        or

        (

            precision == best_precision

            and

            f1 > best_f1

        )

    ):

        best_precision = precision

        best_f1 = f1

        best_model = model

        best_model_name = name


print("="*60)

print("Best Model")

print(best_model_name)

print()

print(f"Precision : {best_precision:.3f}")

print(f"F1 Score  : {best_f1:.3f}")

print()

print("Best Model Saved Successfully!")

print(

    rf"C:\Users\Ishan  Singh\Desktop\VentureDecision\Machine Learning\models\{MODEL_NAME}"

)

