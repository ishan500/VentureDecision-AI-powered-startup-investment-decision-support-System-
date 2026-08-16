# ==========================================================
# INTELLIGENCE SERVICE
# VentureDecision
# ==========================================================


from typing import (

    Optional,

    Dict,

    Any

)


from api.services.data_service import (

    get_startup_by_name

)


# ==========================================================
# GENERATE STARTUP INTELLIGENCE
# ==========================================================


def generate_startup_intelligence(

    startup_name: str,

    dataset_type: str

) -> Optional[Dict[str, Any]]:

    """
    Generates startup intelligence
    from the selected dataset.

    Supported dataset types:

    - old
    - new
    """


    # ======================================================
    # LOAD STARTUP DATA
    # ======================================================


    startup_data = get_startup_by_name(

        startup_name,

        dataset_type

    )


    # ======================================================
    # STARTUP NOT FOUND
    # ======================================================


    if startup_data is None:

        return None


    # ======================================================
    # RETURN INTELLIGENCE
    # ======================================================


    return {

        "dataset_type": dataset_type,

        "startup_name": startup_data.get(

            "Startup_Name"

        ),

        "startup_id": startup_data.get(

            "Startup_ID"

        ),

        "intelligence": startup_data

    }