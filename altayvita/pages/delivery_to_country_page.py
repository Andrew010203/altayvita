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


class Deliveri_to_country_page(Base):
    """ Класс содержащий локаторы и методы для страницы выбора города для отправки товара"""

    # Локаторы

    main_word = '//p[contains(text(),"Укажите город, в который отправить заказ")]'
    city_delivery_field = '//input[@id="shipping_city-input"]'
    choose_dropdown_city = '//div[@data-index="0"]'
    dalee_button = '//button[contains(text(),"Далее")]'


    # Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска, и возвращающие результат данного поиска.

    def get_main_word(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_city_delivery_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.city_delivery_field)))

    def get_choose_dropdown_city(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.choose_dropdown_city)))

    def get_dalee_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.dalee_button)))


    # Actions - методы, которые будут принимать результат поиска от Getters и производить требуемое действие, например кликать или вводить требуемую информацию.

    def input_city_delivery_field(self):
        self.get_city_delivery_field().send_keys(Keys.CONTROL + "a")
        self.get_city_delivery_field().send_keys(Keys.DELETE)
        self.get_city_delivery_field().send_keys("Архангельская обл, Архангельск ")
        print("Input tel number")

    def click_choose_dropdown_city(self):
        self.get_choose_dropdown_city().click()
        print("click choose city")

    def click_dalee_button(self):
        self.get_dalee_button().click()
        print("click dalee")


    # Methods - метод, содержащий список Actions, представленных в виде действий, например один метод может включать в себя несколько действий: вести логин, ввести пароль, нажать кнопку "Войти".
    def input_address(self):
        """комментарий"""
        with allure.step("Input address"):
            self.get_current_url()
            self.assert_word(self.get_main_word(), "Укажите город, в который отправить заказ")
            time.sleep(3)
            self.input_city_delivery_field()
            time.sleep(5)
            self.click_choose_dropdown_city()
            time.sleep(2)
            self.click_dalee_button()
            # time.sleep(10)










