from app.models.skill_gap_models import SkillGapRequest, SkillGapResponse
# Import the (mock) engine from its file
from app.services.skill_gap_engine import analyze_skills
from fastapi import HTTPException

def process_skill_gap(request: SkillGapRequest) -> SkillGapResponse:
    """
    Service layer to process the skill gap request.
    This function is responsible for data transformation.
    """
    
    # 1. Transform the nested Pydantic model into the flat
    #    dictionary that engine expects.
    try:
        engine_input = {
            **request.scores.model_dump(),
            **request.keywords.model_dump()
        }
    except Exception as e:
        # This catch is for safety, though Pydantic handles most of it
        raise HTTPException(status_code=400, detail=f"Error processing request data: {e}")

    # 2. Call engine with the transformed data
    try:
        result_data = analyze_skills(engine_input)
        
        # 3. Validate the engine's output against your Response model
        # This ensures engine is returning what it promised.
        response = SkillGapResponse(**result_data)
        
        return response
        
    except Exception as e:
        # Handle potential errors from engine
        print(f"Error from skill_gap_engine: {e}")
        raise HTTPException(status_code=500, detail="Error in core analysis engine.")