from core.config import Config
from core.notifier import NtfyNotifier
from core.reporter import Reporter

def main():
    cfg = Config()
    report = Reporter().run()
    notifier = NtfyNotifier(
        cfg["ntfy"]["server"],
        cfg["ntfy"]["topic"],
    )
    notifier.send(
        "DevOps Security Digest",
        report,
    )

if __name__ == "__main__":
    main()
