from typing import List

def generate_explanation(
    role: str,
    ats_score: float,
    matched_skills: List[str],
    missing_skills: List[str]
):
    explanation = f"""
Your resume has an ATS compatibility score of {ats_score}% for the role of {role}.

Strengths:
- You demonstrate relevant skills such as {", ".join(matched_skills)}.

Areas for improvement:
- Consider adding or strengthening experience in {", ".join(missing_skills)}.

Overall, your profile aligns moderately well with the role, but improving the above areas
can significantly increase your chances of shortlisting.
"""
    return explanation.strip()