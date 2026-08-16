# ==========================================================
# SCENARIO ROUTES
# VentureDecision
# ==========================================================


from fastapi import (

    APIRouter,

    HTTPException

)


from typing import Dict, Any


from api.services.data_service import (

    get_startup_by_name

)


from api.services.scenario_engine import (

    run_scenario

)


# ==========================================================
# ROUTER
# ==========================================================


router = APIRouter(

    prefix="/scenario",

    tags=["Scenario"]

)


# ==========================================================
# OLD STARTUP SCENARIO
# ==========================================================


@router.post(

    "/old/{startup_name}"

)


def run_old_scenario(

    startup_name: str,

    scenario_changes: Dict[str, Any]

):


    startup_data = get_startup_by_name(

        startup_name,

        "old"

    )


    if startup_data is None:


        raise HTTPException(

            status_code=404,

            detail=(

                f"Old startup "

                f"'{startup_name}' "

                "not found"

            )

        )


    scenario_result = run_scenario(

        startup=startup_data,

        scenario_changes=scenario_changes

    )


    return {


        "dataset_type": "old",


        "startup_name": startup_name,


        "scenario_result": scenario_result

    }


# ==========================================================
# NEW STARTUP SCENARIO
# ==========================================================


@router.post(

    "/new/{startup_name}"

)


def run_new_scenario(

    startup_name: str,

    scenario_changes: Dict[str, Any]

):


    startup_data = get_startup_by_name(

        startup_name,

        "new"

    )


    if startup_data is None:


        raise HTTPException(

            status_code=404,

            detail=(

                f"New startup "

                f"'{startup_name}' "

                "not found"

            )

        )


    scenario_result = run_scenario(

        startup=startup_data,

        scenario_changes=scenario_changes

    )


    return {


        "dataset_type": "new",


        "startup_name": startup_name,


        "scenario_result": scenario_result

    }