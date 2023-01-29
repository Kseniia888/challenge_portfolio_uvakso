import os
import unittest
from selenium import webdriver
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



    @classmethod
    def Test_Login_Page(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user07@getnada.com')

    def Test_Of_Filling_Password(self):
        user_password = LoginPage(self.driver)
        user_password.type_in_password('Test-1234')

    def Test_Click_Button(self):
        user_click = LoginPage(self.driver)
        user_click.click_on_the_button().click()



    @classmethod
    def tearDown(self):
        self.driver.quit()