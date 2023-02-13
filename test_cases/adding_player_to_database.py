import os
import time
import unittest

from selenium import webdriver
from pages.add_player_database import AddPlayerToDataBase
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from test_cases.adding_player import TestAddingPage


class AddPlayerToBase(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/login')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player_to_data(self):
        TestAddingPage.test_add_player_into_the_system(self)
        user_adding = AddPlayerToDataBase(self.driver)
        user_adding.fill_in_name()
        time.sleep(3)
    #    base_page = BasePage(self.driver)
    #    base_page.assert_element_text(self.driver, '//*[@id="__next"]/div[2]/div', 'Added player.')






    """  player_add = AddPlayerToDataBase(self.driver)
      player_add.title_of_page()"""

    def tearDown(self):
        self.driver.quit()
