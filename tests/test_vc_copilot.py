# ==========================================================
# TEST VC COPILOT
# VentureIQ
# ==========================================================


from api.services.data_service import (

    get_startup_by_name

)


from api.services.ollama_service import (

    generate_vc_copilot_response

)


# ==========================================================
# BUILD INVESTOR CONTEXT
# ==========================================================


def build_investor_context(

    startup: dict,

    dataset_type: str

) -> dict:


    # ======================================================
    # COMMON STARTUP PROFILE
    # ======================================================


    startup_profile = {


        "Startup_Name": startup.get(

            "Startup_Name"

        ),


        "sector": startup.get(

            "sector"

        ),


        "founded_year": startup.get(

            "founded_year"

        ),


        "headquarters": startup.get(

            "headquarters"

        ),


        "funding_stage": startup.get(

            "funding_stage"

        ),


        "current_status": startup.get(

            "current_status"

        ),


        "Startup_Age": startup.get(

            "Startup_Age"

        ),


        "Startup_Maturity_Score": startup.get(

            "Startup_Maturity_Score"

        )

    }


    # ======================================================
    # COMMON FINANCIAL METRICS
    # ======================================================


    financial_metrics = {


        "Total_Funding_Raised": startup.get(

            "Total_Funding_Raised"

        ),


        "Latest_Funding_Amount": startup.get(

            "Latest_Funding_Amount"

        ),


        "Number_of_Funding_Rounds": startup.get(

            "Number_of_Funding_Rounds"

        ),


        "Valuation": startup.get(

            "Valuation"

        ),


        "Revenue": startup.get(

            "Revenue"

        ),


        "Profit_or_Loss": startup.get(

            "Profit_or_Loss"

        ),


        "Gross_Margin": startup.get(

            "Gross_Margin"

        ),


        "Financial_Health_Score": startup.get(

            "Financial_Health_Score"

        )

    }


    # ======================================================
    # COMMON GROWTH METRICS
    # ======================================================


    growth_metrics = {


        "Employee_Count": startup.get(

            "Employee_Count"

        ),


        "Monthly_Visits": startup.get(

            "Monthly_Visits"

        ),


        "Google_Trends_Score": startup.get(

            "Google_Trends_Score"

        ),


        "App_Downloads": startup.get(

            "App_Downloads"

        ),


        "Growth_Score": startup.get(

            "Growth_Score"

        ),


        "Market_Leadership_Probability": startup.get(

            "Market_Leadership_Probability"

        )

    }


    # ======================================================
    # COMMON MARKET METRICS
    # ======================================================


    market_metrics = {


        "TAM": startup.get(

            "TAM"

        ),


        "TAM_Growth_Rate": startup.get(

            "TAM_Growth_Rate"

        ),


        "Market_Size_Category": startup.get(

            "Market_Size_Category"

        ),


        "Market_Opportunity_Score": startup.get(

            "Market_Opportunity_Score"

        ),


        "Competitive_Strength_Score": startup.get(

            "Competitive_Strength_Score"

        ),


        "Competitive_Survival_Probability": startup.get(

            "Competitive_Survival_Probability"

        )

    }


    # ======================================================
    # DATASET-SPECIFIC RISK METRICS
    # ======================================================


    if dataset_type == "old":


        risk_metrics = {


            "Risk_Label": startup.get(

                "Risk_Label"

            ),


            "Predicted_Risk": startup.get(

                "Predicted_Risk"

            ),


            "Risk_Probability": startup.get(

                "Risk_Probability"

            ),


            "Burn_Risk_Score": startup.get(

                "Burn_Risk_Score"

            ),


            "Burn_Risk_Label": startup.get(

                "Burn_Risk_Label"

            ),


            "Burn_Risk_Prediction": startup.get(

                "Burn_Risk_Prediction"

            )

        }


    else:


        risk_metrics = {


            "Risk_Score": startup.get(

                "Risk_Score"

            ),


            "Risk_Prediction": startup.get(

                "Risk_Prediction"

            ),


            "Risk_Probability": startup.get(

                "Risk_Probability"

            )

        }


    # ======================================================
    # DATASET-SPECIFIC INVESTMENT METRICS
    # ======================================================


    if dataset_type == "old":


        investment_metrics = {


            "Overall_Startup_Score": startup.get(

                "Overall_Startup_Score"

            ),


            "Investment_Score": startup.get(

                "Investment_Score"

            ),


            "Investment_Recommendation_Label": startup.get(

                "Investment_Recommendation_Label"

            ),


            "Investment_Recommendation_Name": startup.get(

                "Investment_Recommendation_Name"

            ),


            "Predicted_Investment_Recommendation": startup.get(

                "Predicted_Investment_Recommendation"

            ),


            "Investment_Recommendation_Confidence": startup.get(

                "Investment_Recommendation_Confidence"

            ),


            "Funding_Readiness_Score": startup.get(

                "Funding_Readiness_Score"

            ),


            "Funding_Readiness_Label": startup.get(

                "Funding_Readiness_Label"

            ),


            "Funding_Readiness_Name": startup.get(

                "Funding_Readiness_Name"

            )

        }


    else:


        investment_metrics = {


            "Investment_Recommendation_Prediction": startup.get(

                "Investment_Recommendation_Prediction"

            ),


            "Investment_Recommendation_Probability": startup.get(

                "Investment_Recommendation_Probability"

            ),


            "Funding_Readiness_Prediction": startup.get(

                "Funding_Readiness_Prediction"

            ),


            "Funding_Readiness_Name": startup.get(

                "Funding_Readiness_Name"

            ),


            "Funding_Readiness_Probability": startup.get(

                "Funding_Readiness_Probability"

            ),


            "Portfolio_Fit_Prediction": startup.get(

                "Portfolio_Fit_Prediction"

            ),


            "Portfolio_Fit_Probability": startup.get(

                "Portfolio_Fit_Probability"

            )

        }


    # ======================================================
    # COMMON EXIT METRICS
    # ======================================================


    if dataset_type == "old":


        exit_metrics = {


            "Historical_Exit_Type": startup.get(

                "Historical_Exit_Type"

            ),


            "Exit_Status": startup.get(

                "Exit_Status"

            ),


            "Predicted_Exit": startup.get(

                "Predicted_Exit"

            ),


            "Exit_Probability": startup.get(

                "Exit_Probability"

            ),


            "Predicted_Acquisition": startup.get(

                "Predicted_Acquisition"

            ),


            "Acquisition_Probability": startup.get(

                "Acquisition_Probability"

            )

        }


    else:


        exit_metrics = {


            "Exit_Prediction": startup.get(

                "Exit_Prediction"

            ),


            "Exit_Probability": startup.get(

                "Exit_Probability"

            ),


            "Acquisition_Prediction": startup.get(

                "Acquisition_Prediction"

            ),


            "Acquisition_Probability": startup.get(

                "Acquisition_Probability"

            )

        }


    # ======================================================
    # INVESTOR CONFIDENCE METRICS
    # ======================================================


    investor_confidence = {


        "Investor_Confidence_Score": startup.get(

            "Investor_Confidence_Score"

        ),


        "Follow_On_Funding_Probability": startup.get(

            "Follow_On_Funding_Probability"

        ),


        "Market_Leadership_Probability": startup.get(

            "Market_Leadership_Probability"

        ),


        "Competitive_Survival_Probability": startup.get(

            "Competitive_Survival_Probability"

        ),


        "Valuation_Growth_Prediction": startup.get(

            "Valuation_Growth_Prediction"

        )

    }


    # ======================================================
    # RETURN COMPLETE CONTEXT
    # ======================================================


    return {


        "startup_profile": startup_profile,


        "financial_metrics": financial_metrics,


        "growth_metrics": growth_metrics,


        "market_metrics": market_metrics,


        "risk_metrics": risk_metrics,


        "investment_metrics": investment_metrics,


        "exit_metrics": exit_metrics,


        "investor_confidence": investor_confidence

    }


