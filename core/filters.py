from datetime import timedelta
from core.utils import utc_now

ALLOWED = {
    "CRITICAL",
    "HIGH",
}

def filter_advisories(advisories):

    results = []
    now = utc_now()
    for advisory in advisories:
        if advisory.exploited:
            results.append(advisory)
            continue

        if advisory.severity not in ALLOWED:
            continue

        if now - advisory.published > timedelta(days=2):
            continue
        results.append(advisory)
      
    return results
