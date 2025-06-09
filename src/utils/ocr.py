import google.generativeai as genai
from PIL import Image
import io
from src.config import GEMINI_API_KEY, GEMINI_VISION_MODEL, SAFETY_SETTINGS

# Initialize Gemini
try:
    # Configure with explicit API key
    genai.configure(api_key=GEMINI_API_KEY)
    
    # Test the configuration with a simple model
    model = genai.GenerativeModel(
        GEMINI_VISION_MODEL,
        safety_settings=SAFETY_SETTINGS
    )
    
    # Verify the configuration by making a simple test call
    test_response = model.generate_content("Test")
    if not test_response:
        raise RuntimeError("Failed to get response from Gemini API")
    
except Exception as e:
    error_msg = str(e).lower()
    if "api key" in error_msg or "invalid" in error_msg:
        raise RuntimeError(
            f"Invalid API key configuration: {str(e)}\n"
            "Please verify:\n"
            "1. Your .env file exists and contains GEMINI_API_KEY=your_key_here\n"
            "2. The API key is valid and not expired\n"
            "3. You have enabled the Gemini API in Google Cloud Console\n"
            "Get a new key from: https://makersuite.google.com/app/apikey"
        )
    elif "quota" in error_msg:
        raise RuntimeError(
            "API quota exceeded. Please try again later or check your usage limits."
        )
    else:
        raise RuntimeError(
            f"Failed to initialize Gemini: {str(e)}\n"
            "Please check your API key and ensure you have enabled the Gemini API "
            "in your Google Cloud Console."
        )

def process_image(uploaded_files) -> str:
    """
    Process uploaded images using Gemini's vision capabilities.
    
    Args:
        uploaded_files: List of uploaded image files
        
    Returns:
        str: Extracted text from images
        
    Raises:
        Exception: For image processing errors
    """
    all_text = []
    
    try:
        for file in uploaded_files:
            # Read image
            image = Image.open(io.BytesIO(file.read()))
            
            # Use Gemini to extract text
            response = model.generate_content([
                "Extract the conversation text from this image. Format it as 'Speaker: Message' on each line. Preserve the exact text, including any typos or formatting.",
                image
            ])
            
            text = response.text
            all_text.append(text)
        
        # Combine all text
        return "\n".join(all_text)
        
    except Exception as e:
        error_msg = str(e).lower()
        if "api key" in error_msg or "invalid" in error_msg:
            raise RuntimeError(
                f"Invalid API key during image processing: {str(e)}\n"
                "Please verify your API key is correct and has not expired."
            )
        elif "quota" in error_msg:
            raise RuntimeError(
                "API quota exceeded during image processing. Please try again later."
            )
        else:
            raise RuntimeError(f"Error processing image: {str(e)}") 