from typing import List
from core.http import get
from core.models import Advisory
from core.utils import iso_to_datetime
from .base import BaseCollector

URL = (
    "https://services.nvd.nist.gov/rest/json/cves/2.0"
    "?cvssV3Severity=HIGH,CRITICAL"
)

class NVDCollector(BaseCollector):

    name = "NVD"

    def collect(self) -> List[Advisory]:
        advisories = []
        data = get(URL).json()
        for item in data.get("vulnerabilities", []):
            cve = item["cve"]
            metrics = cve.get("metrics", {})
            score = None
            severity = "UNKNOWN"
            if "cvssMetricV31" in metrics:
                metric = metrics["cvssMetricV31"][0]
                score = metric["cvssData"]["baseScore"]
                severity = metric["cvssData"]["baseSeverity"]
            description = ""
            for desc in cve["descriptions"]:
                if desc["lang"] == "en":
                    description = desc["value"]
                    break
            advisories.append(
                Advisory(
                    source="NVD",
                    product="Unknown",
                    title=description,
                    severity=severity,
                    score=score,
                    cve=cve["id"],
                    url=f"https://nvd.nist.gov/vuln/detail/{cve['id']}",
                    published=iso_to_datetime(cve["published"]),
                    updated=iso_to_datetime(cve["lastModified"]),
                )
            )
        return advisories
