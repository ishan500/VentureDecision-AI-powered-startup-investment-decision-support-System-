# ==========================================================
# VentureDecision
# COMPLETE STARTUP PROFILE API
# ==========================================================


from fastapi import (

    APIRouter,

    HTTPException

)


import pandas as pd

import numpy as np


from api.services.data_service import (

    load_startup_data

)


# ==========================================================
# ROUTER
# ==========================================================

router = APIRouter(

    prefix="/profile",

    tags=["Complete Startup Profile"]

)


# ==========================================================
# CONVERT VALUES TO JSON-SAFE VALUES
# ==========================================================

def convert_to_json_safe(

    value

):


    # ------------------------------------------------------
    # MISSING VALUE
    # ------------------------------------------------------

    if pd.isna(value):

        return None


    # ------------------------------------------------------
    # NUMPY INTEGER
    # ------------------------------------------------------

    if isinstance(

        value,

        np.integer

    ):

        return int(value)


    # ------------------------------------------------------
    # NUMPY FLOAT
    # ------------------------------------------------------

    if isinstance(

        value,

        np.floating

    ):

        return float(value)


    # ------------------------------------------------------
    # NUMPY BOOLEAN
    # ------------------------------------------------------

    if isinstance(

        value,

        np.bool_

    ):

        return bool(value)


    # ------------------------------------------------------
    # NORMAL PYTHON VALUE
    # ------------------------------------------------------

    return value


# ==========================================================
# CREATE COMPLETE PROFILE RESPONSE
# ==========================================================

def create_complete_profile_response(

    df,

    startup_name

):


    # ======================================================
    # FIND STARTUP
    # ======================================================

    result = df[

        df["Startup_Name"]

        .astype(str)

        .str.strip()

        .str.lower()

        == startup_name.strip().lower()

    ]


    # ======================================================
    # STARTUP NOT FOUND
    # ======================================================

    if result.empty:

        raise HTTPException(

            status_code=404,

            detail=(

                f"Startup "

                f"'{startup_name}' "

                "not found"

            )

        )


    # ======================================================
    # GET STARTUP ROW
    # ======================================================

    startup = result.iloc[0]


    # ======================================================
    # CREATE COMPLETE STARTUP DATA
    # ======================================================

    startup_data = {}


    for column in df.columns:


        startup_data[column] = (

            convert_to_json_safe(

                startup[column]

            )

        )


    # ======================================================
    # IDENTIFY ML PREDICTIONS
    # ======================================================

    prediction_columns = []


    for column in df.columns:


        if (

            "Prediction" in column

            or

            "Probability" in column

            or

            "Confidence" in column

        ):

            prediction_columns.append(

                column

            )


    # ======================================================
    # CREATE ML PREDICTIONS DICTIONARY
    # ======================================================

    ml_predictions = {}


    for column in prediction_columns:


        ml_predictions[column] = (

            convert_to_json_safe(

                startup[column]

            )

        )


    # ======================================================
    # STARTUP INTELLIGENCE COLUMNS
    # ======================================================

    intelligence_columns = [

        "Valuation_Growth_Prediction",

        "Follow_On_Funding_Probability",

        "Market_Leadership_Probability",

        "Competitive_Survival_Probability"

    ]


    # ======================================================
    # CREATE INTELLIGENCE DICTIONARY
    # ======================================================

    startup_intelligence = {}


    for column in intelligence_columns:


        if column in df.columns:


            startup_intelligence[column] = (

                convert_to_json_safe(

                    startup[column]

                )

            )


    # ======================================================
    # RETURN COMPLETE PROFILE
    # ======================================================

    return {

        "dataset": "processed",

        "startup_profile": startup_data,

        "ml_predictions": ml_predictions,

        "startup_intelligence": startup_intelligence,

        "prediction_count": len(

            ml_predictions

        ),

        "intelligence_count": len(

            startup_intelligence

        )

    }


# ==========================================================
# GET COMPLETE STARTUP PROFILE
# ==========================================================

@router.get(

    "/{startup_name}"

)


def get_startup_profile(

    startup_name: str

):


    # ======================================================
    # LOAD CSV DATA
    # ======================================================

    df = load_startup_data()


    # ======================================================
    # RETURN COMPLETE PROFILE
    # ======================================================

    return create_complete_profile_response(

        df=df,

        startup_name=startup_name

    )