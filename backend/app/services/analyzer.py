from .ats_score import calculate_ats_score
from .role_recommender import recommend_roles
from .ai_explainer import generate_explanation

def analyze_resume_content(text: str) -> dict:
    """
    Coordinates all sub-services to provide a unified 2026-standard analysis.
    """
    # 1. Core Logic: Scoring and Roles
    # Defaulting target_role to 'General' unless specified
    ats_result = calculate_ats_score(text, target_role="General")
    roles = recommend_roles(text)
    
    # 2. Agentic AI Layer: Natural language generation
    # Uses top recommended role as the primary target for explanation
    primary_role = roles[0]["title"] if roles else "Software Professional"
    explanation = generate_explanation(
        role=primary_role,
        ats_score=ats_result["ats_score"],
        matched_skills=ats_result["matched_skills"],
        missing_skills=ats_result["missing_skills"]
    )

    # 3. Component Data Mapping
    # Summary for AnalysisBox.jsx
    summary = (
        f"Strong suitability for {primary_role} positions. "
        f"Key skills detected: {', '.join(ats_result['matched_skills'][:3])}."
    )

    return {
        "ats_analysis": {
            "total_score": int(ats_result["ats_score"]),
            "summary": summary,
            "explanation": explanation,
            "details": {
                "skills_detected": ats_result["matched_skills"],
                "sections_found": ["Experience", "Education", "Skills"], # Placeholder logic
                "sections_missing": ats_result["missing_skills"],
                "word_count": len(text.split())
            }
        },
        "recommended_roles": roles[:3]
    }
