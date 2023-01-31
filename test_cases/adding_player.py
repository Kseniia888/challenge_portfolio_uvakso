import os
import time
import unittest

from selenium import webdriver

from pages.add_a_player import AddAPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):




    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/login')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player_into_the_system(self):
        user_adding = LoginPage(self.driver)
        user_adding.title_of_page()
        user_adding.type_in_email('user07@getnada.com')
        user_adding.type_in_password('Test-1234')
        user_adding.click_on_the_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        add_a_player_page = AddAPlayer(self.driver)
        add_a_player_page.click_on_the_span()


        time.sleep(5)





'''
    @classmethod
    def tearDown(self):
        self.driver.quit()

'''