from app.data.roles import ROLE_SKILL_PROFILES
from app.services.skill_extractor import extract_skills

def recommend_roles(resume_text: str):
    resume_skills = extract_skills(resume_text)
    recommendations = []

    for role, role_skills in ROLE_SKILL_PROFILES.items():
        matched = set(resume_skills).intersection(set(role_skills))
        score = (len(matched) / len(role_skills)) * 100

        recommendations.append({
            "role": role,
            "match_score": round(score, 2),
            "matched_skills": list(matched),
            "missing_skills": list(set(role_skills) - matched)
        })

    recommendations.sort(key=lambda x: x["match_score"], reverse=True)
    return recommendations