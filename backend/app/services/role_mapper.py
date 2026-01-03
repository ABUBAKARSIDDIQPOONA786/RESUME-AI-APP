ROLE_MAP = {
    "Python": ["Backend Engineer", "Data Analyst"],
    "FastAPI": ["Backend Engineer"],
    "React": ["Frontend Engineer"],
}

def map_roles(skills):
    roles = set()
    for skill in skills:
        roles.update(ROLE_MAP.get(skill, []))
    return list(roles) or ["General Software Engineer"]
