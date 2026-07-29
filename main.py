from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import ensure_indexes
from routes import auth, profile, resume, jobs, cover_letter, interview, dashboard

app = FastAPI(
    title="Ascendra API",
    description="Multi-user Agentic AI Career Intelligence Platform with MongoDB + JWT auth",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(resume.router)
app.include_router(jobs.router)
app.include_router(cover_letter.router)
app.include_router(interview.router)
app.include_router(dashboard.router)


@app.on_event("startup")
def on_startup():
    ensure_indexes()


@app.get("/")
def root():
    return {"status": "ok", "message": "Ascendra API is running", "version": "2.0.0"}


@app.get("/api/health")
def health():
    from database import client
    mongo_ok = False
    mongo_error = None
    try:
        client.admin.command("ping")
        mongo_ok = True
    except Exception as e:
        mongo_error = str(e)
    return {
        "api": "ok",
        "mongodb": "ok" if mongo_ok else "unreachable",
        "mongodb_error": mongo_error,
        "hint": None if mongo_ok else (
            "Atlas Network Access must allow this machine's IP "
            "(or 0.0.0.0/0 for development)."
        ),
    }
