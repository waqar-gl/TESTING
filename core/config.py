import yaml

class Config:
    def __init__(self, path="config.yaml"):
        with open(path, "r") as f:
            self.data = yaml.safe_load(f)
    def __getitem__(self, item):
        return self.data[item]
