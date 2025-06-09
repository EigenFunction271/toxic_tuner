def format_transcript(text: str) -> str:
    """
    Format raw text into a standardized transcript format.
    
    Args:
        text: Raw text from OCR or direct input
        
    Returns:
        str: Formatted transcript with "Speaker: Message" format
    """
    # Split into lines and clean
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    # Basic formatting
    formatted_lines = []
    for line in lines:
        # If line doesn't have a colon, assume it's a continuation
        if ':' not in line and formatted_lines:
            formatted_lines[-1] += ' ' + line
        else:
            formatted_lines.append(line)
    
    return '\n'.join(formatted_lines)

def extract_speakers(text: str) -> list:
    """
    Extract unique speakers from the transcript.
    
    Args:
        text: Formatted transcript text
        
    Returns:
        list: List of unique speaker names
    """
    speakers = set()
    for line in text.split('\n'):
        if ':' in line:
            speaker = line.split(':', 1)[0].strip()
            speakers.add(speaker)
    return sorted(list(speakers)) 