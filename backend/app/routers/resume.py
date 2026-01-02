from fastapi import APIRouter, UploadFile, File, Form
import re

from app.services.text_extractor import extract_text
from app.services.skill_extractor import extract_skills
from app.services.resume_structurer import structure_resume
from app.services.ats_score import calculate_ats_score
from app.services.ai_explainer import generate_explanation
from app.services.role_recommender import recommend_roles

router = APIRouter(prefix="/resume", tags=["Resume Analysis"])


@router.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    """
    Extracts text from resume and structures it into sections
    """
    resume_text = extract_text(file)
    structured_resume = structure_resume(resume_text)

    return {
        "structured_resume": structured_resume
    }


@router.post("/score")
async def score_resume(
    file: UploadFile = File(...),
    target_role: str = Form(...)
):
    """
    Calculates ATS score for a given target role
    """
    resume_text = extract_text(file)
    ats_result = calculate_ats_score(resume_text, target_role)

    return ats_result


@router.post("/explain")
async def explain_resume(
    file: UploadFile = File(...),
    target_role: str = Form(...)
):
    """
    Generates ATS score + AI explanation + improvement suggestions
    """
    resume_text = extract_text(file)
    ats_result = calculate_ats_score(resume_text, target_role)

    explanation = generate_explanation(
        role=target_role,
        ats_score=ats_result["ats_score"],
        matched_skills=ats_result["matched_skills"],
        missing_skills=ats_result["missing_skills"]
    )

    return {
        "ats_score": ats_result["ats_score"],
        "matched_skills": ats_result["matched_skills"],
        "missing_skills": ats_result["missing_skills"],
        "breakdown": ats_result["breakdown"],
        "explanation": explanation
    }


@router.post("/recommend-roles")
async def recommend_roles_api(file: UploadFile = File(...)):
    """
    Recommends best-fit job roles based on resume skills
    """
    resume_text = extract_text(file)
    role_recommendations = recommend_roles(resume_text)

    return {
        "recommended_roles": role_recommendations[:3]  # Top 3 roles
    }


@router.post("/full-analysis")
async def full_resume_analysis(
    file: UploadFile = File(...),
    target_role: str = Form(...)
):
    """
    Complete end-to-end resume intelligence:
    - Structuring
    - ATS scoring
    - AI explanation
    - Role recommendations
    """
    resume_text = extract_text(file)

    structured_resume = structure_resume(resume_text)
    ats_result = calculate_ats_score(resume_text, target_role)
    role_recommendations = recommend_roles(resume_text)

    explanation = generate_explanation(
        role=target_role,
        ats_score=ats_result["ats_score"],
        matched_skills=ats_result["matched_skills"],
        missing_skills=ats_result["missing_skills"]
    )

    return {
        "structured_resume": structured_resume,
        "ats_score": ats_result["ats_score"],
        "matched_skills": ats_result["matched_skills"],
        "missing_skills": ats_result["missing_skills"],
        "breakdown": ats_result["breakdown"],
        "explanation": explanation,
        "recommended_roles": role_recommendations[:3]
    }
