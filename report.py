from core.config import Config
from core.logger import setup_logger

logger = setup_logger()

def main():
    logger.info("Starting report generation...")
    cfg = Config()
    logger.info(cfg["timezone"])
if __name__ == "__main__":
    main()
