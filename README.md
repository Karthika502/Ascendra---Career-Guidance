# Ascendra — Agentic AI Career Intelligence Platform

An AI placement mentor that takes a student from **resume → analysis → job match →
cover letter → interview prep**, built as a FastAPI backend + React (Vite/Tailwind)
frontend.

This is the full MVP scaffold covering Features 1–7 from the spec, in priority order.
It runs end-to-end even without API keys (with rule-based fallbacks), and gets
noticeably smarter once you add a free Groq key.

## What's implemented

| Priority | Feature | Status |
|---|---|---|
| 1 | Student Profile | ✅ |
| 1 | Resume Upload + Parsing (PyMuPDF) | ✅ |
| 2 | AI Resume Analysis (0–100 score + reasoning) | ✅ |
| 3 | Smart Job Recommendation (live API + AI matching, local fallback) | ✅ |
| 4 | Cover Letter Generator | ✅ |
| 5 | Interview Preparation | ✅ |
| 6 | Dashboard | ✅ |

No login system, exactly as spec'd — the frontend just remembers your student ID
in the browser.

## Project structure

```
ascendra/
  backend/
    main.py                 FastAPI app + router wiring
    database.py              SQLite + SQLAlchemy session setup
    models.py                 Student, Resume, CoverLetter, InterviewSet
    ai/
      groq_client.py          Shared Groq (Llama) wrapper
      resume_parser.py         PyMuPDF text extraction + structured parsing
      resume_analyzer.py        0-100 scoring engine
      job_matcher.py            Live job fetch (JSearch/Adzuna/local) + AI matching
      cover_letter.py            Cover letter generation
      interview_generator.py      Personalized interview questions
    routes/                  One router per feature (profile, resume, jobs, ...)
    data/local_jobs.json     Fallback dataset when no job API key is set
  frontend/
    src/pages/               Landing, Profile, ResumeAnalysis, JobRecommendations,
                              JobDetails, CoverLetter, Interview, Dashboard
    src/components/          Navbar, Card
```

## 1. Backend setup

```bash
cd backend
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# then edit .env and add your GROQ_API_KEY (free at https://console.groq.com/keys)

uvicorn main:app --reload --port 8000
```

The API is now live at `http://localhost:8000` — interactive docs at
`http://localhost:8000/docs`.

**Without a `GROQ_API_KEY`**, every AI module automatically falls back to a
rule-based version (heuristic resume scoring, skill-overlap job matching, template
cover letters/questions) so the app still fully works while you get your key.

**Job listings**: add `JSEARCH_API_KEY` (RapidAPI) or `ADZUNA_APP_ID` +
`ADZUNA_APP_KEY` to `.env` for live jobs. Without either, Ascendra uses
`backend/data/local_jobs.json` (10 realistic sample listings) so job matching
works out of the box too.

## 2. Frontend setup

```bash
cd frontend
npm install
cp .env.example .env    # VITE_API_BASE=http://localhost:8000
npm run dev
```

Open `http://localhost:5173`.

## 3. Try the full flow

1. **Profile** — fill in your details and skills.
2. **Resume** — upload a PDF resume → get parsed data + AI score/strengths/gaps.
3. **Jobs** — see ranked matches with reasoning and missing skills.
4. **Job Details** → pick a job → **Cover Letter** or **Interview Prep**.
5. **Dashboard** — everything in one place.

## Notes on the spec's tech choices

- **AI**: Groq API running Llama (`llama-3.3-70b-versatile` by default, configurable
  via `GROQ_MODEL`) — fast and free-tier friendly, matches the spec.
- **Resume parsing**: PyMuPDF (`fitz`) for text extraction, then the AI structures
  it into skills/education/projects/certifications/experience/contact.
- **DB**: SQLite via SQLAlchemy — zero setup, matches the spec.
- **Jobs**: JSearch preferred, Adzuna alternative, local dataset fallback — exactly
  the priority order in the spec.

## What's deliberately NOT built (per spec's "Future Scope")

Auto-apply agent, browser automation, LinkedIn/GitHub integration, skill roadmap,
application tracking, email notifications, analytics dashboard, salary prediction,
offer comparison, multi-agent collaboration. These are explicitly out of MVP scope.

## Suggested next steps once this is running

1. Get a free Groq API key and drop it into `backend/.env` — this is the single
   biggest quality jump.
2. Get a JSearch (RapidAPI) key for real, current job listings.
3. Polish the resume upload flow with a progress indicator for the AI analysis step
   (it typically takes a few seconds).
4. If you want persistence across browser sessions instead of just localStorage,
   add a simple login later — the spec deliberately skips this for the MVP.
