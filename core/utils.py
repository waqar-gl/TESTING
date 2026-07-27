from datetime import datetime, timezone

def utc_now() -> datetime:
    return datetime.now(timezone.utc)

def iso_to_datetime(value: str) -> datetime:
    value = value.replace("Z", "+00:00")
    return datetime.fromisoformat(value)
