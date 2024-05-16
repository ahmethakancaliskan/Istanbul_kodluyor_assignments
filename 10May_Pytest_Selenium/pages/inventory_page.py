from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    __app_logo = (By.CSS_SELECTOR, ".app_logo")
    __burger_menu = (By.ID, "react-burger-menu-btn")
    __burger_menu_items = (By.CSS_SELECTOR, "a.bm-item")
    __shopping_card = (By.CSS_SELECTOR, ".shopping_cart_link")
    __item_number_in_the_card = (By.CLASS_NAME, "shopping_cart_badge")
    __item_names = (By.CLASS_NAME, "inventory_item_name")
    __product_prices = (By.CLASS_NAME, "inventory_item_price")
    __first_item_button = (By.ID, "add-to-cart-sauce-labs-backpack")

    def get_item_names_list(self):
        list = self.find_elements(self.__item_names)
        item_list = []
        for i in list:
            item_list.append(i.text)
        return item_list

    def get_hamburger_menu_links_list(self):
        self.wait_until_element_visible(self.get_burger_menu_items_locator())
        list = self.find_elements(self.__burger_menu_items)
        links_list = []
        for i in list:
            links_list.append(i.text)
        return links_list

    def click_hamburger_menu(self):
        self.find_element(self.__burger_menu).click()

    def get_burger_menu_items_locator(self):
        return self.__burger_menu_items

    def get_number_of_items_in_the_card(self):
        number = self.find_element(self.__item_number_in_the_card).text
        return int(number)

    def get_first_item_name(self):
        name = self.find_element(self.__item_names)
        return name

    def add_to_card_first_item(self):
        self.find_element(self.__first_item_button).click()
