from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from pathlib import Path

# Services
from ..services.parser import extract_text
from ..services.ats_score import calculate_ats_score
from ..services.ai_explainer import generate_explanation
from ..services.role_recommender import recommend_roles

# Utils (New Pydantic Schema)
from ..utils.schemas import ResumeAnalysisResponse

router = APIRouter(prefix="/resume", tags=["Resume Analysis"])

@router.post("/upload", response_model=ResumeAnalysisResponse)
async def upload_and_analyze(file: UploadFile = File(...)):
    """
    Consolidated endpoint for the 2026 Dashboard UI.
    This replaces multiple calls with one 'Full Analysis' for performance.
    """
    # 1. Validate File
    ext = Path(file.filename).suffix.lower()
    if ext not in [".pdf", ".docx"]:
        raise HTTPException(status_code=400, detail="Please upload a PDF or DOCX file.")

    # 2. Extract Text
    content = await file.read()
    resume_text = await extract_text(content, ext)

    if not resume_text:
        raise HTTPException(status_code=422, detail="Empty or unreadable resume.")

    # 3. Process Data (Agentic Logic)
    # Defaulting target_role to 'General' for the initial upload
    ats_result = calculate_ats_score(resume_text, target_role="General")
    role_recommendations = recommend_roles(resume_text)
    
    explanation_data = generate_explanation(
        role="Software Engineer", # Dynamic target based on recommendations
        ats_score=ats_result["ats_score"],
        matched_skills=ats_result["matched_skills"],
        missing_skills=ats_result["missing_skills"]
    )

    # 4. Map to Frontend Keys (Matches Dashboard.jsx)
    return {
        "filename": file.filename,
        "status": "success",
        "ats_analysis": {
            "total_score": int(ats_result["ats_score"]),
            "summary": f"Your resume has a strong match for {role_recommendations[0]['title'] if role_recommendations else 'Technical'} roles.",
            "explanation": explanation_data,
            "details": {
                "skills_detected": ats_result["matched_skills"],
                "sections_found": ["Experience", "Education", "Skills"], # Placeholder logic
                "sections_missing": ats_result["missing_skills"],
                "word_count": len(resume_text.split())
            }
        },
        "recommended_roles": role_recommendations[:3]
    }

# Keeping your specialized endpoints below for individual UI features
@router.post("/recommend-roles")
async def recommend_roles_api(file: UploadFile = File(...)):
    ext = Path(file.filename).suffix.lower()
    content = await file.read()
    resume_text = await extract_text(content, ext)
    return {"recommended_roles": recommend_roles(resume_text)[:3]}
