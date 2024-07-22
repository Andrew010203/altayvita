import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):
    """ Класс содержащий локаторы и методы для страницы Авторизации"""

    url = "https://altaivita.ru/login/?login=puk.kak.03@mail.ru"

    # Локаторы
    password_field = '//input[@class="password"]'
    main_word = '//h1[@style="margin-bottom: 0px;"]'
    submit_button = '(//button[@type="submit"])[3]'

    # Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска, и возвращающие результат данного поиска.

    def get_password_field(self):  # или self.password
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_submit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submit_button)))


    # Actions - методы, которые будут принимать результат поиска от Getters и производить требуемое действие, например кликать или вводить требуемую информацию.

    def input_password_field(self, password):
        self.get_password_field().send_keys(password)
        print("Input password")

    def click_submit_button(self):
        self.get_submit_button().click()
        print("Click submit button")


    # Methods - метод, содержащий список Actions, представленных в виде действий, например один метод может включать в себя несколько действий: вести логин, ввести пароль, нажать кнопку "Войти".
    def authorization(self):
        """ Авторизация в системе"""
        with allure.step("Authorization"):
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_password_field('1234')
            self.click_submit_button()  # вызов метода по вводу информации в поле Логин
            self.assert_word(self.get_main_word(), "вход в личный кабинет")  # вызов метода проверки ключевого слова на странице