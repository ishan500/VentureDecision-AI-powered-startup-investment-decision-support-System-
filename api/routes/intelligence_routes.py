# ==========================================================
# INTELLIGENCE ROUTES
# VentureDecision
# ==========================================================


from fastapi import (

    APIRouter,

    HTTPException

)


from api.services.data_service import (

    get_startup_by_name

)


from api.services.intelligence_service import (

    generate_startup_intelligence

)


# ==========================================================
# ROUTER
# ==========================================================


router = APIRouter(

    prefix="/intelligence",

    tags=["Intelligence"]

)


# ==========================================================
# OLD STARTUP INTELLIGENCE
# ==========================================================


@router.get(

    "/old/{startup_name}"

)


def get_old_intelligence(

    startup_name: str

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


    intelligence_result = (

        generate_startup_intelligence(

            startup_data

        )

    )


    return {


        "dataset_type": "old",


        "startup_name": startup_name,


        "intelligence": intelligence_result

    }


# ==========================================================
# NEW STARTUP INTELLIGENCE
# ==========================================================


@router.get(

    "/new/{startup_name}"

)


def get_new_intelligence(

    startup_name: str

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


    intelligence_result = (

        generate_startup_intelligence(

            startup_data

        )

    )


    return {


        "dataset_type": "new",


        "startup_name": startup_name,


        "intelligence": intelligence_result

    }