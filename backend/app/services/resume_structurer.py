import re

SECTION_HEADERS = {
    "skills": ["skills", "technical skills", "key skills"],
    "experience": ["experience", "work experience", "employment"],
    "education": ["education", "academic"],
    "projects": ["projects", "academic projects", "personal projects"],
    "certifications": ["certifications", "certificates"]
}

def structure_resume(resume_text: str):
    resume_text = resume_text.lower()
    lines = resume_text.split("\n")

    structured_data = {
        "skills": [],
        "experience": [],
        "education": [],
        "projects": [],
        "certifications": []
    }

    current_section = None

    for line in lines:
        line = line.strip()

        for section, keywords in SECTION_HEADERS.items():
            if any(k == line for k in keywords):
                current_section = section
                break

        if current_section and line and line not in SECTION_HEADERS.get(current_section, []):
            structured_data[current_section].append(line)

    return structured_data