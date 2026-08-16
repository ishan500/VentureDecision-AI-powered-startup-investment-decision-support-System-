# ==========================================================
# AI CONTEXT SERVICE
# VentureIQ
# ==========================================================


from typing import (

    Dict,

    Any,

    Optional

)


from api.services.ollama_service import (

    generate_natural_language_qa

)


# ==========================================================
# BUILD AI CONTEXT
# ==========================================================


def build_ai_context(

    startup: Dict[str, Any],

    feature: str = "general",

    question: Optional[str] = None,

    scenario: Optional[Dict[str, Any]] = None,

    dataset_type: str = "new"

) -> Dict[str, Any]:


    """

    Builds the context that will be passed to Ollama.

    The ML outputs and feature-engineered values are already
    stored in the CSV dataset.

    Ollama is used only as a natural-language explanation layer.

    """


    # ------------------------------------------------------
    # VALIDATE DATASET TYPE
    # ------------------------------------------------------


    dataset_type = (

        dataset_type

        .strip()

        .lower()

    )


    if dataset_type not in (

        "old",

        "new"

    ):


        raise ValueError(

            "dataset_type must be "

            "'old' or 'new'"

        )


    # ------------------------------------------------------
    # BUILD CONTEXT
    # ------------------------------------------------------


    ai_context = {


        # --------------------------------------------------
        # STARTUP DATA FROM CSV
        # --------------------------------------------------


        "startup_data": startup,


        # --------------------------------------------------
        # STARTUP NAME
        # --------------------------------------------------


        "startup_name": startup.get(

            "Startup_Name"

        ),


        # --------------------------------------------------
        # AI FEATURE
        # --------------------------------------------------


        "feature": feature,


        # --------------------------------------------------
        # QUESTION
        # --------------------------------------------------


        "question": question,


        # --------------------------------------------------
        # SCENARIO
        # --------------------------------------------------


        "scenario": scenario,


        # --------------------------------------------------
        # DATASET TYPE
        # --------------------------------------------------


        "dataset_type": dataset_type

    }


    return ai_context


# ==========================================================
# ASK STARTUP QUESTION
# ==========================================================


def ask_startup_question(

    startup_name: str,

    question: str,

    startup_data: Dict[str, Any],

    dataset_type: str = "new"

) -> str:


    """

    Answers a natural-language question
    about a startup.

    """


    # ------------------------------------------------------
    # BUILD CONTEXT
    # ------------------------------------------------------


    context = build_ai_context(

        startup=startup_data,

        feature="question_answering",

        question=question,

        scenario=None,

        dataset_type=dataset_type

    )


    # ------------------------------------------------------
    # SEND TO OLLAMA
    # ------------------------------------------------------


    answer = generate_natural_language_qa(

        startup_name,

        question,

        context

    )


    return answer