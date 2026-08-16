# ==========================================================
# AI CONTEXT ROUTES
# VentureIQ
# ==========================================================

from fastapi import (

    APIRouter,

    HTTPException

)


from pydantic import BaseModel


from api.services.data_service import (

    get_startup_by_name

)


from api.services.ai_context_service import (

    ask_startup_question

)


# ==========================================================
# ROUTER
# ==========================================================

router = APIRouter(

    prefix="/ai-context",

    tags=["AI Context"]

)


# ==========================================================
# REQUEST MODEL
# ==========================================================

class QuestionRequest(BaseModel):

    question: str


# ==========================================================
# OLD DATASET Q&A
# ==========================================================

@router.post(

    "/old/{startup_name}"

)

def ask_old_startup_question(

    startup_name: str,

    request: QuestionRequest

):

    startup_data = get_startup_by_name(

        startup_name,

        "old"

    )


    if startup_data is None:

        raise HTTPException(

            status_code=404,

            detail=(

                f"Startup '{startup_name}' "

                "not found in old dataset"

            )

        )


    answer = ask_startup_question(

        startup_name,

        request.question,

        startup_data

    )


    return {

        "status": "success",

        "startup_name": startup_name,

        "dataset_type": "old",

        "question": request.question,

        "answer": answer

    }


# ==========================================================
# NEW DATASET Q&A
# ==========================================================

@router.post(

    "/new/{startup_name}"

)

def ask_new_startup_question(

    startup_name: str,

    request: QuestionRequest

):

    startup_data = get_startup_by_name(

        startup_name,

        "new"

    )


    if startup_data is None:

        raise HTTPException(

            status_code=404,

            detail=(

                f"Startup '{startup_name}' "

                "not found in new dataset"

            )

        )


    answer = ask_startup_question(

        startup_name,

        request.question,

        startup_data

    )


    return {

        "status": "success",

        "startup_name": startup_name,

        "dataset_type": "new",

        "question": request.question,

        "answer": answer

    }