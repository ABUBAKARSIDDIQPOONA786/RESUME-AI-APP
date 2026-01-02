KNOWN_SKILLS = [
    "python", "sql", "excel", "power bi", "tableau", "machine learning",
    "deep learning", "tensorflow", "pytorch", "fastapi", "flask",
    "java", "git", "docker", "aws"
]

def extract_skills(text: str):
    text = text.lower()
    found_skills = []

    for skill in KNOWN_SKILLS:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))