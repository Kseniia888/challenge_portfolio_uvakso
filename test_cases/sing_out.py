import os
import time
import unittest

from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.log_out_page import LogOut
from test_cases.login_to_the_system import TestLoginPage

class SingOut(unittest.TestCase):

    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/login')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_out(self):
        TestLoginPage.test_login_into_the_system(self)
        time.sleep(3)
        user_login = LogOut(self.driver)
        user_login.sing_out()

        time.sleep(5)






    def tearDown(self):
        self.driver.quit()

