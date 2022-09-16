from asyncio.log import logger
import os
import sys
import logging


logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"  ## log directory where we will be storing all the logs
log_filepath = os.path.join(log_dir,"running_logs.log")  
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[                    ## The log handler is the component that effectively writes/displays a log
        logging.FileHandler(log_filepath),   ## we will get the looging info into our logging file
        logging.StreamHandler(sys.stdout)     ## Here the logging info it will print into the terminal as well

    ])

logger = logging.getLogger("DeepClassifier")