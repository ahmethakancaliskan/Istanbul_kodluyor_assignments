from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    driver.quit()
