import time
from pages.base_page import BasePage


def test_first(driver):
    page = BasePage(driver, 'https://www.google.com/')
    page.open()
    time.sleep(3)

