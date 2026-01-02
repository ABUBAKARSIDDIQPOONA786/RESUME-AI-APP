def calculate_ats_score(resume_text: str, target_role: str):
    resume_text = resume_text.lower()
    skills_found = extract_skills(resume_text)
    role_skills = ROLE_KEYWORDS.get(target_role, [])

    matched = list(set(skills_found).intersection(set(role_skills)))
    missing = list(set(role_skills) - set(skills_found))

    keyword_score = (len(matched) / len(role_skills)) * 40 if role_skills else 0
    experience_score = 20 if re.search(r"\b\d+\+?\s+years\b", resume_text) else 10
    education_score = 10 if any(deg in resume_text for deg in ["b.tech", "bachelor", "master", "m.tech"]) else 5
    formatting_score = 10 if len(skills_found) >= 5 else 5

    total_score = min(
        keyword_score + experience_score + education_score + formatting_score,
        100
    )

    return {
        "ats_score": round(total_score, 2),
        "matched_skills": matched,
        "missing_skills": missing,
        "breakdown": {
            "skills_match": round(keyword_score, 2),
            "experience": experience_score,
            "education": education_score,
            "formatting": formatting_score
        }
    }