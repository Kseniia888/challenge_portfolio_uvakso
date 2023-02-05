import os
import time
import unittest
from selenium import webdriver

from pages.base_page import BasePage
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage


class TestLoginPage(unittest.TestCase):




    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/login')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_into_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user07@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        base_page = BasePage(self.driver)
        base_page.assert_element_text(self.driver, '//div/div[1]/h5', 'Scouts Panel')



        time.sleep(5)




    @classmethod
    def tearDown(self):
        self.driver.quit()


    #unittest.main()56