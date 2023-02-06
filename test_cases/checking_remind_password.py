import os
import time
import unittest

from selenium import webdriver

from pages.add_a_player import AddAPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestRemindButton(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/login')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
    def test_remind_but_work(self):
        test_login = LoginPage(self.driver)
        test_login.title_of_page()
        test_login.wait_for_button_to_be_clickable()
        test_login.click_on_the_reminder()
        test_login.title_of_reminder()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()



