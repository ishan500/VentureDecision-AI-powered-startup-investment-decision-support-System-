# ==========================================================
# VC COPILOT ROUTES
# VentureIQ
# ==========================================================


from fastapi import (

    APIRouter,

    HTTPException

)


from pydantic import BaseModel


from api.services.data_service import (

    get_startup_by_name

)


from api.services.ollama_service import (

    generate_vc_copilot_response

)


# ==========================================================
# ROUTER
# ==========================================================


router = APIRouter(

    prefix="/vc-copilot",

    tags=["VC Copilot"]

)


# ==========================================================
# REQUEST MODEL
# ==========================================================


class VCCopilotRequest(BaseModel):


    startup_name: str


    question: str


    dataset_type: str = "new"


# ==========================================================
# VC COPILOT
# ==========================================================


@router.post(

    "/ask"

)


def ask_vc_copilot(

    request: VCCopilotRequest

):


    try:


        # ==================================================
        # VALIDATE DATASET TYPE
        # ==================================================


        dataset_type = (

            request.dataset_type

            .strip()

            .lower()

        )


        if dataset_type not in [

            "old",

            "new"

        ]:


            raise HTTPException(

                status_code=400,

                detail=(

                    "dataset_type must be "

                    "'old' or 'new'"

                )

            )


        # ==================================================
        # LOAD STARTUP FROM SELECTED CSV
        # ==================================================


        startup = get_startup_by_name(

            startup_name=request.startup_name,

            dataset_type=dataset_type

        )


        # ==================================================
        # VALIDATE STARTUP
        # ==================================================


        if not startup:


            raise HTTPException(

                status_code=404,

                detail=(

                    f"Startup "

                    f"'{request.startup_name}' "

                    f"not found in "

                    f"{dataset_type} dataset"

                )

            )


        # ==================================================
        # BUILD INVESTOR CONTEXT
        # ==================================================


        investor_context = {


            "startup_profile": {


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


                "founder_count": startup.get(

                    "founder_count"

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

            },


            "financial_metrics": {


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

            },


            "growth_metrics": {


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


                "Growth_Label": startup.get(

                    "Growth_Label"

                ),


                "Predicted_Growth_Potential": startup.get(

                    "Predicted_Growth_Potential"

                ),


                "Growth_Potential_Probability": startup.get(

                    "Growth_Potential_Probability"

                ),


                "Market_Leadership_Probability": startup.get(

                    "Market_Leadership_Probability"

                )

            },


            "market_metrics": {


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

            },


            "risk_metrics": {


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


                "Burn_Risk_Prediction": startup.get(

                    "Burn_Risk_Prediction"

                )

            },


            "investment_metrics": {


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

            },


            "exit_metrics": {


                "Historical_Exit_Type": startup.get(

                    "Historical_Exit_Type"

                ),


                "Exit_Status": startup.get(

                    "Exit_Status"

                ),


                "Historical_Exit_Type": startup.get(

                    "Historical_Exit_Type"

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

            },


            "investor_confidence": {


                "Investor_Confidence_Score": startup.get(

                    "Investor_Confidence_Score"

                ),


                "Portfolio_Fit_Score": startup.get(

                    "Portfolio_Fit_Score"

                ),


                "Portfolio_Fit_Label": startup.get(

                    "Portfolio_Fit_Label"

                ),


                "Portfolio_Fit_Name": startup.get(

                    "Portfolio_Fit_Name"

                )

            }


        }


        # ==================================================
        # GENERATE VC COPILOT ANSWER
        # ==================================================


        answer = generate_vc_copilot_response(

            startup_name=request.startup_name,

            question=request.question,

            investor_context=investor_context,

            dataset_type=dataset_type

        )


        # ==================================================
        # RETURN RESPONSE
        # ==================================================


        return {


            "status": "success",


            "startup_name": request.startup_name,


            "dataset_type": dataset_type,


            "question": request.question,


            "answer": answer


        }


    except HTTPException:


        raise


    except Exception as error:


        raise HTTPException(

            status_code=500,

            detail=str(error)

        )