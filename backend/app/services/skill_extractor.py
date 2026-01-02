import re

def extract_skills(text: str) -> list:
    # 2026 High-Demand Skill Database
    SKILLS_DB = [
        "python", "javascript", "react", "fastapi", "docker", "kubernetes", 
        "aws", "azure", "sql", "machine learning", "pytorch", "tensorflow",
        "project management", "agile", "leadership", "ui/ux", "terraform"
    ]
    
    text_lower = text.lower()
    found_skills = [skill for skill in SKILLS_DB if re.search(rf'\b{re.escape(skill)}\b', text_lower)]
    return list(set(found_skills))
