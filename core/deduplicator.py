from core.models import Advisory

class Deduplicator:

    @staticmethod
    def run(advisories: list[Advisory]) -> list[Advisory]:
        seen = {}
        for advisory in advisories:
            key = advisory.cve

            if not key:
                key = advisory.source + advisory.title

            if key not in seen:
                seen[key] = advisory
                continue
            existing = seen[key]

            if advisory.exploited:
                seen[key] = advisory
                continue

            if advisory.score and existing.score:

                if advisory.score > existing.score:
                    seen[key] = advisory
                  
        return list(seen.values())
