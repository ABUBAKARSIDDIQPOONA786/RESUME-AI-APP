from fastapi import APIRouter, UploadFile, File, HTTPException
from ..services.parser import parse_resume
from ..services.skill_extractor import extract_skills
from ..services.ats_score import calculate_ats_score
from ..services.role_mapper import map_roles
from ..services.ai_explainer import generate_explanation
from ..utils.schemas import ResumeAnalysisResponse

router = APIRouter(prefix="/resume", tags=["Resume Analysis"])

@router.post("/upload", response_model=ResumeAnalysisResponse)
async def analyze_resume(file: UploadFile = File(...)):
    try:
        # 1. Parse resume
        text = parse_resume(file)
        if not text:
            raise ValueError("Empty resume text")

        # 2. Skill extraction
        skills = extract_skills(text)

        # 3. ATS score
        ats_score = calculate_ats_score(text, skills)

        # 4. Role mapping
        roles = map_roles(skills)

        # 5. Explanation
        explanation = generate_explanation(
            ats_score=ats_score,
            skills=skills,
            roles=roles
        )

        return ResumeAnalysisResponse(
            ats_score=ats_score,
            skills=skills,
            recommended_roles=roles,
            explanation=explanation
        )

    except Exception as e:
        print("❌ Resume analysis failed:", str(e))
        raise HTTPException(
            status_code=400,
            detail="Resume analysis failed"
        )
