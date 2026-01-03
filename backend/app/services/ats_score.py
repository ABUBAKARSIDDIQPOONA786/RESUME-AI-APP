def calculate_ats_score(text, skills):
    base_score = min(len(skills) * 5, 60)
    formatting_bonus = 20 if len(text) > 500 else 10
    return min(base_score + formatting_bonus, 100)
