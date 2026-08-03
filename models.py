from pydantic import BaseModel, Field
from typing import Optional, List, Any
from datetime import datetime

SENSITIVE_FIELDS = {"password_hash", "password"}

def serialize_doc(doc: Optional[dict]) -> Optional[dict]:
    """Convert a MongoDB document into an API-friendly dict (string id, no secrets)."""
    if doc is None:
        return None
    serialized = dict(doc)
    if "_id" in serialized:
        serialized["id"] = str(serialized["_id"])
        del serialized["_id"]
    for field in SENSITIVE_FIELDS:
        serialized.pop(field, None)
    return serialized


def serialize_docs(docs: List[dict]) -> List[dict]:
    return [serialize_doc(d) for d in docs if d is not None]


class StudentProfileIn(BaseModel):
    full_name: str
    college: Optional[str] = None
    degree: Optional[str] = None
    department: Optional[str] = None
    graduation_year: Optional[int] = None
    cgpa: Optional[float] = None
    skills: List[str] = Field(default_factory=list)
    preferred_role: Optional[str] = None
    preferred_location: Optional[str] = None


class StudentProfileOut(StudentProfileIn):
    id: str
    resume_path: Optional[str] = None
    email: Optional[str] = None
    created_at: Optional[Any] = None

    class Config:
        from_attributes = True
