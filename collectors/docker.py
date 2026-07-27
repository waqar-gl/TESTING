from .base import BaseCollector

class DockerCollector(BaseCollector):
    name = "Docker"
    def collect(self):
        return []
