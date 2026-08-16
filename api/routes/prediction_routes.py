# ==========================================================
# VentureDecision
# ML PREDICTION API ROUTES
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

    prefix="/predictions",

    tags=["ML Predictions"]

)


# ==========================================================
# GET MODEL PREDICTION COLUMNS
# ==========================================================

def get_prediction_columns(

    df

):


    prediction_columns = []


    for column in df.columns:


        # --------------------------------------------------
        # MODEL OUTPUT COLUMNS
        # --------------------------------------------------

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


    return prediction_columns


# ==========================================================
# CONVERT VALUE TO JSON-SAFE VALUE
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
# CREATE PREDICTION RESPONSE
# ==========================================================

def create_prediction_response(

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
    # GET SINGLE STARTUP ROW
    # ======================================================

    startup = result.iloc[0]


    # ======================================================
    # GET PREDICTION COLUMNS
    # ======================================================

    prediction_columns = (

        get_prediction_columns(df)

    )


    # ======================================================
    # CREATE PREDICTIONS DICTIONARY
    # ======================================================

    predictions = {}


    for column in prediction_columns:


        predictions[column] = (

            convert_to_json_safe(

                startup[column]

            )

        )


    # ======================================================
    # RETURN JSON-SAFE RESPONSE
    # ======================================================

    return {

        "dataset": "processed",

        "startup_name": str(

            startup["Startup_Name"]

        ),

        "prediction_count": len(

            predictions

        ),

        "predictions": predictions

    }


# ==========================================================
# GET STARTUP PREDICTIONS
# ==========================================================

@router.get(

    "/{startup_name}"

)


def get_startup_predictions(

    startup_name: str

):


    # ======================================================
    # LOAD BOTH CSV DATASETS
    # ======================================================

    df = load_startup_data()


    # ======================================================
    # RETURN PREDICTIONS
    # ======================================================

    return create_prediction_response(

        df=df,

        startup_name=startup_name

    )