from .skill_extractor import extract_skills

def calculate_ats_score(text: str, target_role: str = "General"):
    matched_skills = extract_skills(text)
    
    # 2026 Scoring Weights
    score = 0
    text_lower = text.lower()
    
    # 1. Skill Match (50 points)
    score += min(len(matched_skills) * 8, 50)
    
    # 2. Section Headers (30 points)
    headers = ["experience", "education", "projects", "skills", "summary"]
    found_headers = [h for h in headers if h in text_lower]
    score += (len(found_headers) / len(headers)) * 30
    
    # 3. Quantifiable Impact (20 points)
    # 2026 ATS look for metrics (%, $, numbers)
    if re.search(r'\d+%', text) or re.search(r'\$\d+', text):
        score += 20

    # Define missing skills for improvement
    all_needed = ["python", "sql", "aws", "docker"] # Example subset
    missing = [s for s in all_needed if s not in matched_skills]

    return {
        "ats_score": int(score),
        "matched_skills": matched_skills,
        "missing_skills": missing,
        "breakdown": {
            "skills": min(len(matched_skills) * 8, 50),
            "structure": (len(found_headers) / len(headers)) * 30,
            "impact": 20 if (re.search(r'\d+%', text) or re.search(r'\$\d+', text)) else 0
        }
    }
