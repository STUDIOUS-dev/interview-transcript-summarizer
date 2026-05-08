# Intervue

## Interview Transcript Summarizer

A simple LLM-based tool that takes an interview transcript as input and generates a structured hiring summary.

The output includes:
- Topics covered during the interview
- Suggested candidate profile and likely seniority
- A concise recruiter-style candidate summary

---

# Setup

## Prerequisites

- Python 3.8+
- Gemini API key from Google AI Studio

Install dependencies:

```bash
pip install google-generativeai python-dotenv
```

---

# API Key Setup

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

The `.env` file should not be committed to GitHub.

Recommended `.gitignore` entry:

```gitignore
.env
```

---

# How to Run

Run the script using:

```bash
python summarizer.py sample_transcript_assignment_1.txt
```

You can also test with:

```bash
python summarizer.py sample_transcript_assignment_2.txt
```

The generated summary is:
- printed in the terminal
- saved as a `.md` file in the same directory

Example:

```bash
sample_transcript_assignment_1_summary.md
```

---

# Model Used

Provider:
- Google AI Studio

Model:
- `gemini-3.1-flash-lite`

Reason for choosing:
- Fast responses
- Large context window
- Free tier access
- Good instruction following for structured outputs

---

# Prompt Design Approach

The main focus of the assignment was prompt quality rather than complex engineering.

The prompt evolved across multiple iterations to improve:
- output consistency
- evidence-based assessment
- handling of vague or incomplete answers
- realistic seniority estimation
- separation between broad familiarity and deeper expertise

Both provided transcripts were used during testing to avoid overfitting the prompt to a single interview style.

---

# Reflection

One thing that stood out during testing was how easily the model would overestimate candidates when the prompt was too open ended. In early versions, candidates were often labeled as "senior" based mostly on years of experience or familiarity with technical terminology. Adding instructions around conservative seniority estimation made the summaries feel more realistic.

Another issue was that early prompts often produced summaries that sounded too polished or overly positive. Adding tone guidance and asking the model to stay closer to realistic recruiter-style evaluations made the summaries feel more natural.

If I had more time, I would explore:
- structured JSON output for easier downstream parsing
- confidence scoring for profile estimation
- a second evaluation pass to check for unsupported claims or hallucinated details

---

# Limitations

- Very short transcripts reduce the reliability of seniority estimation.
- Informal or highly unstructured conversations can make topic extraction less consistent.
- The system relies entirely on transcript content and does not verify technical correctness or claimed experience.
- Multi-speaker transcripts can sometimes blur the distinction between interviewer discussion topics and candidate expertise.
- The quality of the output still depends heavily on how detailed the interview discussion is. Stronger transcripts naturally lead to more reliable assessments.