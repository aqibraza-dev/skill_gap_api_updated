from fastapi import APIRouter, Body, HTTPException
from app.models.skill_gap_models import SkillGapRequest, SkillGapResponse
from app.services import skill_gap_service

router = APIRouter()

@router.post(
    "/skill-gap", 
    response_model=SkillGapResponse,
    summary="Analyze Skill Gaps",
    description="Receives skill scores and keywords, then returns a detailed analysis and roadmap."
)
async def get_skill_gap_analysis(
    request: SkillGapRequest = Body(...)
):
    """
    This endpoint processes a user's skill data to identify strengths, 
    weaknesses, and a personalized learning roadmap.
    
    - **scores**: A JSON object containing various skill scores (0-10).
    - **keywords**: A JSON object containing lists of strong and weak keywords.
    
    Returns a complete analysis object.
    """
    try:
        # Delegate all logic to the service layer
        response = skill_gap_service.process_skill_gap(request)
        return response
    except HTTPException as he:
        # Re-raise HTTPExceptions (like 400, 500) from the service
        raise he
    except Exception as e:
        # Catch any other unexpected errors
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")