import os
import sys

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Missing GEMINI_API_KEY in .env file.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3.1-flash-lite")

SYSTEM_PROMPT = """
You are reviewing interview transcripts and writing concise hiring summaries.

Base the assessment only on what is clearly shown in the interview.

Write in the style of an internal recruiter or hiring manager evaluation:
- balanced and professional
- specific but not overly harsh
- confident but not absolute
- grounded in interview evidence

Do not exaggerate strengths or weaknesses.
Avoid dramatic conclusions or psychological assumptions.
If implementation depth appears weaker than conceptual familiarity, describe it cautiously and naturally.
"""

def build_prompt(transcript: str) -> str:
    return f"""
Review the interview transcript below and generate a structured candidate summary.

Transcript:
{transcript}

Return exactly these sections:

## Topics Covered
- 4 to 8 concise bullet points
- Focus on major interview themes only

## Candidate Profile
- Suggested role and seniority level
- 2 to 4 sentences explaining the assessment
- Mention both strengths and weaker areas if relevant

## Candidate Summary
Write a short recruiter-style summary covering:
- background
- strengths
- gaps or concerns
- communication observations
- overall impression

Additional instructions:
- Do not invent experience or skills
- Keep the assessment grounded in the transcript
- Avoid overly harsh or overly positive language
"""

def summarize_transcript(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as file:
        transcript = file.read().strip()

    if not transcript:
        raise ValueError("Transcript file is empty.")

    prompt = build_prompt(transcript)

    response = model.generate_content(
        SYSTEM_PROMPT + "\n\n" + prompt
    )

    return response.text

def main():
    if len(sys.argv) < 2:
        print("Usage: python summarizer.py <transcript_file>")
        sys.exit(1)

    filepath = sys.argv[1]

    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        sys.exit(1)

    print(f"\nSummarizing transcript: {filepath}")
    print("=" * 60)

    result = summarize_transcript(filepath)

    print(result)

    print("=" * 60)

    os.makedirs("outputs", exist_ok=True)

    filename = os.path.basename(filepath).replace(".txt", "_summary.md")
    output_path = os.path.join("outputs", filename)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(result)

    print(f"\nSummary saved to: {output_path}")

if __name__ == "__main__":
    main()