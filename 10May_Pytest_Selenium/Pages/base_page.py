from selenium import webdriver


class BasePage:
    driver = ""

    def BasePage(self,driver):
        self.driver = driver

