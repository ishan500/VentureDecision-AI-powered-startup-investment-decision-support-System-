# ==========================================================
# VC COPILOT SERVICE
# VentureIQ
# ==========================================================


from typing import (

    Dict,

    Any

)


from api.services.ai_context_service import (

    build_ai_context

)


from api.services.ollama_service import (

    generate_vc_copilot_response

)


# ==========================================================
# SAFE VALUE HELPER
# ==========================================================


def get_value(

    startup: Dict[str, Any],

    *possible_columns: str

) -> Any:


    """

    Returns the first available value from the provided
    possible column names.

    This allows VC Copilot to support both:

    OLD DATASET
    and

    NEW DATASET

    even when column names differ.

    """


    for column in possible_columns:


        if column in startup:


            value = startup.get(

                column

            )


            if value is not None and str(

                value

            ).strip().lower() not in (

                "",

                "nan",

                "none"

            ):


                return value


    return "Not available in the provided startup data."


# ==========================================================
# BUILD VC INVESTOR CONTEXT
# ==========================================================


def build_vc_investor_context(

    startup: Dict[str, Any],

    dataset_type: str

) -> Dict[str, Any]:


    """

    Builds a structured investor-focused context.

    The context supports both:

    OLD DATASET:
    feature_engineered_startups.csv

    NEW DATASET:
    new_feature_engineered_startups.csv

    """


    dataset_type = (

        dataset_type

        .strip()

        .lower()

    )


    if dataset_type not in (

        "old",

        "new"

    ):


        raise ValueError(

            "dataset_type must be "

            "'old' or 'new'"

        )


    # ======================================================
    # STARTUP PROFILE
    # ======================================================


    startup_profile = {


        "Startup Name": get_value(

            startup,

            "Startup_Name"

        ),


        "Sector": get_value(

            startup,

            "sector"

        ),


        "Founded Year": get_value(

            startup,

            "founded_year"

        ),


        "Headquarters": get_value(

            startup,

            "headquarters"

        ),


        "Founder Count": get_value(

            startup,

            "founder_count"

        ),


        "Funding Stage": get_value(

            startup,

            "funding_stage"

        ),


        "Current Status": get_value(

            startup,

            "current_status"

        ),


        "Startup Age": get_value(

            startup,

            "Startup_Age"

        ),


        "Startup Maturity Score": get_value(

            startup,

            "Startup_Maturity_Score"

        )

    }


    # ======================================================
    # FINANCIAL PROFILE
    # ======================================================


    financial_profile = {


        "Total Funding Raised": get_value(

            startup,

            "Total_Funding_Raised"

        ),


        "Latest Funding Amount": get_value(

            startup,

            "Latest_Funding_Amount"

        ),


        "Latest Funding Round": get_value(

            startup,

            "Latest_Funding_Round"

        ),


        "Latest Funding Date": get_value(

            startup,

            "Latest_Funding_Date"

        ),


        "Number of Funding Rounds": get_value(

            startup,

            "Number_of_Funding_Rounds"

        ),


        "Valuation": get_value(

            startup,

            "Valuation"

        ),


        "Revenue": get_value(

            startup,

            "Revenue"

        ),


        "Profit or Loss": get_value(

            startup,

            "Profit_or_Loss"

        ),


        "Gross Margin": get_value(

            startup,

            "Gross_Margin"

        ),


        "Financial Health Score": get_value(

            startup,

            "Financial_Health_Score"

        ),


        "Burn Risk Score": get_value(

            startup,

            "Burn_Risk_Score"

        ),


        "Burn Risk Label": get_value(

            startup,

            "Burn_Risk_Label",

            "Burn_Risk_Name"

        ),


        "Burn Risk Prediction": get_value(

            startup,

            "Burn_Risk_Prediction",

            "Predicted_Risk"

        ),


        "Burn Risk Confidence": get_value(

            startup,

            "Burn_Risk_Confidence"

        )

    }


    # ======================================================
    # GROWTH PROFILE
    # ======================================================


    growth_profile = {


        "Employee Count": get_value(

            startup,

            "Employee_Count"

        ),


        "Monthly Visits": get_value(

            startup,

            "Monthly_Visits"

        ),


        "Google Trends Score": get_value(

            startup,

            "Google_Trends_Score"

        ),


        "App Downloads": get_value(

            startup,

            "App_Downloads"

        ),


        "App Rating": get_value(

            startup,

            "App_Rating"

        ),


        "App Reviews Count": get_value(

            startup,

            "App_Reviews_Count"

        ),


        "Growth Score": get_value(

            startup,

            "Growth_Score"

        ),


        "TAM": get_value(

            startup,

            "TAM"

        ),


        "TAM Growth Rate": get_value(

            startup,

            "TAM_Growth_Rate"

        ),


        "Market Size Category": get_value(

            startup,

            "Market_Size_Category"

        ),


        "Growth Prediction": get_value(

            startup,

            "Growth_Prediction",

            "Predicted_Growth_Potential"

        ),


        "Growth Probability": get_value(

            startup,

            "Growth_Probability",

            "Growth_Potential_Probability"

        )

    }


    # ======================================================
    # RISK PROFILE
    # ======================================================


    risk_profile = {


        "Risk Score": get_value(

            startup,

            "Risk_Score"

        ),


        "Risk Label": get_value(

            startup,

            "Risk_Label"

        ),


        "Risk Prediction": get_value(

            startup,

            "Risk_Prediction",

            "Predicted_Risk"

        ),


        "Risk Probability": get_value(

            startup,

            "Risk_Probability"

        ),


        "Predicted Risk Name": get_value(

            startup,

            "Predicted_Risk_Name"

        ),


        "Burn Risk Score": get_value(

            startup,

            "Burn_Risk_Score"

        ),


        "Burn Risk Label": get_value(

            startup,

            "Burn_Risk_Label",

            "Burn_Risk_Name"

        )

    }


    # ======================================================
    # INVESTMENT PROFILE
    # ======================================================


    investment_profile = {


        "Overall Startup Score": get_value(

            startup,

            "Overall_Startup_Score"

        ),


        "Investment Score": get_value(

            startup,

            "Investment_Score"

        ),


        "Investment Recommendation": get_value(

            startup,

            "Investment_Recommendation_Name",

            "Investment_Recommendation_Label",

            "Investment_Recommendation_Prediction",

            "Predicted_Investment_Recommendation_Name"

        ),


        "Investment Recommendation Probability": get_value(

            startup,

            "Investment_Recommendation_Probability",

            "Investment_Recommendation_Confidence"

        ),


        "Investment Timing Signal": get_value(

            startup,

            "Investment_Timing_Signal"

        ),


        "Investor Confidence Score": get_value(

            startup,

            "Investor_Confidence_Score"

        )

    }


    # ======================================================
    # FUNDING READINESS
    # ======================================================


    funding_profile = {


        "Funding Readiness Score": get_value(

            startup,

            "Funding_Readiness_Score"

        ),


        "Funding Readiness": get_value(

            startup,

            "Funding_Readiness_Name",

            "Funding_Readiness_Label",

            "Predicted_Funding_Readiness_Name"

        ),


        "Funding Readiness Prediction": get_value(

            startup,

            "Funding_Readiness_Prediction",

            "Predicted_Funding_Readiness"

        ),


        "Funding Readiness Probability": get_value(

            startup,

            "Funding_Readiness_Probability",

            "Funding_Readiness_Confidence"

        ),


        "Funding Requirement": get_value(

            startup,

            "Funding_Requirement_Prediction",

            "Predicted_Funding_Requirement_Name"

        ),


        "Funding Stage Prediction": get_value(

            startup,

            "Funding_Stage_Prediction",

            "Predicted_Funding_Stage_Name"

        )

    }


    # ======================================================
    # COMPETITIVE PROFILE
    # ======================================================


    competitive_profile = {


        "Competitive Strength Score": get_value(

            startup,

            "Competitive_Strength_Score"

        ),


        "Competitive Survival Probability": get_value(

            startup,

            "Competitive_Survival_Probability"

        ),


        "Market Leadership Probability": get_value(

            startup,

            "Market_Leadership_Probability"

        ),


        "Portfolio Fit": get_value(

            startup,

            "Portfolio_Fit_Name",

            "Portfolio_Fit_Label",

            "Portfolio_Fit_Prediction"

        ),


        "Portfolio Fit Probability": get_value(

            startup,

            "Portfolio_Fit_Probability",

            "Portfolio_Fit_Confidence"

        )

    }


    # ======================================================
    # EXIT PROFILE
    # ======================================================


    exit_profile = {


        "Historical Exit Type": get_value(

            startup,

            "Historical_Exit_Type"

        ),


        "Exit Status": get_value(

            startup,

            "Exit_Status"

        ),


        "Exit Valuation": get_value(

            startup,

            "Exit_Valuation_USD_Million"

        ),


        "Acquirer Name": get_value(

            startup,

            "Acquirer_Name"

        ),


        "Predicted Acquisition": get_value(

            startup,

            "Acquisition_Prediction",

            "Predicted_Acquisition"

        ),


        "Acquisition Probability": get_value(

            startup,

            "Acquisition_Probability"

        ),


        "Predicted Exit": get_value(

            startup,

            "Exit_Prediction",

            "Predicted_Exit"

        ),


        "Exit Probability": get_value(

            startup,

            "Exit_Probability"

        )

    }


    # ======================================================
    # RETURN STRUCTURED CONTEXT
    # ======================================================


    return {


        "dataset_type": dataset_type,


        "startup_profile": startup_profile,


        "financial_profile": financial_profile,


        "growth_profile": growth_profile,


        "risk_profile": risk_profile,


        "investment_profile": investment_profile,


        "funding_profile": funding_profile,


        "competitive_profile": competitive_profile,


        "exit_profile": exit_profile

    }


