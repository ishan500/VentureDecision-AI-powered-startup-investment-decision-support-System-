# ==========================================================
# DUE DILIGENCE ROUTE
# VentureDecision
# ==========================================================


from fastapi import (

    APIRouter,

    HTTPException

)


from api.services.due_dilligence_service import (

    generate_due_diligence_report

)


router = APIRouter(

    prefix="/due-diligence",

    tags=[

        "Due Diligence"

    ]

)


# ==========================================================
# OLD DATASET
# ==========================================================


@router.get(

    "/old/{startup_name}"

)


def get_old_due_diligence(

    startup_name: str

):


    result = generate_due_diligence_report(

        startup_name,

        "old"

    )


    if result.get(

        "status"

    ) == "error":


        raise HTTPException(

            status_code=404,

            detail=result.get(

                "message"

            )

        )


    return result


# ==========================================================
# NEW DATASET
# ==========================================================


@router.get(

    "/new/{startup_name}"

)


def get_new_due_diligence(

    startup_name: str

):


    result = generate_due_diligence_report(

        startup_name,

        "new"

    )


    if result.get(

        "status"

    ) == "error":


        raise HTTPException(

            status_code=404,

            detail=result.get(

                "message"

            )

        )


    return result