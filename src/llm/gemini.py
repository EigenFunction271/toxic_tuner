import google.generativeai as genai
from src.config import GEMINI_API_KEY, GEMINI_MODEL
import json
from typing import Dict, Any

# Initialize Gemini
try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(GEMINI_MODEL)
except Exception as e:
    raise RuntimeError(f"Failed to initialize Gemini: {str(e)}. Please check your API key and permissions.")

def analyze_toxicity(transcript: str, context: str = "") -> Dict[str, Any]:
    """
    Analyze conversation toxicity using Gemini.
    
    Args:
        transcript: The conversation text
        context: Optional context about the conversation
        
    Returns:
        dict: Analysis results including scores and roast
        
    Raises:
        RuntimeError: For API or permission errors
        ValueError: For invalid input or response format
    """
    if not transcript.strip():
        raise ValueError("Transcript cannot be empty")
        
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
    
    Analyze this conversation and provide a JSON response with these exact keys:
    {{
        "toxicity_score": <number between 0 and 100>,
        "trait_scores": {{
            "entitlement": <number between 0 and 5>,
            "passive_aggression": <number between 0 and 5>,
            "ego_fragility": <number between 0 and 5>,
            "vagueness_deflection": <number between 0 and 5>,
            "social_awareness": <number between 0 and 5>,
            "gratitude_empathy": <number between 0 and 5>
        }},
        "roast": "<one-line roast>"
    }}

    IMPORTANT: Your response must be valid JSON. Do not include any text before or after the JSON object.
    """
    
    try:
        response = model.generate_content(prompt)
        
        if not response.text:
            raise ValueError("Empty response from Gemini")
            
        # Clean the response text to ensure it's valid JSON
        response_text = response.text.strip()
        
        # Try to find JSON object if there's extra text
        if not response_text.startswith('{'):
            start_idx = response_text.find('{')
            if start_idx == -1:
                raise ValueError("No JSON object found in response")
            response_text = response_text[start_idx:]
            
        if not response_text.endswith('}'):
            end_idx = response_text.rfind('}')
            if end_idx == -1:
                raise ValueError("No JSON object found in response")
            response_text = response_text[:end_idx + 1]
            
        # Parse JSON response
        try:
            result = json.loads(response_text)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON response from Gemini: {str(e)}\nResponse text: {response_text}")
            
        # Validate response structure
        required_keys = ["toxicity_score", "trait_scores", "roast"]
        missing_keys = [key for key in required_keys if key not in result]
        if missing_keys:
            raise ValueError(f"Missing required fields in response: {', '.join(missing_keys)}")
            
        # Validate trait scores
        required_traits = [
            "entitlement", "passive_aggression", "ego_fragility",
            "vagueness_deflection", "social_awareness", "gratitude_empathy"
        ]
        missing_traits = [trait for trait in required_traits if trait not in result["trait_scores"]]
        if missing_traits:
            raise ValueError(f"Missing required trait scores: {', '.join(missing_traits)}")
            
        # Validate score ranges
        if not isinstance(result["toxicity_score"], (int, float)) or not 0 <= result["toxicity_score"] <= 100:
            raise ValueError("Toxicity score must be a number between 0 and 100")
            
        for trait, score in result["trait_scores"].items():
            if not isinstance(score, (int, float)) or not 0 <= score <= 5:
                raise ValueError(f"Trait score for {trait} must be a number between 0 and 5")
                
        if not isinstance(result["roast"], str) or not result["roast"].strip():
            raise ValueError("Roast must be a non-empty string")
            
        return result
        
    except Exception as e:
        if "permission denied" in str(e).lower():
            raise RuntimeError(
                "Permission denied. Please check your API key and ensure you have access to Gemini. "
                "You may need to enable the Gemini API in your Google Cloud Console."
            )
        elif "quota exceeded" in str(e).lower():
            raise RuntimeError(
                "API quota exceeded. Please try again later or check your usage limits."
            )
        else:
            raise RuntimeError(f"Error analyzing toxicity: {str(e)}") 