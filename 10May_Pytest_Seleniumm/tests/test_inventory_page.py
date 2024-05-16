import time

from pages.base_page import BasePage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from constants import constant


def test_total_items(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    base_page = BasePage(driver)
    base_page.go_to(constant.BASE_URL)
    login_page.enter_username(constant.VALID_USERNAME)
    login_page.enter_password(constant.VALID_PASSWORD)
    login_page.click_login_button()
    assert base_page.get_current_url() == constant.INVENTORY_URL
    actualItemList = inventory_page.get_item_names_list()
    assert actualItemList == constant.PRODUCT_NAMES


def test_hamburger_menu_links(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    base_page = BasePage(driver)
    base_page.go_to(constant.BASE_URL)
    login_page.enter_username(constant.VALID_USERNAME)
    login_page.enter_password(constant.VALID_PASSWORD)
    login_page.click_login_button()
    assert base_page.get_current_url() == constant.INVENTORY_URL
    inventory_page.click_hamburger_menu()
    actualLinksList = inventory_page.get_hamburger_menu_links_list()
    assert actualLinksList == constant.EXPECTED_MENU_ITEMS





def test_add_to_card_first_item(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    base_page = BasePage(driver)
    base_page.go_to(constant.BASE_URL)
    login_page.enter_username(constant.VALID_USERNAME)
    login_page.enter_password(constant.VALID_PASSWORD)
    login_page.click_login_button()
    assert base_page.get_current_url() == constant.INVENTORY_URL
    inventory_page.add_to_card_first_item()
    card = inventory_page.get_number_of_items_in_the_card()
    assert card == 1


# def test_go_to_product_detail_page_by_clicking_first_item_name(driver):
#     login_page = LoginPage(driver)
#     inventory_page = InventoryPage(driver)
#     base_page = BasePage(driver)
#     base_page.go_to(constant.BASE_URL)
#     login_page.enter_username(constant.VALID_USERNAME)
#     login_page.enter_password(constant.VALID_PASSWORD)
#     login_page.click_login_button()
#     assert base_page.get_current_url() == constant.INVENTORY_URL
#     productName = inventory_page.get_first_item_name().text
#     productPrice = inventory_page.
#     inventory_page.add_to_card_first_item()


