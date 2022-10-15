import logging
import time
import uuid

fmt = "%(asctime)s, %(levelname)-8s %(name)-10s [%(filename)s:%(lineno)d] %(message)s"
logging.basicConfig(encoding="utf-8", format=fmt, level=logging.INFO)
logger = logging.getLogger("log-output")


def main() -> None:
    random_string = uuid.uuid4()
    while True:
        logger.info(random_string)
        time.sleep(5)


if __name__ == "__main__":
    main()
