from typing import List
from collectors import (
    AWSStatusCollector,
    AnthropicCollector,
    CISACollector,
    CloudflareCollector,
    DockerCollector,
    GitHubCollector,
    NVDCollector,
    UbuntuCollector,
)
from core.logger import setup_logger
from core.models import Advisory

logger = setup_logger()

class CollectorManager:
    def __init__(self):
        self.collectors = [
            CISACollector(),
            NVDCollector(),
            UbuntuCollector(),
            DockerCollector(),
            GitHubCollector(),
            AWSStatusCollector(),
            CloudflareCollector(),
            AnthropicCollector(),
        ]

    def run(self) -> List[Advisory]:
        advisories = []
        for collector in self.collectors:
            try:
                logger.info("Running %s", collector.name)
                advisories.extend(collector.collect())
            except Exception:
                logger.exception("%s failed", collector.name)
        logger.info("Collected %d advisories", len(advisories))
        return advisories
