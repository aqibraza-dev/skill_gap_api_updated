from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.routers import skill_gap_router

app = FastAPI(
    title="Skill Gap Analyzer API",
    description="Provides skill gap analysis and personalized roadmaps.",
    version="1.0.0"
)

# --- CORS Configuration ---
# This allows your Node/Flask/Flutter frontend to call this API.
# WARNING: For production, you should restrict origins.
origins = [
    "http://localhost",
    "http://localhost:3000",  # Example: React default
    "http://localhost:5173",  # Example: Vite default
    "*"  # Allows all origins (NOT For production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# --- Graceful Error Handling ---
# Pydantic handles 422 (Unprocessable Entity) errors automatically.
# This adds a handler for 500 Internal Server Errors.
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": f"An internal server error occurred: {exc}"},
    )

# --- Include Routers ---
app.include_router(skill_gap_router.router, prefix="/api/v1")

# --- Root Endpoint ---
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Skill Gap Analyzer API. Go to /docs for documentation."}