from dataclasses import dataclass
from datetime import datetime


@dataclass
class Advisory:
    source: str
    product: str
    title: str
    severity: str
    score: float | None
    cve: str | None
    url: str
    published: datetime
    updated: datetime
    exploited: bool = False
    action: str | None = None
