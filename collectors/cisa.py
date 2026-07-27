from typing import List
from core.http import get
from core.models import Advisory
from core.utils import iso_to_datetime
from .base import BaseCollector

URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

class CISACollector(BaseCollector):
  
    name = "CISA KEV"
  
    def collect(self) -> List[Advisory]:
        advisories = []
        data = get(URL).json()
        for item in data["vulnerabilities"]:
            advisories.append(
                Advisory(
                    source="CISA",
                    product=item["product"],
                    title=item["vulnerabilityName"],
                    severity="CRITICAL",
                    score=None,
                    cve=item["cveID"],
                    url="https://www.cisa.gov/known-exploited-vulnerabilities-catalog",
                    published=iso_to_datetime(item["dateAdded"]),
                    updated=iso_to_datetime(item["dateAdded"]),
                    exploited=True,
                    action=item["requiredAction"]
                )
            )
        return advisories
