from app.services.ats_score import calculate_ats_score

ROLE_SKILL_MAP = {
    "Data Analyst": [
        "sql", "excel", "python", "power bi", "tableau", "statistics"
    ],
    "Machine Learning Engineer": [
        "python", "machine learning", "tensorflow", "pytorch", "model"
    ],
    "Backend Developer": [
        "python", "java", "api", "database", "fastapi", "flask"
    ],
    "Software Engineer": [
        "data structures", "algorithms", "python", "java", "git"
    ],
    "Business Analyst": [
        "excel", "powerpoint", "sql", "requirements", "stakeholders"
    ]
}

def recommend_roles(resume_text: str, top_n: int = 3):
    role_scores = []

    for role in ROLE_SKILL_MAP.keys():
        ats_result = calculate_ats_score(resume_text, role)
        role_scores.append({
            "role": role,
            "match_score": ats_result["ats_score"],
            "matched_keywords": ats_result["matched_keywords"]
        })

    role_scores.sort(key=lambda x: x["match_score"], reverse=True)

    return role_scores[:top_n]