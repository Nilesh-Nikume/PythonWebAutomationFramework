import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Element Locators
    Email_Address_ID = "login-username"
    Pass_word_ID = "login-password"
    Sigh_ID = "js-login-btn"
    Error_message_Id = (By.ID, "js-notification-box-msg")
    Sign_Up

    def enter_emaiId(self, email):
        self.driver.find_element(By.ID, self.Email_Address_ID).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.Pass_word_ID).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(By.ID, self.Sigh_ID).click()

    def get_error_message(self):
        return self.driver.find_element(*self.Error_message_Id).text
