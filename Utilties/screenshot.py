import os
from datetime import datetime


class Screenshot:

    @staticmethod
    def capture(driver, test_name):

        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screenshot_dir = os.path.join(project_root, "Screenshots")

        os.makedirs(screenshot_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"{test_name}_{timestamp}.png"

        file_path = os.path.join(screenshot_dir, file_name)

        driver.save_screenshot(file_path)

        return file_path