import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Data_input_page(Base):
    """ Класс содержащий локаторы и методы для страницы данных"""

    # Локаторы

    main_word = '//h1[@class="d-none d-sm-none d-md-none d-lg-block"]'
    radio_btn_courier = '//div[@data-shipping_type="courier_online"]'
    radio_btn_post = '//div[@data-shipping_type="russian_post"]'
    checkout_btn = '(//button[@type="button"])[3]'
    address_field = '//input[@id="shipping_type_russian_post_address"]'
    fio_field = '//*[@id="shipping_fio_ru"]'


    # Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска, и возвращающие результат данного поиска.

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_radio_btn_courier(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.radio_btn_courier)))

    def get_radio_btn_post(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.radio_btn_post)))

    def get_address_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.address_field)))

    def get_fio_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.fio_field)))

    def get_checkout_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkout_btn)))



    # Actions - методы, которые будут принимать результат поиска от Getters и производить требуемое действие, например кликать или вводить требуемую информацию.

    def click_radio_btn_courier(self):
        self.get_radio_btn_courier().click()
        print("radio btn courier")

    def click_radio_btn_post(self):
        self.get_radio_btn_post().click()
        print("radio btn post")

    def input_address_field(self):
        self.get_address_field().send_keys(Keys.CONTROL + "a")
        self.get_address_field().send_keys(Keys.DELETE)
        self.get_address_field().send_keys("Ленина 20")
        print("Input address")

    def input_fio_field(self):
        self.get_fio_field().send_keys(Keys.CONTROL + "a")
        self.get_fio_field().send_keys(Keys.DELETE)
        self.get_fio_field().send_keys("Иванов Иван Иваныч")
        print("Input fio")

    def click_checkout_btn(self):
        self.get_checkout_btn().click()
        print("click checkout")


    # Methods - метод, содержащий список Actions, представленных в виде действий, например один метод может включать в себя несколько действий: вести логин, ввести пароль, нажать кнопку "Войти".
    def input_data(self):
        """комментарий"""
        with allure.step("Input data"):
            self.get_current_url()
            self.assert_word(self.get_main_word(), "Оформление заказа")
            time.sleep(8)


            self.scroll_page(0, 1000)
            self.click_radio_btn_courier()
            time.sleep(6)
            self.click_radio_btn_post()
            self.input_address_field()
            self.input_fio_field()
            time.sleep(3)
            self.click_checkout_btn()
            time.sleep(5)
            self.get_screenshot()


















