# ==========================================================
# DATA SERVICE
# VentureIQ
# ==========================================================


import os


from typing import (

    Optional,

    Dict,

    Any,

    List

)


import pandas as pd


import numpy as np


# ==========================================================
# PROJECT PATH
# ==========================================================


BASE_DIR = os.path.dirname(

    os.path.dirname(

        os.path.dirname(

            os.path.abspath(__file__)

        )

    )

)


# ==========================================================
# DATA DIRECTORY
# ==========================================================


DATA_DIR = os.path.join(

    BASE_DIR,

    "data",

    "processed"

)


# ==========================================================
# DATASET FILES
# ==========================================================


OLD_STARTUPS_FILE = os.path.join(

    DATA_DIR,

    "feature_engineered_startups.csv"

)


NEW_STARTUPS_FILE = os.path.join(

    DATA_DIR,

    "new_feature_engineered_startups.csv"

)


# ==========================================================
# VALID DATASET TYPES
# ==========================================================


VALID_DATASET_TYPES = {

    "old",

    "new"

}


# ==========================================================
# LOAD OLD STARTUPS
# ==========================================================


def load_old_startups() -> pd.DataFrame:


    if not os.path.exists(

        OLD_STARTUPS_FILE

    ):


        raise FileNotFoundError(

            f"Old startup dataset not found: "

            f"{OLD_STARTUPS_FILE}"

        )


    return pd.read_csv(

        OLD_STARTUPS_FILE

    )


# ==========================================================
# LOAD NEW STARTUPS
# ==========================================================


def load_new_startups() -> pd.DataFrame:


    if not os.path.exists(

        NEW_STARTUPS_FILE

    ):


        raise FileNotFoundError(

            f"New startup dataset not found: "

            f"{NEW_STARTUPS_FILE}"

        )


    return pd.read_csv(

        NEW_STARTUPS_FILE

    )


# ==========================================================
# LOAD DATASET BY TYPE
# ==========================================================


def load_startup_data(

    dataset_type: str

) -> pd.DataFrame:


    dataset_type = (

        dataset_type

        .strip()

        .lower()

    )


    if dataset_type == "old":


        return load_old_startups()


    if dataset_type == "new":


        return load_new_startups()


    raise ValueError(

        "dataset_type must be "

        "'old' or 'new'"

    )


# ==========================================================
# GET STARTUP BY NAME
# ==========================================================


def get_startup_by_name(

    startup_name: str,

    dataset_type: str

) -> Optional[Dict[str, Any]]:


    df = load_startup_data(

        dataset_type

    )


    # ------------------------------------------------------
    # VALIDATE REQUIRED COLUMN
    # ------------------------------------------------------


    if "Startup_Name" not in df.columns:


        raise KeyError(

            "Required column 'Startup_Name' "

            "not found in startup dataset"

        )


    # ------------------------------------------------------
    # SEARCH STARTUP
    # ------------------------------------------------------


    result = df[

        df["Startup_Name"]

        .astype(str)

        .str.strip()

        .str.lower()

        == startup_name.strip().lower()

    ]


    if result.empty:


        return None


    return dataframe_to_records(

        result

    )[0]


# ==========================================================
# CONVERT VALUE TO JSON-SAFE VALUE
# ==========================================================


def convert_to_json_safe(

    value: Any

) -> Any:


    # ------------------------------------------------------
    # HANDLE NONE
    # ------------------------------------------------------


    if value is None:


        return None


    # ------------------------------------------------------
    # HANDLE PANDAS / NUMPY NA VALUES
    # ------------------------------------------------------


    try:


        if pd.isna(

            value

        ):


            return None


    except (

        TypeError,

        ValueError

    ):


        pass


    # ------------------------------------------------------
    # NUMPY INTEGER
    # ------------------------------------------------------


    if isinstance(

        value,

        np.integer

    ):


        return int(

            value

        )


    # ------------------------------------------------------
    # NUMPY FLOAT
    # ------------------------------------------------------


    if isinstance(

        value,

        np.floating

    ):


        return float(

            value

        )


    # ------------------------------------------------------
    # NUMPY BOOLEAN
    # ------------------------------------------------------


    if isinstance(

        value,

        np.bool_

    ):


        return bool(

            value

        )


    return value


# ==========================================================
# DATAFRAME TO RECORDS
# ==========================================================


def dataframe_to_records(

    df: pd.DataFrame

) -> List[Dict[str, Any]]:


    records = []


    for record in df.to_dict(

        orient="records"

    ):


        clean_record = {}


        for key, value in record.items():


            clean_record[key] = (

                convert_to_json_safe(

                    value

                )

            )


        records.append(

            clean_record

        )


    return records