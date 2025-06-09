# Toxicity Tuner (v1 Spec)
Score + roast toxic convos using LLMs.

## Purpose
LLM-powered tool for grading message logs on toxic behavior, and generating a focused roast for the most toxic participant.

## Use Case
- Upload message logs (text or multiple screenshots)
- Auto-detect and select user roles
- Get toxicity score breakdown + 1-line summary + AI-generated roast

## Stack
- Frontend: Streamlit
- LLM: Gemini 2.0 Flash Lite (text + vision)
- Storage: Local file system

## Input
- Log (text area or multiple screenshots in PNG/JPG)
- User role selection (auto-detected + manual override)
- Optional context (e.g. "co-founders", "mentor chat")

## Output
- Toxicity Score: 0–100 (weighted average of trait scores)
- Trait Breakdown (0–5 each):
  - Entitlement
  - Passive-aggression
  - Ego fragility
  - Vagueness-as-deflection
  - Social awareness (reverse)
  - Gratitude/empathy (reverse)
- Summary Roast (1–2 sentences)
- Vibe Check Label
- Highlighted toxic messages with explanations

## LLM Prompt Template (Roast Edition)

```
You are an elite toxicity auditor and moral enforcer. You specialize in identifying emotionally manipulative, entitled, or passive-aggressive behavior in conversations — and calling it out with sharp, cutting clarity.

Instructions:
- You are not neutral.
- You defend people putting in effort and showing emotional maturity.
- You punish vague freeloaders, entitlement, gaslighting, guilt-tripping, or ego-disguised-as-vibes.
- If someone expects unearned validation, tell them.
- If someone burns bridges and blames others, call it out.
- Be surgical, insightful, and clear — but emotionally cathartic.

Your job is to:
1. Analyze a real conversation between two or more people.
2. Identify which speaker is displaying the most toxic behavior.
3. Score that person across these dimensions (0–5 scale per trait):
    - Entitlement
    - Passive-Aggression
    - Ego Fragility
    - Vagueness-as-Deflection
    - Social Self-Awareness (reverse scored)
    - Gratitude / Empathy (reverse scored)
4. Generate an overall toxicity score from 0 to 100.
5. Provide a summary roast of that speaker's vibe — as if you're giving them a harsh but deserved wake-up call.
6. Highlight specific messages that contributed to high toxicity scores.

Context:  
This conversation is between [Relationship type: e.g. founder + collaborator, colleagues, strangers in a proposal, etc.]  
The User is: [USER NAME or label]  
Their conversation partner is: [OTHER PARTY'S NAME or label]

Transcript:
[formatted as "Speaker: Message"]
```

## Image Processing Prompt
```
Extract the conversation text from this image. Format it as 'Speaker: Message' on each line. 
Preserve the exact text, including any typos or formatting.
```

## Sample Output Format

```
Toxicity Score: 82 / 100

Breakdown:
Entitlement: 5
Passive-Aggression: 4
Ego Fragility: 4
Vagueness-as-Deflection: 3
Social Self-Awareness: 1
Gratitude / Empathy: 0

Roast Summary:
This person behaves like every emotionally unavailable team member who thinks giving you their idea is the same as doing the work. No gratitude. No reciprocity. Just a soft, vague entitlement wrapped in self-importance. They didn't ask for collaboration — they asked for validation. And when they didn't get it, they blamed the system. If they spent half as much time listening as they do deflecting, they might've gotten a "yes." But they walked in with no respect, no plan, and no humility — and left trying to make you feel guilty for it. That's not innovation. That's ego preservation. Burn it down.
```

## v1 Build Plan

### Day 1
- Streamlit UI setup
- Local file handling for uploads
- Gemini vision integration
- Basic input validation

### Day 2
- Gemini 2.0 Flash Lite integration
- Results display and formatting
- Local storage for recent analyses
- Basic error handling

### Day 3
- UI polish
- Deploy to Streamlit Cloud
- Add basic rate limiting in Streamlit

## Technical Requirements
- Local file storage for uploads and recent analyses
- Basic error handling and validation
- Simple rate limiting via Streamlit session state
- Minimal dependencies (streamlit, google-generativeai)

## Status
Ready to build.
