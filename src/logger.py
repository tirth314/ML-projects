import logging
import os
from datetime import datetime

# 1. Generate the log file name with the current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the path to the 'logs' directory (without the file name)
logs_dir = os.path.join(os.getcwd(), "logs")

# 3. Create the 'logs' directory if it doesn't already exist
os.makedirs(logs_dir, exist_ok=True)

# 4. Define the full path where the log file will be saved
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# 5. Set up the basic configuration for logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


if __name__ == "__main__":
    logging.info("Logger configuration successful! Logging has started.")