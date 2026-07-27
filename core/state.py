import json
from pathlib import Path

STATE_FILE = Path("state/reported.json")

class StateManager:
    def __init__(self):
        self.data = set()

        if STATE_FILE.exists():
            self.data = set(json.loads(STATE_FILE.read_text()))

    def is_new(self, advisory):
        key = advisory.cve or advisory.title
        return key not in self.data

    def mark(self, advisory):
        key = advisory.cve or advisory.title
        self.data.add(key)

    def save(self):
        STATE_FILE.parent.mkdir(exist_ok=True)
        STATE_FILE.write_text(
            json.dumps(
                sorted(self.data),
                indent=2,
            )
        )
