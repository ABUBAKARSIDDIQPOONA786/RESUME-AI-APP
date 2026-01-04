from fastapi import APIRouter, UploadFile, File, HTTPException
import tempfile
import os

from app.services.parser import parse_resume
from app.services.skill_extractor import extract_skills
from app.services.ats_score import calculate_ats_score
from app.services.role_mapper import map_roles
from app.services.ai_explainer import generate_explanation
from app.utils.schemas import ResumeAnalysisResponse

router = APIRouter(prefix="/resume", tags=["Resume Analysis"])


@router.post("/upload", response_model=ResumeAnalysisResponse)
async def analyze_resume(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    try:
        # 1️⃣ Save uploaded file temporarily
        suffix = os.path.splitext(file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        # 2️⃣ Parse resume
        text = parse_resume(tmp_path)
        os.remove(tmp_path)

        if not text.strip():
            raise HTTPException(status_code=400, detail="Resume text is empty")

        # 3️⃣ Skill extraction
        skills = extract_skills(text)

        # 4️⃣ ATS score
        ats_score = calculate_ats_score(text, skills)

        # 5️⃣ Role mapping
        roles = map_roles(skills)

        # 6️⃣ AI explanation
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

    except HTTPException:
        raise

    except Exception as e:
        print("❌ Resume analysis failed:", str(e))
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
