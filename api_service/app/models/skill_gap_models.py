from pydantic import BaseModel, Field
from typing import List, Dict



class Scores(BaseModel):
    """Pydantic model for the 'scores' object."""
    technical_score: int = Field(..., ge=0, le=10)
    communication_score: int = Field(..., ge=0, le=10)
    dsa_score: int = Field(..., ge=0, le=10)
    ml_score: int = Field(..., ge=0, le=10)
    project_explanation_score: int = Field(..., ge=0, le=10)

class Keywords(BaseModel):
    """Pydantic model for the 'keywords' object."""
    weak_keywords: List[str]
    strong_keywords: List[str]

# Request Body model

class SkillGapRequest(BaseModel):
    """The main request body for the /skill-gap endpoint."""
    scores: Scores
    keywords: Keywords

# Define the Response model 

class Resource(BaseModel):
    topic: str
    link: str

class SkillGapResponse(BaseModel):
    """
    The main response body. This validates emgine output
    before sending it to the client.
    """
    strengths: List[str]
    weaknesses: List[str]
    priority_topics: List[str]
    roadmap_2_weeks: Dict[str, str]
    resources: List[Resource]