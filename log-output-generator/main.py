import logging
from datetime import datetime
import time

fmt = "%(asctime)s, %(levelname)-8s %(name)-10s [%(filename)s:%(lineno)d] %(message)s"
logging.basicConfig(encoding="utf-8", format=fmt, level=logging.INFO)
logger = logging.getLogger("log-output-generator")

FILE_PATH = "/shared/timestamp.txt"


def main() -> None:
    logger.info("Started!")
    while True:
        with open(FILE_PATH, "w") as f:
            f.write(datetime.now().isoformat())
        time.sleep(5)


if __name__ == "__main__":
    main()
