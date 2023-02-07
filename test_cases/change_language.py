import os
import time
import unittest

from selenium import webdriver

from test_cases.login_to_the_system import TestLoginPage
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class ChangeLanguage(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/login')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player_to_data(self):
        TestLoginPage.test_login_into_the_system(self)
        chang_language = LoginPage(self.driver)
        time.sleep(3)
        chang_language.click_on_the_language()

    time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
