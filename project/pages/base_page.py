from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def is_element_present(self, how, what, timeout = 20):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until(EC.presence_of_element_located((how, what)))
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open(self):
        self.browser.get(self.url)