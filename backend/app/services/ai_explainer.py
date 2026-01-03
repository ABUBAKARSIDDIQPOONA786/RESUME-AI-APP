def generate_explanation(ats_score, skills, roles):
    return (
        f"The resume achieved an ATS score of {ats_score}% "
        f"based on detected skills such as {', '.join(skills[:5])}. "
        f"These skills align well with roles like {', '.join(roles[:3])}."
    )
