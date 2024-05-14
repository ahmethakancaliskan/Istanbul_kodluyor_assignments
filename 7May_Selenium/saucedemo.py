import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestCases:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Chrome kullanarak tarayıcıyı başlat
        self.driver.maximize_window()  # Tam ekran yap
        self.driver.implicitly_wait(20)  # sayfa yüklenene kadar gizlice 20 sn bekle

    def test_empty_username_and_password(self):  #CASE 1 boş kullanıcı adı ve şifre testi
        self.driver.get("https://www.saucedemo.com/")
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert error_message == "Epic sadface: Username is required"
        print(f"Case 1 : {error_message}")

    def test_empty_password(self):  #CASE 2 boş şifre testi
        self.driver.get("https://www.saucedemo.com/")
        username_input = self.driver.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert error_message == "Epic sadface: Password is required"
        print(f"Case 2 : {error_message}")

    def test_locked_out_user(self):  #CASE 3 locked_out_user adlı kullanıcı giriş testi
        self.driver.get("https://www.saucedemo.com/")
        username_input = self.driver.find_element(By.ID, "user-name")
        username_input.send_keys("locked_out_user")
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        error_message = self.driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert error_message == "Epic sadface: Sorry, this user has been locked out."
        print(f"Case 3 : {error_message}")

    def test_standard_user_login(self):  #CASE 4 standard user başarılı giriş
        self.driver.get("https://www.saucedemo.com/")
        username_input = self.driver.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        # url inventory.html olana kadar 10 sn bekle
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be("https://www.saucedemo.com/inventory.html"))
        expected_page_url = "https://www.saucedemo.com/inventory.html"
        assert self.driver.current_url == expected_page_url

        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item") # aynı classdaki tüm ürünleri al
        assert len(products) == 6, "Number of products is not 6"
        print(f"Case 4 : ürün sayısı {len(products)}")

    def test_problem_user(self): #CASE 5 anasayfada ürün sepete ekleyip kaldıramama testi
        self.driver.get("https://www.saucedemo.com/")
        username_input = self.driver.find_element(By.ID, "user-name")
        username_input.send_keys("problem_user")
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be("https://www.saucedemo.com/inventory.html"))
        expected_page_url = "https://www.saucedemo.com/inventory.html"
        assert self.driver.current_url == expected_page_url  # inventory.html sayfasına yönlendirilidiğini doğrula

        item = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        item.click() # ürün sepete ekle
        # sağ üstte bulunan dinamik sepet ikonundan sepetteki ürün sayısını al
        sepet = self.driver.find_element(By.XPATH,"//span[@class='shopping_cart_badge']")
        assert sepet.text == "1"
        item = self.driver.find_element(By.ID,"remove-sauce-labs-backpack")
        item.click() # ürün sepetten çıkarma
        sepet = self.driver.find_element(By.XPATH,"//span[@class='shopping_cart_badge']")
        assert sepet.text == "1"
        print(f"Case 5 : sepetteki ürün sayısı {sepet.text}")


test = TestCases()
test.test_problem_user()
test.test_empty_username_and_password()
test.test_empty_password()
test.test_locked_out_user()
test.test_standard_user_login()
