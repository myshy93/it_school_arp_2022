import logging
from datetime import datetime
from utils import configure_logger, LOGGER_NAME


# MAIN
configure_logger()
logger = logging.getLogger(LOGGER_NAME)

user_name = "Ionut"

logger.info("Starting....")
logger.debug(f"Execution started at {datetime.now()}")

logger.info("Creating database...")
logger.info("Database created.")


logger.info(f"Creating invoice for {user_name}...")
# fct pentru facturi
logger.error("Could not create invoice!")

logger.info("Generating report...")
# fct pt raport
logger.info("Report done.")

logger.debug("Closing database connection....")
logger.error("Database is corrupt...aborting.")
logger.critical("System crash, due to no database instance.")