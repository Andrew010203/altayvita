import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Prod_page_1(Base):
    """ Класс содержащий локаторы и методы для страницы товара"""

    # Локаторы

    add_basket = '(//button[@class="main-btn blue"])[1]'
    click_right = '//div[@class="ug-slider-control ug-arrow-right ug-skin-alexis"]'
    click_left = '//div[@class="ug-slider-control ug-arrow-left ug-skin-alexis"]'
    plus_button = '(//button[@class="more js-plus_2_0"])[1]'
    minus_button = '(//button[@class="less js-minus_2_0"])[1]'
    amount_prod = '(//span[@class="count  js-count-number active"])[1]'
    sum_price_basket = '//span[@class="basket-price js-total"]'
    up_radio_btn = '//*[@data-product-id-subtype="699"]'
    price_up_radio_btn = '//span[@class="sum js-product-price"]'
    down_radio_btn = '//*[@data-product-id-subtype="4596"]'
    go_to_basket = '(//a[@href="/cart/"])[1]'
    checkout_button = '//a[@class="dropdown-offer-btn main-btn green link-blue"]'


    # Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска, и возвращающие результат данного поиска.

    def get_add_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_basket)))

    def get_click_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.click_right)))

    def get_click_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.click_left)))

    def get_plus_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.plus_button)))

    def get_minus_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.minus_button)))

    def get_amount_prod(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.amount_prod)))

    def get_sum_price_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sum_price_basket)))

    def get_up_radio_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.up_radio_btn)))

    def get_price_up_radio_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_up_radio_btn)))

    def get_down_radio_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.down_radio_btn)))

    def get_go_to_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_basket)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    # Actions - методы, которые будут принимать результат поиска от Getters и производить требуемое действие, например кликать или вводить требуемую информацию.

    def click_add_basket(self):
        self.get_add_basket().click()
        print("click add basket")

    def click_right_button(self):
        self.get_click_right().click()
        print("click right")

    def click_left_button(self):
        self.get_click_left().click()
        print("click left")

    def click_plus_button(self):
        self.get_plus_button().click()
        print("click plus")

    def click_minus_button(self):
        self.get_minus_button().click()
        print("click minus")

    def click_up_radio_btn(self):
        self.get_up_radio_btn().click()
        print("click up radio btn")

    def click_down_radio_btn(self):
        self.get_down_radio_btn().click()
        print("click down radio btn")

    def click_go_to_basket(self):
        self.get_go_to_basket().click()
        print("click go to basket")


    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("checkout")


    # Methods - метод, содержащий список Actions, представленных в виде действий, например один метод может включать в себя несколько действий: вести логин, ввести пароль, нажать кнопку "Войти".

    def add_product(self):
        """Цепочка действий метода страницы"""
        self.get_current_url()
        self.click_add_basket()
        self.click_right_button()
        time.sleep(1)
        self.click_left_button()
        time.sleep(2)
        self.click_plus_button()
        value_amount_prod = self.get_amount_prod().text
        print(value_amount_prod)
        self.assert_word(self.get_amount_prod(), '1')
        time.sleep(2)
        self.assert_word(self.get_sum_price_basket(), '1 422 ₽')
        self.click_plus_button()
        time.sleep(2)
        self.assert_word(self.get_amount_prod(), '3')
        self.assert_word(self.get_sum_price_basket(), '2 133 ₽')
        self.click_minus_button()
        time.sleep(2)
        self.assert_word(self.get_sum_price_basket(), '1 422 ₽')
        self.assert_word(self.get_amount_prod(), '2')
        time.sleep(2)
        self.click_up_radio_btn()
        time.sleep(2)
        self.assert_word(self.get_price_up_radio_btn(), '513')
        self.click_down_radio_btn()
        self.click_go_to_basket()
        self.click_checkout_button()
