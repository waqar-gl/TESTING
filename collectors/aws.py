import feedparser
from typing import List
from core.models import Advisory
from core.utils import utc_now
from .base import BaseCollector

RSS = "https://status.aws.amazon/rss/all.rss"

class AWSStatusCollector(BaseCollector):

    name = "AWS Status"

    def collect(self) -> List[Advisory]:
        advisories = []
        feed = feedparser.parse(RSS)
        for entry in feed.entries[:10]:
            if "service is operating normally" in entry.title.lower():
                continue
            advisories.append(
                Advisory(
                    source="AWS",
                    product="AWS",
                    title=entry.title,
                    severity="HIGH",
                    score=None,
                    cve=None,
                    url=entry.link,
                    published=utc_now(),
                    updated=utc_now(),
                )
            )
        return advisories