# ==========================================================
# GET USER INPUT
# ==========================================================


STARTUP_NAME = input(

    "\nEnter startup name: "

).strip()


# ==========================================================
# GET INVESTOR QUESTION
# ==========================================================


QUESTION = input(

    "\nEnter your investor question: "

).strip()


# ==========================================================
# SELECT DATASET
# ==========================================================


print("\n")

print("=" * 70)

print("SELECT DATASET")

print("=" * 70)

print("1. OLD DATASET")

print("2. NEW DATASET")

print("3. BOTH DATASETS")


DATASET_OPTION = input(

    "\nEnter option (1/2/3): "

).strip()


if DATASET_OPTION == "1":


    DATASET_TYPES = [

        "old"

    ]


elif DATASET_OPTION == "2":


    DATASET_TYPES = [

        "new"

    ]


elif DATASET_OPTION == "3":


    DATASET_TYPES = [

        "old",

        "new"

    ]


else:


    print(

        "\nInvalid option."

    )


    exit()


# ==========================================================
# PROCESS SELECTED DATASETS
# ==========================================================


for DATASET_TYPE in DATASET_TYPES:


    print("\n")

    print("=" * 70)

    print(

        f"PROCESSING "

        f"{DATASET_TYPE.upper()} DATASET"

    )

    print("=" * 70)


    # ======================================================
    # LOAD STARTUP
    # ======================================================


    startup = get_startup_by_name(

        startup_name=STARTUP_NAME,

        dataset_type=DATASET_TYPE

    )


    if not startup:


        print("\n")

        print(

            f"Startup '{STARTUP_NAME}' "

            f"not found in "

            f"{DATASET_TYPE} dataset."

        )


        continue


    print("\n")

    print(

        f"Startup found in "

        f"{DATASET_TYPE} dataset."

    )


    # ======================================================
    # BUILD INVESTOR CONTEXT
    # ======================================================


    investor_context = build_investor_context(

        startup=startup,

        dataset_type=DATASET_TYPE

    )


    # ======================================================
    # SEND TO OLLAMA
    # ======================================================


    print("\n")

    print(

        "Sending startup data to Ollama..."

    )


    print(

        "Please wait..."

    )


    answer = generate_vc_copilot_response(

        startup_name=STARTUP_NAME,

        question=QUESTION,

        investor_context=investor_context,

        dataset_type=DATASET_TYPE

    )


    # ======================================================
    # PRINT ANSWER
    # ======================================================


    print("\n")

    print("=" * 70)

    print(

        f"VC COPILOT ANSWER - "

        f"{DATASET_TYPE.upper()} DATASET"

    )

    print("=" * 70)

    print("\n")

    print(answer)

    print("\n")

    print("=" * 70)


print("\n")

print(

    "VC COPILOT TEST COMPLETED."

)

print("\n")