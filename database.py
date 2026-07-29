import os
from datetime import datetime
from pymongo import MongoClient, ASCENDING
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv(
    "MONGODB_URI",
    "mongodb+srv://karthi_admin:test123@cluster0.w3f4uhj.mongodb.net/ascendra?retryWrites=true&w=majority",
)

client = MongoClient(
    MONGODB_URI,
    serverSelectionTimeoutMS=5000,
    connectTimeoutMS=5000,
)
db = client.get_default_database()
if db is None:
    db = client["ascendra"]

users_collection = db["users"]
resumes_collection = db["resumes"]
cover_letters_collection = db["cover_letters"]
interview_sets_collection = db["interview_sets"]


def ensure_indexes():
    """Create indexes once; safe to call repeatedly."""
    try:
        users_collection.create_index([("email", ASCENDING)], unique=True)
        resumes_collection.create_index([("student_id", ASCENDING), ("created_at", ASCENDING)])
        cover_letters_collection.create_index([("student_id", ASCENDING), ("created_at", ASCENDING)])
        interview_sets_collection.create_index([("student_id", ASCENDING), ("created_at", ASCENDING)])
    except Exception as e:
        print(f"[database] Index setup skipped/failed: {e}")


def get_db():
    return db


def utcnow():
    return datetime.utcnow()
