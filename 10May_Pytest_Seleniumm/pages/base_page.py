from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# BasePage classı tüm sayfalarda ortak kullanılan reusable selenium methodlarının toplandığı yerdir.
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    # bu method string veri tipinde bir URL ister ve ilgili URL adresine gider
    def go_to(self, URL):
        self.driver.get(URL)

    # bu method bir web elementinin locatarını parametre olarak ister
    # ve ilgili web elementi sayfada görünür olana kadar 20 sn bekler
    def wait_until_element_visible(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
