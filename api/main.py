# ==========================================================
# MAIN APPLICATION
# VentureIQ
# ==========================================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# ==========================================================
# ROUTE IMPORTS
# ==========================================================

from api.routes.ai_context_routes import (
    router as ai_context_router
)

from api.routes.due_dilligence import (
    router as due_diligence_router
)

from api.routes.intelligence_routes import (
    router as intelligence_router
)

from api.routes.investment_memo import (
    router as investment_memo_router
)

from api.routes.prediction_routes import (
    router as prediction_router
)

from api.routes.profile_routes import (
    router as profile_router
)

from api.routes.scenario_routes import (
    router as scenario_router
)

from api.routes.startup_routes import (
    router as startup_router
)

from api.routes.vc_copilot import (
    router as vc_copilot_router
)


# ==========================================================
# CREATE APPLICATION
# ==========================================================

app = FastAPI(
    title="VentureIQ",
    description="AI-Powered Startup Intelligence Platform",
    version="1.0.0"
)


# ==========================================================
# CORS CONFIGURATION
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================================
# REGISTER ROUTERS
# ==========================================================

app.include_router(
    startup_router
)

app.include_router(
    vc_copilot_router
)

app.include_router(
    ai_context_router
)

app.include_router(
    intelligence_router
)

app.include_router(
    scenario_router
)

app.include_router(
    due_diligence_router
)

app.include_router(
    investment_memo_router
)

app.include_router(
    prediction_router
)

app.include_router(
    profile_router
)


# ==========================================================
# ROOT ENDPOINT
# ==========================================================

@app.get("/")
def root():

    return {
        "status": "success",
        "message": "VentureIQ API is running"
    }