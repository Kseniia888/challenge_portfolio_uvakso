import os
import time
import unittest
from selenium import webdriver

from pages.base_page import BasePage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage



class TestUncorrectLogin(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/login')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_warning_message(self):
        chek_login = LoginPage(self.driver)
        chek_login.title_of_page()
        chek_login.type_in_email('user@getnada.com')
        chek_login.type_in_password('Test-1234')
        chek_login.wait_for_button_to_be_clickable()
        chek_login.click_on_the_button()
        base_page = BasePage(self.driver)
        base_page.assert_element_text(self.driver, '//div[3]/span', 'Identifier or password invalid.')





        time.sleep(5)




    @classmethod
    def tearDown(self):
        self.driver.quit()