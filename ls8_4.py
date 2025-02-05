import logging

logging.basicConfig(level=logging.DEBUG, filemode="w", filename="_ls8_4-logs.log",
                    format="Next logging message - %(asctime)s:%(levelname)s - "
                           "%(relativeCreated)d - %(module)s - %(message)s")

logging.debug("debug")
logging.info("info")

try:
    print(10/0)
except ZeroDivisionError:
    logging.exception("Exception")
