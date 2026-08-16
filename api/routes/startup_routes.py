# ==========================================================
# STARTUP ROUTES
# VentureDecision
# ==========================================================


from fastapi import (

    APIRouter,

    HTTPException

)


from api.services.data_service import (

    load_old_startups,

    load_new_startups,

    dataframe_to_records

)


# ==========================================================
# ROUTER
# ==========================================================


router = APIRouter(

    prefix="/startups",

    tags=["Startups"]

)


# ==========================================================
# GET OLD STARTUP
# ==========================================================


@router.get(

    "/old/{startup_name}"

)


def get_old_startup(

    startup_name: str

):


    df = load_old_startups()


    result = df[

        df["Startup_Name"]

        .astype(str)

        .str.strip()

        .str.lower()

        == startup_name.strip().lower()

    ]


    if result.empty:


        raise HTTPException(

            status_code=404,

            detail=(

                f"Old startup "

                f"'{startup_name}' "

                "not found"

            )

        )


    return {


        "dataset_type": "old",


        "startup": dataframe_to_records(

            result

        )[0]

    }


# ==========================================================
# GET NEW STARTUP
# ==========================================================


@router.get(

    "/new/{startup_name}"

)


def get_new_startup(

    startup_name: str

):


    df = load_new_startups()


    result = df[

        df["Startup_Name"]

        .astype(str)

        .str.strip()

        .str.lower()

        == startup_name.strip().lower()

    ]


    if result.empty:


        raise HTTPException(

            status_code=404,

            detail=(

                f"New startup "

                f"'{startup_name}' "

                "not found"

            )

        )


    return {


        "dataset_type": "new",


        "startup": dataframe_to_records(

            result

        )[0]

    }