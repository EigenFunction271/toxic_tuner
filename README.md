# Toxicity Tuner

A Streamlit application that analyzes conversations for toxic behavior using Gemini AI.

## Features
- Upload text or screenshots of conversations
- Auto-detect user roles
- Get toxicity scores and trait breakdowns
- Receive AI-generated roasts of toxic behavior

## Setup

### 1. Get Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your new API key
5. Keep this key secure and never commit it to version control

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
1. Create a `.env` file in the project root:
```bash
cp .env.example .env
```

2. Add your Gemini API key to `.env`:
```
GEMINI_API_KEY=your_api_key_here
```

### 4. Run the App
```bash
streamlit run app.py
```

## Development
- `app.py`: Main Streamlit application
- `src/`: Core application code
  - `llm/`: Gemini integration
  - `utils/`: OCR and text processing
  - `ui/`: Reusable UI components

## Troubleshooting
- If you get an API key error, verify your `.env` file exists and contains the correct key
- For OCR issues, ensure Tesseract is installed on your system:
  - Windows: Download and install from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
  - Mac: `brew install tesseract`
  - Linux: `sudo apt-get install tesseract-ocr`

## License
MIT 