import pandas as pd
import joblib

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier

from sklearn.metrics import (

    accuracy_score,

    precision_score,

    recall_score,

    f1_score,

    confusion_matrix

)


# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv(

    r"C:\Users\Ishan  Singh\Desktop\VentureDecision\data\processed\feature_engineered_startups.csv"

)

TARGET_COLUMN = "Investment_Recommendation_Label"

MODEL_NAME = "investment_recommendation.pkl"

# ==========================================================
# FEATURES
# ==========================================================

DROP_COLUMNS = [

    "Startup_ID",

    "Startup_Name",

    TARGET_COLUMN,

    "Investment_Recommendation_Name",

    "Investment_Score"

]

X = df.drop(

    columns=DROP_COLUMNS,

    errors="ignore"

)

X = pd.get_dummies(

    X,

    drop_first=True

)

# ==========================================================
# HANDLE MISSING VALUES
# ==========================================================

X = X.fillna(

    X.median(numeric_only=True)

)

X = X.fillna(0)

y = df[TARGET_COLUMN]

print("=" * 60)

print("Investment Recommendation Distribution")

print(

    df[TARGET_COLUMN].value_counts().sort_index()

)

print()

print("Investment Recommendation Distribution (%)")

print(

    (df[TARGET_COLUMN].value_counts(normalize=True).sort_index() * 100).round(2)

)

print("=" * 60)

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

        max_iter=5000,

        random_state=42

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

        objective="multi:softprob",

        num_class=4,

        eval_metric="mlogloss"

    )

}

# ==========================================================
# MODEL PRIORITY
# ==========================================================

model_priority = {

    "Logistic Regression": 1,

    "Random Forest": 2,

    "XGBoost": 3

}

# ==========================================================
# BEST MODEL VARIABLES
# PRIMARY = WEIGHTED PRECISION
# SECONDARY = WEIGHTED F1
# ==========================================================

best_model = None

best_model_name = ""

best_precision = 0

best_f1 = 0

EPSILON = 1e-6

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

        average="weighted",

        zero_division=0

    )

    recall = recall_score(

        y_test,

        prediction,

        average="weighted",

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

    print(f"Accuracy            : {accuracy:.3f}")

    print(f"Weighted Precision  : {precision:.3f}")

    print(f"Weighted Recall     : {recall:.3f}")

    print(f"Weighted F1 Score   : {f1:.3f}")

    print()

    print("Confusion Matrix")

    print(cm)

    print()

    # ======================================================
    # MODEL SELECTION
    # PRIMARY = WEIGHTED PRECISION
    # SECONDARY = WEIGHTED F1
    # ======================================================

    if (

        precision > best_precision + EPSILON

        or

        (

            abs(precision - best_precision) <= EPSILON

            and

            f1 > best_f1 + EPSILON

        )

        or

        (

            abs(precision - best_precision) <= EPSILON

            and

            abs(f1 - best_f1) <= EPSILON

            and

            model_priority[name] < model_priority.get(best_model_name, 999)

        )

    ):

        best_precision = precision

        best_f1 = f1

        best_model = model

        best_model_name = name


# ==========================================================
# BEST MODEL
# ==========================================================

print("=" * 60)

print("Best Model Selected")

print(best_model_name)

print(f"Weighted Precision : {best_precision:.3f}")

print(f"Weighted F1 Score  : {best_f1:.3f}")

print()

joblib.dump(

    best_model,

    rf"C:\Users\Ishan  Singh\Desktop\VentureDecision\Machine Learning\models\{MODEL_NAME}"

)

print("Model Saved Successfully")

