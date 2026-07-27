import requests

class NtfyNotifier:
    def __init__(self, server, topic):
        self.server = server.rstrip("/")
        self.topic = topic
    def send(self, title, message):
        requests.post(
            f"{self.server}/{self.topic}",
            data=message.encode(),
            headers={
                "Title": title,
                "Markdown": "yes",
                "Priority": "high"
            },
            timeout=20
        )
