from fastapi import APIRouter, UploadFile, File, HTTPException
import tempfile, os, traceback

from app.services.parser import parse_resume
from app.services.skill_extractor import extract_skills
from app.services.ats_score import calculate_ats_score
from app.services.role_mapper import map_roles
from app.services.ai_explainer import generate_explanation
from app.utils.schemas import ResumeAnalysisResponse

router = APIRouter(prefix="/resume", tags=["Resume Analysis"])

@router.post("/upload", response_model=ResumeAnalysisResponse)
def analyze_resume(file: UploadFile = File(...)):
    try:
        # ---- Save file safely ----
        suffix = os.path.splitext(file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(file.file.read())
            temp_path = tmp.name

        # ---- Parse ----
        text = parse_resume(temp_path)
        if not text.strip():
            raise ValueError("Parsed resume text is empty")

        # ---- Analysis ----
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
        print("❌ Resume analysis error:")
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        try:
            os.remove(temp_path)
        except:
            pass
