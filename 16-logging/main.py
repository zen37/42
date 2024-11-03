import logging

# Basic configuration for root logger
logging.basicConfig(level=logging.INFO)

# Creating loggers
logger1 = logging.getLogger("logger1")
logger2 = logging.getLogger("logger2")

# Without setting levels, logger1 and logger2 will inherit WARNING level
logger1.info("This won't show")  # This won't show because it's at INFO level
logger2.warning("This will show")  # This will show because it's at WARNING level

# Set logger levels explicitly
logger1.setLevel(logging.DEBUG)
logger1.info("This will show now")  # This will show now because we've set DEBUG level

logger2.setLevel(logging.ERROR)
logger2.warning("This won't show")  # This won't show anymore because we've set to ERROR level
