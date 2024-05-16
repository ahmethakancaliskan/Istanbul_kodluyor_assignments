import time
import pytest
from pages.login_page import LoginPage
from pages.base_page import BasePage
from constants import constant


def test_valid_login(driver):
    login_page = LoginPage(driver)
    base_page = BasePage(driver)
    login_page.go_to(constant.BASE_URL)
    login_page.enter_username(constant.VALID_USERNAME)
    login_page.enter_password(constant.VALID_PASSWORD)
    base_page.wait_until_element_visible(login_page.get_login_button())
    login_page.click_login_button()
    assert base_page.get_current_url() == constant.INVENTORY_URL


def test_invalid_login(driver):
    login_page = LoginPage(driver)
    base_page = BasePage(driver)
    login_page.go_to(constant.BASE_URL)
    login_page.enter_username("deneme")
    login_page.enter_password("1234")
    base_page.wait_until_element_visible(login_page.get_login_button())
    login_page.click_login_button()
    assert login_page.get_error_massage() == constant.ERROR_INVALID_LOGIN


def test_empty_password(driver):
    login_page = LoginPage(driver)
    base_page = BasePage(driver)
    login_page.go_to(constant.BASE_URL)
    login_page.enter_username(constant.VALID_USERNAME)
    base_page.wait_until_element_visible(login_page.get_login_button())
    login_page.click_login_button()
    assert login_page.get_error_massage() == constant.ERROR_EMPTY_PASSWORD


def test_empty_username(driver):
    login_page = LoginPage(driver)
    base_page = BasePage(driver)
    login_page.go_to(constant.BASE_URL)
    login_page.enter_password(constant.VALID_PASSWORD)
    base_page.wait_until_element_visible(login_page.get_login_button())
    login_page.click_login_button()
    assert login_page.get_error_massage() == constant.ERROR_EMPTY_USERNAME


def test_empty_login(driver):
    login_page = LoginPage(driver)
    base_page = BasePage(driver)
    login_page.go_to(constant.BASE_URL)
    base_page.wait_until_element_visible(login_page.get_login_button())
    login_page.click_login_button()
    assert login_page.get_error_massage() == constant.ERROR_EMPTY_INPUTS
