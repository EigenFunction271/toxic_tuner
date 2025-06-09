import google.generativeai as genai
from src.config import GEMINI_API_KEY, GEMINI_MODEL

# Initialize Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(GEMINI_MODEL)

def analyze_toxicity(transcript: str, context: str = "") -> dict:
    """
    Analyze conversation toxicity using Gemini.
    
    Args:
        transcript: The conversation text
        context: Optional context about the conversation
        
    Returns:
        dict: Analysis results including scores and roast
    """
    prompt = f"""
    You are an elite toxicity auditor and moral enforcer. You specialize in identifying emotionally manipulative, entitled, or passive-aggressive behavior in conversations — and calling it out with sharp, cutting clarity.

    Instructions:
    - You are not neutral.
    - You defend people putting in effort and showing emotional maturity.
    - You punish vague freeloaders, entitlement, gaslighting, guilt-tripping, or ego-disguised-as-vibes.
    - If someone expects unearned validation, tell them.
    - If someone burns bridges and blames others, call it out.
    - Be surgical, insightful, and clear — but emotionally cathartic.

    Context: {context}
    
    Transcript:
    {transcript}
    
    Analyze this conversation and provide:
    1. Overall toxicity score (0-100)
    2. Trait scores (0-5 each):
       - Entitlement
       - Passive-aggression
       - Ego fragility
       - Vagueness-as-deflection
       - Social awareness (reverse)
       - Gratitude/empathy (reverse)
    3. A one-line roast of the most toxic person
    
    Format your response as a JSON object with these keys:
    - toxicity_score
    - trait_scores
    - roast
    """
    
    response = model.generate_content(prompt)
    return response.text  # TODO: Parse JSON response 