def generate_explanation(role: str, ats_score: int, matched_skills: list, missing_skills: list) -> str:
    """
    Returns a high-quality mock explanation instead of calling a real LLM.
    """
    return (
        f"Your resume shows strong suitability for {role} positions, particularly in 2026's competitive market. "
        f"With an ATS score of {ats_score}%, your expertise in {', '.join(matched_skills[:2])} is highly visible. "
        "To reach the 90%+ range, consider quantifying your achievements with specific metrics and "
        f"addressing gaps in {', '.join(missing_skills[:2]) if missing_skills else 'advanced certifications'}."
    )
