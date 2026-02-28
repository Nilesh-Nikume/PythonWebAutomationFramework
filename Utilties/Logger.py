import os
import inspect
import logging
from datetime import datetime


class LoggenClass:

    @staticmethod
    def log_generator():

        # Get caller method name
        log_name = inspect.stack()[1][3]

        logger = logging.getLogger(log_name)
        logger.setLevel(logging.INFO)

        # Prevent duplicate logs
        if not logger.handlers:

            # Project root path
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

            # Logs folder (already exists in root)
            log_dir = os.path.join(project_root, "Logs")
            os.makedirs(log_dir, exist_ok=True)

            # Create date-wise log file
            date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            log_file_path = os.path.join(log_dir, f"{date_str}.log")

            file_handler = logging.FileHandler(log_file_path)

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | "
                "%(funcName)s | %(lineno)d | %(message)s"
            )

            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger