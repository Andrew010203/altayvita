import time

import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Basket_page(Base):
    """ Класс содержащий локаторы и методы для страницы корзина"""

    # Локаторы
    main_word = '//h1[contains(text(),"Корзина заказа")]'
    price_in_basket = '//span[@class="js-item-total"]'
    total_cost = '(//span[@class="js-cart_page_total_amount"])[1]'
    minus_button = '//button[@class="less js-minus"]'
    plus_button = '//button[@class="more js-plus"]'
    go_to_checkout = '(//div[@id="test123"])[1]'


    # Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска, и возвращающие результат данного поиска.

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_price_in_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_in_basket)))

    def get_total_cost(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_cost)))

    def get_minus_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.minus_button)))

    def get_plus_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.plus_button)))

    def get_go_to_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_checkout)))


    # Actions - методы, которые будут принимать результат поиска от Getters и производить требуемое действие, например кликать или вводить требуемую информацию.

    def click_minus_button(self):
        self.get_minus_button().click()
        print("click minus")

    def click_plus_button(self):
        self.get_plus_button().click()
        print("click plus")

    def click_go_to_checkout(self):
        self.get_go_to_checkout().click()
        print("click go to checkout")


    # Methods - метод, содержащий список Actions, представленных в виде действий, например один метод может включать в себя несколько действий: вести логин, ввести пароль, нажать кнопку "Войти".
    def go_to_payment(self):
        """Список действий"""
        with allure.step("Go to payment"):
            self.get_current_url()
            self.assert_word(self.get_main_word(), "Корзина заказа")
            time.sleep(2)
            self.assert_word(self.get_price_in_basket(), "1 660 ₽")
            self.assert_word(self.get_total_cost(), "1 660 ₽")
            self.click_minus_button()
            time.sleep(2)
            self.assert_word(self.get_price_in_basket(), "830 ₽")
            self.assert_word(self.get_total_cost(), "830 ₽")
            time.sleep(2)
            self.click_plus_button()
            time.sleep(2)
            self.assert_word(self.get_price_in_basket(), "1 660 ₽")
            self.assert_word(self.get_total_cost(), "1 660 ₽")
            self.click_go_to_checkout()












