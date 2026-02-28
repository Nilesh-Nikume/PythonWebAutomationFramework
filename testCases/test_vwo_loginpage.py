import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjests.VWO_Login_Page import LoginPage
from Utilties.readconfig import ReadConfig
from Utilties.Logger import LoggenClass
from Utilties.screenshot import Screenshot


class Test_Login:
    Email = ReadConfig.get_email()  # invalid user use for negative scenario
    Password = ReadConfig.get_password()  # invalid user use for negative scenario
    Active_Email = ReadConfig.valid_user_email()  # valid user use for Positive scenario
    Active_Password = ReadConfig.valid_user_password() # valid user use for Positive scenario

    @allure.title("Test URL Working or Not")
    @allure.description("This test attempt to open ap.vwo.com URL")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Nilesh")
    @allure.testcase("ADD here Jiraticket")
    def test_verify_url(self, setup):
        self.driver = setup
        logger = LoggenClass.log_generator()

        logger.info("===== Test Started: Verify URL =====")

        actual_title = self.driver.title
        expected_title = "Login - VWO"

        logger.info(f"Actual Title: {actual_title}")
        logger.info(f"Expected Title: {expected_title}")

        Screenshot.capture(self.driver, "test_verify_url")

        assert actual_title == expected_title, \
            f"Page title {actual_title} but expected {expected_title}"

        logger.info("===== Test Passed: Verify URL =====")




    @allure.title("Check Error Message")
    @allure.description("This test attempts to log into the website using a wrong login and a password.")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Nilesh")
    # @allure.testcase("ADD here Jiraticket")
    @pytest.mark.negative
    def test_user_login_TC_01(self, setup):
        self.driver = setup
        logger = LoggenClass.log_generator()

        logger.info("===== Test Started: Invalid Login =====")

        self.lp = LoginPage(self.driver)

        logger.info("Entering Email")
        self.lp.enter_emaiId(self.Email)

        logger.info("Entering Password")
        self.lp.enter_password(self.Password)

        logger.info("Clicking Sign In")
        self.lp.click_sign_in_button()

        logger.info("Waiting for error message")

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.lp.Error_message_Id)
        )

        error_message = self.lp.get_error_message()
        logger.info(f"Captured Error Message: {error_message}")

        Screenshot.capture(self.driver, "test_user_login_fail")
        # Attach screenshot
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Invalid_Login_Error",
            attachment_type=AttachmentType.PNG
        )

        assert "did not match" in error_message, \
            f"Unexpected error message: {error_message}"

        logger.info("===== Test Passed: Invalid Login =====")
