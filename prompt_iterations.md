# Prompt Iterations Log

> All iterations were tested against both provided interview transcripts to make sure the prompt worked across different interview styles and role types.

---

# Iteration 1 - Basic Structured Summary

## The Prompt

```text
Read the interview transcript and provide:

1. Topics covered
2. Candidate profile and likely seniority
3. A short summary of the candidate

Transcript:
{transcript}
```

## Input Used (excerpt from Transcript 1)

```text
Interviewer: Have you used Zustand?

Candidate: Zustand, I cannot use this. I worked on React Query.

Interviewer: Can you also write the code for redux slice?

Candidate: Redux slice, okay. I will write.
```

## Output Produced

```text
Topics Covered:
- React state management
- Redux implementation
- Frontend architecture

Candidate Profile:
Senior Frontend Engineer

Candidate Summary:
The candidate has strong frontend development experience in React and Angular ecosystems. They appear confident working with state management and modern frontend tools. Overall, the candidate demonstrates strong technical expertise.
```

## What Worked / What Didn't

This version could identify the broad interview topics and generate readable summaries, but the assessment felt too generic. It labeled the candidate as a senior engineer even though the transcript showed hesitation around Zustand and Redux implementation questions. The summary also relied too much on generic praise and did not mention weaker areas from the interview. Another issue was that the output style changed a lot between transcripts because the prompt structure was too open ended.

For the next iteration, I added stricter formatting and asked the model to justify its assessment using examples from the transcript.

---

# Iteration 2 - Structured Recruiter Style Prompt

## The Prompt

```text
You are a recruiter analyzing an interview transcript.

Produce exactly three sections:

## Topics Covered
List 4-8 concise bullet points describing the main themes discussed.

## Candidate Profile
State the most likely role and seniority level. Justify the assessment using examples from the interview.

## Candidate Summary
Write a concise paragraph covering:
- background
- strengths
- concerns
- overall hiring impression

Transcript:
{transcript}
```

## Input Used (excerpt from Transcript 2)

```text
Candidate: I connected with Experian and CIBIL for credit score. Integrated with our app.

Candidate: I built my own score by giving weightages.

Candidate: Finally I proved it and we stopped that partnership.
```

## Output Produced

```text
## Topics Covered
- Fraud detection workflows
- Vendor management processes
- CRM implementation
- KPI and analytics reporting
- Leadership communication

## Candidate Profile
Program Manager - Senior Level

The candidate described working on fraud prevention systems, vendor coordination, and dashboard reporting across teams. They also showed ownership while handling operational problems and stakeholder discussions.

## Candidate Summary
The candidate has experience in operations, fraud prevention, analytics, and stakeholder coordination. Their strongest examples came from improving fraud detection workflows and implementing process improvements through CRM systems and internal scoring methods. They appeared comfortable working with leadership teams and external vendors. However, some explanations lacked structure and became difficult to follow during longer answers. Overall, the candidate looked capable of handling cross-functional operational responsibilities.
```

## What Worked / What Didn't

This version worked better because the structure became more consistent across both transcripts. The summaries were also more tied to examples from the interview instead of generic praise.

However, another issue showed up during testing. The model still tended to overestimate seniority whenever a candidate talked about ownership or years of experience. For example, Transcript 2 showed good operational ownership, but the communication gaps and lack of deeper strategic discussion made the "Senior Level" label feel slightly too strong. Some outputs also became too polished and overly positive.

For the next iteration, I focused more on tone control, conservative assessment, and reducing exaggerated conclusions.

---

# Iteration 3 - Final Prompt Version

## System Prompt

```text
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
```

## User Prompt

```text
Review the interview transcript below and generate a structured candidate summary.

Return exactly these sections:

## Topics Covered
- 4 to 8 concise bullet points
- Focus only on major interview themes

## Candidate Profile
- Suggested role and seniority level
- 2 to 4 sentences explaining the assessment
- Mention strengths and weaker areas only if they are clearly supported by the interview discussion or follow-up questions

## Candidate Summary
Write a short recruiter-style summary covering:
- background
- strengths
- gaps or concerns
- communication observations
- overall impression

Avoid sounding overly promotional or overly critical.

Additional instructions:
- Do not invent experience or skills
- Keep the assessment grounded in the transcript
```

## Input Used (excerpt from Transcript 1)

```text
Candidate: For global state, Context API along with reducer for token management. For server state, React Query.

Interviewer: Have you used Zustand?

Candidate: Zustand, I cannot use this. I worked on React Query.

Interviewer: Can you write an example of Zustand for creating a useStore?

Candidate: Yeah. Like a constant. Use store. This is the base structure.
```

## Output Produced

```text
## Topics Covered
- AI-assisted software development life cycle
- Ionic framework and mobile-first architecture
- Capacitor plugin implementation for native mobile features
- Angular modular architecture and design patterns
- React state management strategies

## Candidate Profile
- Suggested Role: Senior Frontend / Full-Stack Developer

The candidate demonstrates strong foundational familiarity with Angular, Ionic, and frontend application architecture. While they communicate high-level design approaches comfortably, the interview showed less consistency during follow-up implementation questions around Zustand and Redux patterns.

## Candidate Summary
Prasanna Kumar brings several years of experience in Angular, React, and hybrid mobile application development. His strongest areas appear to be application structure, reusable component thinking, and frontend architecture discussions. He also communicated clearly while discussing workflows, scalability, and AI-assisted development practices. However, the interview showed stronger conceptual familiarity than hands-on implementation depth in some advanced frontend state management areas. Overall, he appears well suited for frontend or hybrid mobile roles that prioritize architectural familiarity and framework experience.
```

## What Worked / What Didn't

This version produced the most balanced results across both transcripts. The summaries became more realistic and sounded closer to actual recruiter notes instead of generated performance reviews. Tone control also improved a lot after reducing exaggerated wording and avoiding absolute conclusions.

The final prompt handled uncertainty better, especially in situations where the candidate showed broader architectural familiarity than deep implementation fluency. It also worked more consistently across both the technical interview transcript and the operations-focused transcript without needing role-specific tuning.

This became the final version used in `summarizer.py`.