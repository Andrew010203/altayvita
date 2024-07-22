import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):
    """ Класс содержащий локаторы и методы для страницы поиск и выбор товара"""

    # Локаторы

    search_field = '//input[@placeholder="Поиск товаров"]'
    prod_1 = '(//div[@data-product-id="4596"])[1]'


    # Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска, и возвращающие результат данного поиска.

    def get_search_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_field)))

    def get_prod_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.prod_1)))

    # Actions - методы, которые будут принимать результат поиска от Getters и производить требуемое действие, например кликать или вводить требуемую информацию.

    def input_search_field(self):
        search_field = self.get_search_field()
        search_field.send_keys('Гриб  Рейши')
        print("Input search and pressed Enter")

    def click_prod_1(self):
        self.get_prod_1().click()
        print("click prod_1")

    # Methods - метод, содержащий список Actions, представленных в виде действий, например один метод может включать в себя несколько действий: вести логин, ввести пароль, нажать кнопку "Войти".

    def select_product(self):
        """комментарий"""
        with allure.step("Select product"):
            self.get_current_url()
            self.input_search_field()
            # self.scroll_page(0, 300)
            self.click_prod_1()


