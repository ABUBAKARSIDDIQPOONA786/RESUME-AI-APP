from pydantic import BaseModel
from typing import List

class ResumeAnalysisResponse(BaseModel):
    ats_score: int
    skills: List[str]
    recommended_roles: List[str]
    explanation: str
