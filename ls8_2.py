import logging

# logging.basicConfig(level=logging.DEBUG)
logging.warning("warning")
logging.error("error")
logging.critical("critical")
logging.debug("debug")
logging.info("info")

logging.basicConfig(level=logging.DEBUG)
logging.debug("debug2")
logging.info("info2")
