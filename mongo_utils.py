from functools import wraps
from fastapi import HTTPException, status
from pymongo.errors import PyMongoError, ServerSelectionTimeoutError


MONGO_HELP = (
    "Cannot reach MongoDB Atlas. Open Atlas > Network Access > Add IP Address "
    "and allow your current IP (or 0.0.0.0/0 for development). "
    "Also confirm the cluster is running and MONGODB_URI in backend/.env is correct."
)


def raise_mongo_unavailable(exc: Exception = None):
    detail = MONGO_HELP
    if exc:
        detail = f"{MONGO_HELP} ({type(exc).__name__})"
    raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=detail)


def mongo_call(fn, *args, **kwargs):
    """Run a Mongo operation; translate connectivity failures into HTTP 503."""
    try:
        return fn(*args, **kwargs)
    except ServerSelectionTimeoutError as e:
        raise_mongo_unavailable(e)
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Database error: {e}",
        )
