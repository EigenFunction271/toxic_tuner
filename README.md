# Toxicity Tuner

A Streamlit application that analyzes conversations for toxic behavior using Gemini AI.

## Features
- Upload text or screenshots of conversations
- Auto-detect user roles
- Get toxicity scores and trait breakdowns
- Receive AI-generated roasts of toxic behavior

## Setup

### 1. Set Up Gemini API
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Enable the Gemini API:
   - Go to [Google Cloud Console](https://console.cloud.google.com)
   - Create a new project or select existing one
   - Enable the "Gemini API" for your project
   - Set up billing (required for API access)
4. Create API Key:
   - Go back to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Click "Create API Key"
   - Copy your new API key
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
  - `utils/`: Text processing utilities
  - `ui/`: Reusable UI components

## Troubleshooting
- If you get an API key error:
  - Verify your `.env` file exists and contains the correct key
  - Check that you've enabled the Gemini API in Google Cloud Console
  - Ensure billing is set up for your Google Cloud project
  - Try creating a new API key if issues persist
- For image processing issues:
  - Ensure your images are clear and well-lit
  - Try reducing image size before upload
- If the app is slow:
  - Check your internet connection
  - Reduce image size before upload
  - Consider upgrading your Google Cloud quota if needed

## License
MIT 