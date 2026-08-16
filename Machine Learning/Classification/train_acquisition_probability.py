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

TARGET_COLUMN = "Acquisition_Label"

MODEL_NAME = "acquisition_probability.pkl"

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
# CLASS DISTRIBUTION
# ==========================================================

class_counts = df[TARGET_COLUMN].value_counts()

print("=" * 60)
print("Class Distribution")
print(class_counts)
print("=" * 60)

negative = class_counts.iloc[0]

positive = class_counts.iloc[1]

ratio = negative / positive

if ratio >= 5:

    scale_pos_weight = ratio

    print(f"Imbalanced Dataset")
    print(f"Scale Pos Weight : {scale_pos_weight:.2f}")

else:

    scale_pos_weight = 1

    print("Balanced Dataset")
    print("Scale Pos Weight Not Required")
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

        eval_metric="logloss",

        scale_pos_weight=scale_pos_weight

    )

}

# ==========================================================
# BEST MODEL VARIABLES
# ==========================================================

best_model = None

best_model_name = ""

best_recall = 0

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
    # PRIMARY = RECALL
    # SECONDARY = F1 SCORE
    # ======================================================

    if (

        recall > best_recall

        or

        (

            recall == best_recall

            and

            f1 > best_f1

        )

    ):

        best_recall = recall

        best_f1 = f1

        best_model = model

        best_model_name = name

    


    



print("="*60)

print("Best Model Selected")

print(best_model_name)

print(f"Recall : {best_recall:.3f}")

print(f"F1 Score : {best_f1:.3f}")
print()

joblib.dump(

    best_model,

    rf"C:\Users\Ishan  Singh\Desktop\VentureDecision\Machine Learning\models\{MODEL_NAME}"

)

print("Model Saved Successfully")

# ==========================================================
# GENERATE PREDICTIONS FOR ENTIRE DATASET
# ==========================================================

# Predicted Class (0 = No Acquisition, 1 = Acquisition)

df["Predicted_Acquisition"] = best_model.predict(X)

# Prediction Confidence (%)

df["Acquisition_Probability"] = (

    best_model.predict_proba(X)[:, 1] * 100

).round(2)

# ==========================================================
# SAVE UPDATED CSV
# ==========================================================

df.to_csv(

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv",

    index=False

)

print()

print("Acquisition Predictions Saved Successfully")