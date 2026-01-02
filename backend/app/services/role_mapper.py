def map_roles_to_resume(text: str) -> list:
    
    text_lower = text.lower()
    
    # 2026 Role-Skill Matrix
    JOB_PROFILES = {
        "AI/ML Engineer": {
            "required": ["python", "pytorch", "tensorflow", "scikit-learn", "llm", "pandas"],
            "weight": 1.2
        },
        "Full Stack Developer": {
            "required": ["react", "node.js", "typescript", "fastapi", "postgresql", "tailwind"],
            "weight": 1.0
        },
        "Cloud Solutions Architect": {
            "required": ["aws", "azure", "docker", "kubernetes", "terraform", "ci/cd"],
            "weight": 1.1
        },
        "Data Analyst": {
            "required": ["sql", "power bi", "tableau", "excel", "python", "statistics"],
            "weight": 0.9
        },
        "Product Manager": {
            "required": ["agile", "scrum", "roadmap", "stakeholder", "product lifecycle", "jira"],
            "weight": 1.0
        }
    }

    recommendations = []

    for role, criteria in JOB_PROFILES.items():
        required_skills = criteria["required"]
        # Calculate how many key skills from this profile are in the resume
        matches = [skill for skill in required_skills if skill in text_lower]
        
        if len(matches) > 0:
            # Base score = (matched / total) * 100
            base_score = (len(matches) / len(required_skills)) * 100
            
            # Apply 2026 Market Demand Weight
            final_score = min(int(base_score * criteria["weight"]), 100)

            # Only recommend if match is meaningful (e.g., > 25%)
            if final_score > 25:
                recommendations.append({
                    "title": role,
                    "match_score": final_score
                })

    # Sort by highest match score
    return sorted(recommendations, key=lambda x: x["match_score"], reverse=True)
