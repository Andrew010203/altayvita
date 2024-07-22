import time

import allure
import pytest
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from pages.basket_page import Basket_page
from pages.data_input_page import Data_input_page
from pages.delivery_to_country_page import Deliveri_to_country_page
from pages.face_page import Face_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page
from pages.placing_an_order_page import Placing_an_order_page
from pages.prod_page_1 import Prod_page_1
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class Test_1():

    @allure.description("Functional testing")
    def test_select_product(self):
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 30, poll_frequency=1)
        action: ActionChains = ActionChains(driver)
        print("start test")

        fp = Face_page(driver)
        fp.enter_personal_cabinet()

        login = Login_page(driver)
        login.authorization()

        mp = Main_page(driver)
        mp.select_product()

        p1p = Prod_page_1(driver)
        p1p.add_product()

        bp = Basket_page(driver) # создаем переменную и присваивавем ей значение модуля страницы "корзина"
        bp.go_to_payment() # вызываем метод из страницы "корзина"

        pp = Payment_page(driver)
        pp.payment()

        po = Placing_an_order_page(driver)
        po.oform()

        dc = Deliveri_to_country_page(driver)
        dc.input_address()

        dip = Data_input_page(driver)
        dip.input_data()

        time.sleep(3)
        print('finish test')









