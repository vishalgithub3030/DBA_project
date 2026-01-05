import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Logger is set up.")
logger.info("This is an info message.")
logger.error("This is an error message.")
