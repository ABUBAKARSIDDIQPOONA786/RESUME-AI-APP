def recommend_roles(text: str) -> list:
    text_lower = text.lower()
    recommendations = []
    
    # Role Profiles
    PROFILES = {
        "Data Scientist": ["python", "machine learning", "sql", "pytorch"],
        "Full Stack Developer": ["react", "javascript", "fastapi", "sql"],
        "Cloud Engineer": ["aws", "docker", "kubernetes", "terraform"],
        "Product Manager": ["agile", "leadership", "project management"]
    }
    
    for role, required in PROFILES.items():
        match_count = len([s for s in required if s in text_lower])
        match_score = int((match_count / len(required)) * 100)
        
        if match_score > 30: # Only suggest roles with >30% match
            recommendations.append({
                "title": role,
                "match_score": match_score
            })
            
    # Sort by highest match
    return sorted(recommendations, key=lambda x: x['match_score'], reverse=True)
