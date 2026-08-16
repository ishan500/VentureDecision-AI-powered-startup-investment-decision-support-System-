# ==========================================================
# INVESTMENT MEMO SERVICE
# VentureIQ
# ==========================================================

from typing import Dict, Any


from api.services.ai_context_service import (

    build_ai_context

)


from api.services.ollama_service import (

    generate_ai_response

)


from api.services.pdf_service import (

    generate_investment_memo_pdf

)


# ==========================================================
# GENERATE INVESTMENT MEMO
# ==========================================================

def generate_investment_memo(

    startup: Dict[str, Any],

    dataset_type: str = "new"

) -> Dict[str, Any]:


    # ======================================================
    # BUILD AI CONTEXT
    # ======================================================

    ai_context = build_ai_context(

        startup=startup,

        feature="investment_memo",

        question=None,

        scenario=None,

        dataset_type=dataset_type

    )


    # ======================================================
    # GENERATE AI RESPONSE USING OLLAMA
    # ======================================================

    ai_response = generate_ai_response(

        context=str(ai_context)

    )


    # ======================================================
    # EXTRACT MEMO TEXT FROM OLLAMA RESPONSE
    # ======================================================

    memo_text = ai_response.get(

        "response",

        ""

    )


    # ======================================================
    # GET STARTUP NAME
    # ======================================================

    startup_name = ai_context.get(

        "startup_name"

    )


    # ======================================================
    # GENERATE INVESTMENT MEMO PDF
    # ======================================================

    pdf_path = generate_investment_memo_pdf(

        startup_name=startup_name,

        dataset_type=dataset_type,

        memo_text=memo_text

    )


    # ======================================================
    # RETURN AI RESPONSE + PDF PATH
    # ======================================================

    return {

        "status": "success",

        "startup_name": startup_name,

        "dataset_type": dataset_type,

        "feature": "investment_memo",


        # ----------------------------------------------
        # AI RESPONSE FROM OLLAMA
        # ----------------------------------------------

        "memo": ai_response,


        # ----------------------------------------------
        # GENERATED PDF PATH
        # ----------------------------------------------

        "pdf_path": pdf_path

    }