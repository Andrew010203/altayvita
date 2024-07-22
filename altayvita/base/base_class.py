import datetime



class Base():
    """ Базовый класс, содержащий универсальные методы """
    def __init__(self, driver):
        self.driver = driver


    """Method get current url"""

    def get_current_url(self):
        """Метод проверки url"""
        get_url = self.driver.current_url
        print("current url " + get_url)


    """Method assert word"""

    def assert_word(self, word, result):
        """Проверка значения текста"""
        value_word = word.text
        assert value_word == result
        print("Значение текста верно")


    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot" + now_date + ".png"
        self.driver.save_screenshot(f"screen/{name_screenshot}")
        print("Скриншот выполнен")

    """Method assert url"""

    def assert_url(self, result):
        """Проверка url"""
        get_url = self.driver.current_url
        assert get_url == result
        print("Верный url")


    def scroll_page(self, x, y):
        self.driver.execute_script(f"window.scrollBy({x}, {y})")
        print("scroll to element")


