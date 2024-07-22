import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Face_page(Base):
    """ Класс содержащий локаторы и методы для страницы Авторизации"""

    url = "https://altaivita.ru/"

    # Локаторы
    personal_cabinet = '//span[@class="header__personal-name"]'
    login_field = '//input[@class="aj_login"]'
    login_button = '(//button[@class="main-btn green sign-in"])[1]'


    # Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска, и возвращающие результат данного поиска.

    def get_personal_cabinet(self):  # или self.username
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.personal_cabinet)))

    def get_login_field(self):  # или self.username
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_field)))

    def get_login_button(self):  # или self.username
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))



    # Actions - методы, которые будут принимать результат поиска от Getters и производить требуемой действие, например кликать или вводить требуемую информацию.

    def click_personal_cabinet(self):
        self.get_personal_cabinet().click()
        print("Click personal cabinet")

    def input_login_field(self, login):
        self.get_login_field().send_keys(login)
        print("Input login field")
    #
    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")



    # Methods - метод, содержащий список Actions, представленных в виде действий, например один метод может включать в себя несколько действий: вести логин, ввести пароль, нажать кнопку "Войти".
    def enter_personal_cabinet(self):
        """ Авторизация в системе"""
        with allure.step("Enter personal cabinet"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_personal_cabinet()
            self.input_login_field("puk.kak.03@mail.ru")
            self.click_login_button()

