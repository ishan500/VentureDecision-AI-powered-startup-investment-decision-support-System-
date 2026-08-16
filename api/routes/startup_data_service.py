# ==========================================================
# STARTUP DATA SERVICE
# VentureDecision
# ==========================================================

from typing import Optional, Dict, Any

from pathlib import Path

import pandas as pd


# ==========================================================
# PROJECT PATH
# ==========================================================

# Current file:
#
# VentureDecision/
# ├── api/
# │   └── services/
# │       └── startup_data_service.py
#
# Data:
#
# VentureDecision/
# └── data/
#     └── processed/
#         ├── feature_engineered_startups.csv
#         └── new_feature_engineered_startups.csv


PROJECT_ROOT = Path(__file__).resolve().parents[2]


PROCESSED_DATA_DIR = (

    PROJECT_ROOT

    / "data"

    / "processed"

)


OLD_DATA_PATH = (

    PROCESSED_DATA_DIR

    / "feature_engineered_startups.csv"

)


NEW_DATA_PATH = (

    PROCESSED_DATA_DIR

    / "new_feature_engineered_startups.csv"

)


# ==========================================================
# CSV CACHE
# ==========================================================

_old_startups_cache: Optional[pd.DataFrame] = None

_new_startups_cache: Optional[pd.DataFrame] = None


# ==========================================================
# NORMALIZE COLUMN NAMES
# ==========================================================

def normalize_column_name(

    column_name: Any

) -> str:

    return (

        str(column_name)

        .strip()

        .lower()

        .replace(" ", "_")

        .replace("-", "_")

    )


# ==========================================================
# LOAD OLD DATASET
# ==========================================================

def load_old_startups() -> pd.DataFrame:

    global _old_startups_cache


    if _old_startups_cache is not None:

        return _old_startups_cache


    if not OLD_DATA_PATH.exists():

        raise FileNotFoundError(

            f"Old startup dataset not found at: "

            f"{OLD_DATA_PATH}"

        )


    print(

        "Loading old startup dataset..."

    )


    df = pd.read_csv(

        OLD_DATA_PATH

    )


    # Create normalized helper column

    df["_normalized_startup_name"] = (

        df["Startup_Name"]

        .astype(str)

        .str.strip()

        .str.lower()

    )


    _old_startups_cache = df


    print(

        f"Old dataset loaded: {len(df)} startups"

    )


    return _old_startups_cache


# ==========================================================
# LOAD NEW DATASET
# ==========================================================

def load_new_startups() -> pd.DataFrame:

    global _new_startups_cache


    if _new_startups_cache is not None:

        return _new_startups_cache


    if not NEW_DATA_PATH.exists():

        raise FileNotFoundError(

            f"New startup dataset not found at: "

            f"{NEW_DATA_PATH}"

        )


    print(

        "Loading new startup dataset..."

    )


    df = pd.read_csv(

        NEW_DATA_PATH

    )


    # Create normalized helper column

    df["_normalized_startup_name"] = (

        df["Startup_Name"]

        .astype(str)

        .str.strip()

        .str.lower()

    )


    _new_startups_cache = df


    print(

        f"New dataset loaded: {len(df)} startups"

    )


    return _new_startups_cache


# ==========================================================
# GET STARTUP BY NAME
# ==========================================================

def get_startup_by_name(

    startup_name: str,

    dataset_type: str = "new"

) -> Optional[Dict[str, Any]]:


    # ------------------------------------------------------

    # Normalize input

    # ------------------------------------------------------

    normalized_name = (

        str(startup_name)

        .strip()

        .lower()

    )


    dataset_type = (

        str(dataset_type)

        .strip()

        .lower()

    )


    # ------------------------------------------------------

    # Select dataset

    # ------------------------------------------------------

    if dataset_type == "old":

        df = load_old_startups()


    elif dataset_type == "new":

        df = load_new_startups()


    else:

        raise ValueError(

            "dataset_type must be either 'old' or 'new'"

        )


    # ------------------------------------------------------

    # Search startup

    # ------------------------------------------------------

    result = df[

        df["_normalized_startup_name"]

        == normalized_name

    ]


    # ------------------------------------------------------

    # Startup not found

    # ------------------------------------------------------

    if result.empty:

        return None


    # ------------------------------------------------------

    # Convert to dictionary

    # ------------------------------------------------------

    startup = (

        result.iloc[0]

        .drop(

            labels=[

                "_normalized_startup_name"

            ]

        )

        .to_dict()

    )


    # ------------------------------------------------------

    # Convert NaN to None

    # ------------------------------------------------------

    cleaned_startup = {}


    for key, value in startup.items():

        if pd.isna(value):

            cleaned_startup[key] = None

        else:

            cleaned_startup[key] = value


    return cleaned_startup


# ==========================================================
# CLEAR CACHE
# ==========================================================

def clear_startup_cache():

    global _old_startups_cache

    global _new_startups_cache


    _old_startups_cache = None

    _new_startups_cache = None


    print(

        "Startup dataset cache cleared."

    )