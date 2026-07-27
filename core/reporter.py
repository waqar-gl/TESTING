from core.collector_manager import CollectorManager
from core.deduplicator import Deduplicator
from core.filters import filter_advisories
from core.formatter import build_report
from core.state import StateManager

class Reporter:
    def run(self):
        advisories = CollectorManager().run()
        advisories = Deduplicator.run(advisories)
        advisories = filter_advisories(advisories)
        state = StateManager()
        new_items = []
      
        for advisory in advisories:
            if state.is_new(advisory):
                new_items.append(advisory)
                state.mark(advisory)
        state.save()
        report = build_report(new_items)
      
        return report
