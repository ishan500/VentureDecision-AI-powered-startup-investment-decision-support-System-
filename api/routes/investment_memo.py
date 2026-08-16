# ==========================================================
# INVESTMENT MEMO ROUTES
# VentureIQ
# ==========================================================

import os


from fastapi import (

    APIRouter,

    HTTPException

)


from fastapi.responses import (

    FileResponse

)


from api.routes.startup_data_service import (

    get_startup_by_name

)


from api.services.investment_memo_service import (

    generate_investment_memo

)


# ==========================================================
# ROUTER
# ==========================================================

router = APIRouter(

    prefix="/investment-memo",

    tags=["Investment Memo"]

)


# ==========================================================
# GENERATE OLD INVESTMENT MEMO
# ==========================================================

@router.get(

    "/old/{startup_name}"

)

def create_old_investment_memo(

    startup_name: str

):

    dataset_type = "old"


    try:

        # ----------------------------------------------
        # LOAD STARTUP FROM OLD CSV
        # ----------------------------------------------

        startup = get_startup_by_name(

            startup_name=startup_name,

            dataset_type=dataset_type

        )


        # ----------------------------------------------
        # VALIDATE STARTUP
        # ----------------------------------------------

        if not startup:

            raise HTTPException(

                status_code=404,

                detail=(

                    f"Startup '{startup_name}' "

                    "not found in old dataset"

                )

            )


        # ----------------------------------------------
        # GENERATE OLD INVESTMENT MEMO
        # ----------------------------------------------

        result = generate_investment_memo(

            startup=startup,

            dataset_type=dataset_type

        )


        return result


    except HTTPException:

        raise


    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )


# ==========================================================
# GENERATE NEW INVESTMENT MEMO
# ==========================================================

@router.get(

    "/new/{startup_name}"

)

def create_new_investment_memo(

    startup_name: str

):

    dataset_type = "new"


    try:

        # ----------------------------------------------
        # LOAD STARTUP FROM NEW CSV
        # ----------------------------------------------

        startup = get_startup_by_name(

            startup_name=startup_name,

            dataset_type=dataset_type

        )


        # ----------------------------------------------
        # VALIDATE STARTUP
        # ----------------------------------------------

        if not startup:

            raise HTTPException(

                status_code=404,

                detail=(

                    f"Startup '{startup_name}' "

                    "not found in new dataset"

                )

            )


        # ----------------------------------------------
        # GENERATE NEW INVESTMENT MEMO
        # ----------------------------------------------

        result = generate_investment_memo(

            startup=startup,

            dataset_type=dataset_type

        )


        return result


    except HTTPException:

        raise


    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )


# ==========================================================
# DOWNLOAD OLD INVESTMENT MEMO PDF
# ==========================================================

@router.get(

    "/old/{startup_name}/pdf"

)

def download_old_investment_memo_pdf(

    startup_name: str

):

    dataset_type = "old"


    try:

        # ----------------------------------------------
        # LOAD STARTUP FROM OLD CSV
        # ----------------------------------------------

        startup = get_startup_by_name(

            startup_name=startup_name,

            dataset_type=dataset_type

        )


        # ----------------------------------------------
        # VALIDATE STARTUP
        # ----------------------------------------------

        if not startup:

            raise HTTPException(

                status_code=404,

                detail=(

                    f"Startup '{startup_name}' "

                    "not found in old dataset"

                )

            )


        # ----------------------------------------------
        # GENERATE OLD MEMO + PDF
        # ----------------------------------------------

        result = generate_investment_memo(

            startup=startup,

            dataset_type=dataset_type

        )


        # ----------------------------------------------
        # GET PDF PATH
        # ----------------------------------------------

        pdf_path = result.get(

            "pdf_path"

        )


        # ----------------------------------------------
        # VALIDATE PDF PATH
        # ----------------------------------------------

        if not pdf_path:

            raise HTTPException(

                status_code=404,

                detail=(

                    "Old investment memo PDF "

                    "path was not generated"

                )

            )


        if not os.path.exists(

            pdf_path

        ):

            raise HTTPException(

                status_code=404,

                detail=(

                    "Old investment memo PDF "

                    "file not found"

                )

            )


        # ----------------------------------------------
        # RETURN OLD PDF
        # ----------------------------------------------

        return FileResponse(

            path=pdf_path,

            media_type="application/pdf",

            filename=os.path.basename(

                pdf_path

            )

        )


    except HTTPException:

        raise


    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )


# ==========================================================
# DOWNLOAD NEW INVESTMENT MEMO PDF
# ==========================================================

@router.get(

    "/new/{startup_name}/pdf"

)

def download_new_investment_memo_pdf(

    startup_name: str

):

    dataset_type = "new"


    try:

        # ----------------------------------------------
        # LOAD STARTUP FROM NEW CSV
        # ----------------------------------------------

        startup = get_startup_by_name(

            startup_name=startup_name,

            dataset_type=dataset_type

        )


        # ----------------------------------------------
        # VALIDATE STARTUP
        # ----------------------------------------------

        if not startup:

            raise HTTPException(

                status_code=404,

                detail=(

                    f"Startup '{startup_name}' "

                    "not found in new dataset"

                )

            )


        # ----------------------------------------------
        # GENERATE NEW MEMO + PDF
        # ----------------------------------------------

        result = generate_investment_memo(

            startup=startup,

            dataset_type=dataset_type

        )


        # ----------------------------------------------
        # GET PDF PATH
        # ----------------------------------------------

        pdf_path = result.get(

            "pdf_path"

        )


        # ----------------------------------------------
        # VALIDATE PDF PATH
        # ----------------------------------------------

        if not pdf_path:

            raise HTTPException(

                status_code=404,

                detail=(

                    "New investment memo PDF "

                    "path was not generated"

                )

            )


        if not os.path.exists(

            pdf_path

        ):

            raise HTTPException(

                status_code=404,

                detail=(

                    "New investment memo PDF "

                    "file not found"

                )

            )


        # ----------------------------------------------
        # RETURN NEW PDF
        # ----------------------------------------------

        return FileResponse(

            path=pdf_path,

            media_type="application/pdf",

            filename=os.path.basename(

                pdf_path

            )

        )


    except HTTPException:

        raise


    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )