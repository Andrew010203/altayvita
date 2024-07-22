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


class Placing_an_order_page(Base):
    """ Класс содержащий локаторы и методы для страницы с указанием номера телефона"""

    # Локаторы

    main_word = '//h1[contains(text(),"Оформление заказа")]'
    tel_number_field = '//input[@id="auth_phone_email"]'
    dalee_button = '//button[contains(text(),"Далее")]'


    # Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска, и возвращающие результат данного поиска.

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_tel_number_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.tel_number_field)))

    def get_dalee_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.dalee_button)))


    # Actions - методы, которые будут принимать результат поиска от Getters и производить требуемое действие, например кликать или вводить требуемую информацию.

    def input_tel_number_field(self):
        self.get_tel_number_field().send_keys("+79990000000")
        print("Input tel number")

    def click_dalee_button(self):
        self.get_dalee_button().click()
        print("click dalee")


    # Methods - метод, содержащий список Actions, представленных в виде действий, например один метод может включать в себя несколько действий: вести логин, ввести пароль, нажать кнопку "Войти".
    def oform(self):
        """комментарий"""
        with allure.step("Ofom"):
            self.get_current_url()
            self.assert_word(self.get_main_word(), "Оформление заказа")
            self.input_tel_number_field()
            self.click_dalee_button()










