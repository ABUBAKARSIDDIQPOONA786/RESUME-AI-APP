from pydantic import BaseModel
from typing import List, Optional

class RoleRecommendation(BaseModel):
    title: str
    match_score: int

class ATSDetails(BaseModel):
    skills_detected: List[str]
    sections_found: List[str]
    sections_missing: List[str]
    word_count: int

class ATSAnalysis(BaseModel):
    total_score: int
    summary: str      # For AnalysisBox.jsx
    explanation: str  # For ExplanationBox.jsx
    details: ATSDetails

class ResumeAnalysisResponse(BaseModel):
    filename: str
    status: str
    ats_analysis: ATSAnalysis
    recommended_roles: List[RoleRecommendation]
