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


class Payment_page(Base):
    """ Класс содержащий локаторы и методы для страницы оплаты"""

    # Локаторы

    main_word = '//h1[contains(text(),"Оформление заказа")]'
    next_button = '//div[@class="placing__continue width_input_media_50_100"]'


    # Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска, и возвращающие результат данного поиска.

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_next_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.next_button)))


    # Actions - методы, которые будут принимать результат поиска от Getters и производить требуемое действие, например кликать или вводить требуемую информацию.
    def click_next_button(self):
        self.get_next_button().click()
        print("click next button")


    # Methods - метод, содержащий список Actions, представленных в виде действий, например один метод может включать в себя несколько действий: вести логин, ввести пароль, нажать кнопку "Войти".
    def payment(self):
        """комментарий"""
        with allure.step("Payment"):
            self.get_current_url()
            self.assert_word(self.get_main_word(), "Оформление заказа")
            self.click_next_button()










