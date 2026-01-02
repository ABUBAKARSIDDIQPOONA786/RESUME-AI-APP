import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load API Key from .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize LLM (Using GPT-4o for 2026 high-fidelity reasoning)
llm = ChatOpenAI(
    model="gpt-4o", 
    temperature=0.7, 
    openai_api_key=OPENAI_API_KEY
)

def generate_explanation(role: str, ats_score: int, matched_skills: list, missing_skills: list) -> str:
    """
    Generates a professional, agentic explanation and career advice 
    based on the resume's ATS performance.
    """
    
    template = """
    You are an expert Career Coach and Senior Technical Recruiter in 2026. 
    A candidate has just analyzed their resume for the role of: {role}.
    
    ATS Analysis Results:
    - Compatibility Score: {ats_score}/100
    - Skills Matched: {matched_skills}
    - Critical Gaps: {missing_skills}
    
    Task:
    Provide a professional 3-sentence summary. 
    1. Acknowledge their current strengths.
    2. Explain why the score is at this level based on the gaps.
    3. Give one high-impact, actionable piece of advice for 2026 (e.g., specific certifications, 
       quantifying achievements, or updating to modern tech stacks).
    
    Tone: Encouraging, data-driven, and authoritative.
    """

    prompt = PromptTemplate(
        input_variables=["role", "ats_score", "matched_skills", "missing_skills"],
        template=template,
    )

    # Format data for the prompt
    formatted_matched = ", ".join(matched_skills) if matched_skills else "None detected"
    formatted_missing = ", ".join(missing_skills) if missing_skills else "No major gaps found"

    # Generate content
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run({
        "role": role,
        "ats_score": ats_score,
        "matched_skills": formatted_matched,
        "missing_skills": formatted_missing
    })

    return response.strip()
