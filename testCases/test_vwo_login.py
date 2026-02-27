import allure
import pytest
from allure_commons.types import AttachmentType

from pageObjests.VWO_Login_Page import LoginPage
from testCases.conftest import *
from Utilties.readconfig import ReadConfig


class Test_Login:
    Email = ReadConfig.get_email()
    Password = ReadConfig.get_password()

    def test_verify_url(self, setup):
        self.driver = setup
        actual_title = self.driver.title
        expected_title = "Login - VWO"
        allure.attach(self.driver.get_screenshot_as_png(), name="verify_app.vwo_url_pass",
                      attachment_type=AttachmentType.PNG)
        assert actual_title == expected_title, f"Page title {actual_title} but expected {expected_title}"

    def test_user_login_TC_01(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)

        self.lp.enter_emaiId(self.Email)

        self.lp.enter_password(self.Password)

        self.lp.click_sign_in_button()

