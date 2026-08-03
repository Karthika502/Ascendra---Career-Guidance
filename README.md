# 🚀 Ascendra – Agentic AI Career Intelligence Platform

> **Agentic AI for Smarter Career Success**

Ascendra is an **AI-powered Career Intelligence Platform** designed to assist students and fresh graduates throughout their placement journey. Instead of relying on multiple platforms for resume building, job searching, cover letter creation, and interview preparation, Ascendra unifies these processes into a single intelligent platform.

The platform leverages **Agentic AI** to understand a student's profile, analyze resumes, recommend suitable career opportunities, generate professional application documents, and prepare users for interviews.

---

# 📌 Problem Statement

Students often struggle with:

* Creating ATS-friendly resumes
* Finding jobs that match their skills
* Writing personalized cover letters
* Preparing for interviews
* Managing multiple placement resources across different platforms

Existing solutions address these problems individually, forcing students to switch between several tools.

Ascendra solves this by providing a single AI-powered platform that guides students through every stage of the placement process.

---

# 🎯 Project Objective

Build an intelligent career assistant capable of:

* Understanding student profiles
* Parsing and analyzing resumes
* Recommending suitable internships and jobs
* Building ATS-friendly resumes
* Generating personalized cover letters
* Preparing students for interviews

---

# ✨ Key Features

* 👤 Student Profile Management
* 📄 Resume Upload & Parsing
* 📊 AI Resume Analysis
* 💼 Smart Job Recommendations
* 📝 AI Resume Builder
* ✉️ AI Cover Letter Generator
* 🎤 AI Interview Preparation
* 📈 Career Dashboard

---

# 🤖 AI Agents

Ascendra follows an **Agentic AI Architecture**, where each agent performs a specialized task.

---

## 1️⃣ Resume Parser Agent

**Class:** `ResumeParserAgent`

### Responsibilities

* Extract text from uploaded resumes
* Identify skills
* Extract education
* Detect projects
* Identify certifications
* Extract work experience
* Parse contact information

### Output

Structured resume data in JSON format.

---

## 2️⃣ Resume Analyzer Agent

**Class:** `ResumeAnalyzerAgent`

### Responsibilities

* Evaluate resume quality
* Calculate Resume Score (0–100)
* Detect strengths
* Detect weaknesses
* Identify missing skills
* Suggest improvements

### Output

Detailed AI-powered resume analysis report.

---

## 3️⃣ Smart Job Matcher Agent

**Class:** `JobMatcherAgent`

### Responsibilities

* Fetch live job listings
* Compare resume against job descriptions
* Calculate job match percentage
* Explain recommendation reasoning
* Highlight missing skills

### Output

Ranked list of personalized job recommendations.

---

## 4️⃣ Resume Builder Agent

**Class:** `ResumeBuilderAgent`

### Responsibilities

* Generate professional resumes
* Improve uploaded resumes
* Rewrite weak bullet points
* Optimize ATS compatibility
* Enhance professional summaries
* Export resumes as downloadable PDFs

### Output

Professional ATS-friendly resume.

---

## 5️⃣ Cover Letter Generator Agent

**Class:** `CoverLetterAgent`

### Responsibilities

* Analyze student profile
* Understand target job description
* Generate personalized cover letters
* Align skills with company requirements

### Output

Professional company-specific cover letter.

---

## 6️⃣ Interview Preparation Agent

**Class:** `InterviewPrepAgent`

### Responsibilities

* Analyze resume
* Analyze job description
* Generate personalized interview questions
* Create HR questions
* Create technical questions
* Generate behavioral questions
* Generate resume-based questions

### Output

Personalized interview preparation report.

---

# 🔄 Application Workflow

```text
Student Profile
        │
        ▼
Resume Upload
        │
        ▼
Resume Parser Agent
        │
        ▼
Resume Analyzer Agent
        │
        ▼
Smart Job Matcher Agent
        │
        ▼
Job Recommendations
        │
        ▼
Select Job
        │
        ├──────────────┐
        ▼              ▼
Resume Builder     Cover Letter Generator
        │              │
        └──────┬───────┘
               ▼
Interview Preparation Agent
               ▼
Career Dashboard
```

---

# 🖥️ Technology Stack

## Frontend

* React.js
* Tailwind CSS
* Axios
* Vite

## Backend

* FastAPI
* Python

## Database

* SQLite
* SQLAlchemy

## Artificial Intelligence

* Groq API
* Llama Models

## Resume Parsing

* PyMuPDF

## PDF Generation

* ReportLab / WeasyPrint

---

# 📂 Project Structure

```text
ascendra/

├── backend/
│   ├── ai/
│   │   ├── groq_client.py
│   │   ├── resume_parser.py
│   │   ├── resume_analyzer.py
│   │   ├── job_matcher.py
│   │   ├── resume_builder.py
│   │   ├── cover_letter.py
│   │   └── interview_generator.py
│   │
│   ├── routes/
│   ├── models/
│   ├── database.py
│   └── main.py
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   ├── services/
│   │   └── assets/
│
├── uploads/
├── database/
└── README.md
```

---

# 📱 Application Pages

* Landing Page
* Student Profile
* Resume Upload
* Resume Analysis
* Job Recommendations
* Job Details
* Resume Builder
* Cover Letter Generator
* Interview Preparation
* Dashboard

---

# 🎨 UI Design

* Modern & Minimal
* Fully Responsive
* Blue–Purple Gradient Theme
* Rounded Components
* Soft Shadows
* Clean Typography
* User-Friendly Navigation

---

# 🎯 Target Users

* College Students
* Final-Year Students
* Fresh Graduates
* Internship Seekers
* Entry-Level Professionals

---

# 🌟 Future Scope

The current version focuses on the core placement workflow. Planned future enhancements include:

* Auto Apply Agent
* LinkedIn Integration
* GitHub Integration
* Skill Gap Analysis
* Career Roadmap Generator
* Placement Readiness Analysis
* Career Mentor Agent
* Email Notifications
* Salary Prediction
* Multi-Agent Collaboration

---

# 💡 Why Ascendra?

Unlike conventional job portals, Ascendra acts as an intelligent career companion that not only recommends opportunities but also improves application quality and interview readiness through specialized AI agents.

By combining resume intelligence, job matching, document generation, and interview preparation into one seamless experience, Ascendra simplifies the placement journey and empowers students to confidently pursue their dream careers.

---

# 👨‍💻 Developed For

Hackathons • Academic Projects • Career Assistance Platforms • AI-Based Recruitment Solutions

---

## 📜 License

This project is developed for educational, research, and hackathon purposes.
