from fastapi import APIRouter, UploadFile, File, HTTPException
import tempfile, os

from app.services.parser import parse_resume
from app.services.skill_extractor import extract_skills
from app.services.ats_score import calculate_ats_score
from app.services.role_mapper import map_roles
from app.services.ai_explainer import generate_explanation
from app.utils.schemas import ResumeAnalysisResponse

router = APIRouter(prefix="/resume", tags=["Resume"])

@router.post("/upload", response_model=ResumeAnalysisResponse)
async def analyze_resume(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".docx")):
        raise HTTPException(status_code=400, detail="Invalid file format")

    try:
        # ✅ Save file properly
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        text = parse_resume(tmp_path)
        os.remove(tmp_path)

        if not text.strip():
            raise ValueError("Empty resume")

        skills = extract_skills(text)
        ats_score = calculate_ats_score(text, skills)
        roles = map_roles(skills)
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
        print("❌ ERROR:", str(e))
        raise HTTPException(status_code=500, detail="Resume analysis failed")
