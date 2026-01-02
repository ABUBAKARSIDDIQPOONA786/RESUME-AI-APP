import re

def structure_resume(text: str) -> dict:
    sections = {
        "Contact": "",
        "Summary": "",
        "Experience": "",
        "Education": "",
        "Skills": ""
    }
    
    # Simple regex-based splitting (2026 Standard)
    pattern = r'(Experience|Education|Skills|Projects|Summary)'
    parts = re.split(pattern, text, flags=re.IGNORECASE)
    
    # Zip the list into key-value pairs
    for i in range(1, len(parts), 2):
        key = parts[i].capitalize()
        if key in sections:
            sections[key] = parts[i+1].strip()
            
    return sections
