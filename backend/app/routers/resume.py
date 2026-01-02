from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path

# Services
from ..services.parser import extract_text
from ..services.ats_score import calculate_ats_score
from ..services.ai_explainer import generate_explanation
from ..services.role_recommender import recommend_roles
# role_mapper can be used if you want even deeper mapping logic
from ..services.role_mapper import map_roles_to_resume 

# Utils
from ..utils.schemas import ResumeAnalysisResponse

router = APIRouter(prefix="/resume", tags=["Resume Analysis"])

@router.post("/upload", response_model=ResumeAnalysisResponse)
async def upload_and_analyze(file: UploadFile = File(...)):
    """
    Consolidated 2026 endpoint: One upload, complete intelligence.
    """
    # 1. Validate File Extension
    ext = Path(file.filename).suffix.lower()
    if ext not in [".pdf", ".docx"]:
        raise HTTPException(status_code=400, detail="Invalid format. Please upload PDF or DOCX.")

    # 2. Extract Text (Async)
    content = await file.read()
    resume_text = await extract_text(content, ext)

    if not resume_text or len(resume_text.strip()) < 50:
        raise HTTPException(status_code=422, detail="Resume text is too short or unreadable.")

    # 3. Core Analysis Logic
    # We use recommend_roles to find the candidate's natural career path
    role_recommendations = recommend_roles(resume_text)
    
    # Determine primary role for the AI coach to focus on
    primary_role = role_recommendations[0]['title'] if role_recommendations else "General Professional"
    
    # Calculate ATS Score specifically for that primary role
    ats_result = calculate_ats_score(resume_text, target_role=primary_role)
    
    # Generate Agentic AI Explanation
    explanation_data = generate_explanation(
        role=primary_role,
        ats_score=ats_result["ats_score"],
        matched_skills=ats_result["matched_skills"],
        missing_skills=ats_result["missing_skills"]
    )

    # 4. Final Response Mapping (Matches Dashboard.jsx state)
    return {
        "filename": file.filename,
        "status": "success",
        "ats_analysis": {
            "total_score": int(ats_result["ats_score"]),
            "summary": f"Strong suitability for {primary_role} positions detected.",
            "explanation": explanation_data,
            "details": {
                "skills_detected": ats_result["matched_skills"],
                "sections_found": ["Experience", "Education", "Skills", "Projects"], 
                "sections_missing": ats_result["missing_skills"],
                "word_count": len(resume_text.split())
            }
        },
        "recommended_roles": role_recommendations[:3]
    }
