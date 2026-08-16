# ==========================================================
# OLLAMA Q&A TEST SCRIPT
# VentureIQ
# ==========================================================

import sys

import os

import requests


# ==========================================================
# ADD PROJECT ROOT TO PYTHON PATH
# ==========================================================

PROJECT_ROOT = os.path.dirname(

    os.path.dirname(

        os.path.abspath(__file__)

    )

)


sys.path.append(

    PROJECT_ROOT

)


# ==========================================================
# IMPORT DATA SERVICE
# ==========================================================

from api.services.data_service import (

    get_startup_by_name

)


# ==========================================================
# OLLAMA CONFIGURATION
# ==========================================================

OLLAMA_URL = (

    "http://localhost:11434/api/generate"

)


OLLAMA_MODEL = (

    "qwen2.5:3b"

)


# ==========================================================
# GET STARTUP CONTEXT
# ==========================================================

def get_startup_context(

    startup_name,

    dataset_type

):

    startup_data = get_startup_by_name(

        startup_name,

        dataset_type

    )


    if startup_data is None:

        return None


    context = "\n".join(

        [

            f"{key}: {value}"

            for key, value

            in startup_data.items()

        ]

    )


    return context


# ==========================================================
# ASK OLLAMA
# ==========================================================

def ask_ollama(

    question,

    startup_name,

    dataset_type

):

    context = get_startup_context(

        startup_name,

        dataset_type

    )


    if context is None:

        print()

        print(

            f"Startup '{startup_name}' "

            f"not found in "

            f"'{dataset_type}' dataset."

        )

        return


    prompt = f"""

You are VentureIQ, an AI startup intelligence assistant.

Answer the user's question specifically about the startup provided below.

Use the startup data as your primary source.

Do not say that you do not know the startup if data is provided.

Do not give generic information unrelated to the startup.

For questions about risk, advantages, disadvantages,

investment, strengths, weaknesses, or opportunities,

derive the answer from the available startup metrics.

Explain the reasoning clearly.

Startup Name:

{startup_name}


Dataset Type:

{dataset_type}


Startup Data:

{context}


User Question:

{question}


Answer specifically for {startup_name}.

"""


    payload = {

        "model": OLLAMA_MODEL,

        "prompt": prompt,

        "stream": False

    }


    try:

        response = requests.post(

            OLLAMA_URL,

            json=payload,

            timeout=300

        )


        response.raise_for_status()


        result = response.json()


        answer = result.get(

            "response",

            "No response received."

        )


        print()

        print("=" * 70)

        print("VENTUREIQ AI ANSWER")

        print("=" * 70)

        print()

        print(answer)

        print()

        print("=" * 70)


    except requests.exceptions.RequestException as error:

        print()

        print(

            "Ollama request failed:"

        )

        print(error)


# ==========================================================
# MAIN TEST LOOP
# ==========================================================

if __name__ == "__main__":

    print()

    print("=" * 70)

    print(

        "VENTUREIQ OLLAMA Q&A TESTER"

    )

    print("=" * 70)

    print()


    startup_name = input(

        "Enter startup name: "

    )


    dataset_type = input(

        "Enter dataset type (old/new): "

    )


    print()

    print(

        "Ask questions about the startup."

    )

    print(

        "Type 'exit' to stop."

    )

    print()


    while True:

        question = input(

            "Question: "

        )


        if question.lower().strip() == "exit":

            print()

            print(

                "Exiting VentureIQ Q&A."

            )

            break


        ask_ollama(

            question,

            startup_name,

            dataset_type

        )