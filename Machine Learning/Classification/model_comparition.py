import pandas as pd

# ==========================================================
# EXIT PROBABILITY (Binary Classification)
# ==========================================================

exit_probability = pd.DataFrame({

    "Model": [
        "Logistic Regression",
        "Random Forest",
        "XGBoost"
    ],

    "Accuracy": [
        0.800,
        0.850,
        0.950
    ],

    "Precision": [
        0.600,
        1.000,
        1.000
    ],

    "Recall": [
        0.600,
        0.400,
        0.800
    ],

    "F1 Score": [
        0.600,
        0.571,
        0.889
    ]

})

print("="*95)
print("               EXIT PROBABILITY (Binary Classification)")
print("="*95)

print(exit_probability.to_string(index=False))

print("\nPrimary Metric   : Recall")
print("Secondary Metric : F1 Score")
print("Best Model       : XGBoost")

print("\n")
print("-"*95)
print("\n")

# ==========================================================
# INVESTMENT RECOMMENDATION (Multiclass Classification)
# ==========================================================

investment = pd.DataFrame({

    "Model": [
        "Logistic Regression",
        "Random Forest",
        "XGBoost"
    ],

    "Accuracy": [
        0.650,
        0.850,
        0.850
    ],

    "Weighted Precision": [
        0.667,
        0.867,
        0.867
    ],

    "Weighted Recall": [
        0.650,
        0.850,
        0.850
    ],

    "Weighted F1": [
        0.654,
        0.842,
        0.842
    ]

})

print("="*95)
print("      INVESTMENT RECOMMENDATION (Multiclass Classification)")
print("="*95)

print(investment.to_string(index=False))

print("\nPrimary Metric   : Weighted Precision")
print("Secondary Metric : Weighted F1 Score")
print("Best Model       : Random Forest")