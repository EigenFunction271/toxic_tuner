import pytesseract
from PIL import Image
import io
from src.config import TESSERACT_CONFIG

def process_image(uploaded_files) -> str:
    """
    Process uploaded images using OCR.
    
    Args:
        uploaded_files: List of uploaded image files
        
    Returns:
        str: Extracted text from images
    """
    all_text = []
    
    for file in uploaded_files:
        # Read image
        image = Image.open(io.BytesIO(file.read()))
        
        # Extract text
        text = pytesseract.image_to_string(
            image,
            config=TESSERACT_CONFIG
        )
        
        all_text.append(text)
    
    # Combine all text
    return "\n".join(all_text) 