# ==========================================================
# GENERATE VC COPILOT ANSWER
# ==========================================================


def generate_vc_copilot_answer(

    startup: Dict[str, Any],

    question: str,

    dataset_type: str = "new"

) -> Dict[str, Any]:


    """

    Generates an investor-oriented answer using Ollama.

    """


    # ------------------------------------------------------
    # BUILD STRUCTURED INVESTOR CONTEXT
    # ------------------------------------------------------


    investor_context = build_vc_investor_context(

        startup=startup,

        dataset_type=dataset_type

    )


    # ------------------------------------------------------
    # BUILD AI CONTEXT
    # ------------------------------------------------------


    ai_context = build_ai_context(

        startup=investor_context,

        feature="vc_copilot",

        question=question,

        scenario=None,

        dataset_type=dataset_type

    )


    # ------------------------------------------------------
    # SEND TO OLLAMA
    # ------------------------------------------------------


    ai_response = generate_vc_copilot_response(

        startup_name=startup.get(

            "Startup_Name",

            "Unknown Startup"

        ),

        question=question,

        investor_context=ai_context,

        dataset_type=dataset_type

    )


    # ------------------------------------------------------
    # RETURN RESULT
    # ------------------------------------------------------


    return {


        "status": "success",


        "startup_name": startup.get(

            "Startup_Name"

        ),


        "dataset_type": dataset_type,


        "question": question,


        "answer": ai_response

    }