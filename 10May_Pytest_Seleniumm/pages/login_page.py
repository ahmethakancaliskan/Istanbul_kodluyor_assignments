from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    __username_input = (By.ID, "user-name")
    __password_input = (By.ID, "password")
    __login_button = (By.ID, "login-button")
    __error_message = (By.XPATH, "//h3[@data-test='error']")

    def enter_username(self, username):
        self.find_element(self.__username_input).send_keys(username)

    def enter_password(self, password):
        self.find_element(self.__password_input).send_keys(password)

    def click_login_button(self):
        self.find_element(self.__login_button).click()

    def get_error_massage(self):
        massage = self.find_element(self.__error_message)
        return massage.text

    def get_login_button(self):
        return self.__login_button



