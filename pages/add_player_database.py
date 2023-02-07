import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.add_a_player import AddAPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.support.select import Select


class AddPlayerToDataBase(BasePage):
    email_xpath = "//input[@name = 'email']"
    name_xpath = "//input[@name = 'name']"
    surname_xpath = "//input[@name = 'surname']"
    phone_xpath = "//input[@name = 'phone']"
    weight_xpath = "//input[@name = 'weight']"
    height_xpath = "//input[@name = 'height']"
    age_xpath = "//input[@name = 'age']"
    leg_xpath = "//*[@id = 'mui-component-select-leg']"
    left_leg_xpath = "//li[@data-value='left'"
    right_leg_xpath = "//li[@data-value='right']"
    club_xpath = "//input[@name='club'"
    level_xpath = "//input[@name = 'level']"
    mainPosition_xpath = "//input[@name = 'mainPosition']"
    secondPosition_xpath = "//input[@name = 'secondPosition']"
    district_xpath = "//*[@id = 'mui-component-select-district']"
    district1_xpath = "//ul/li[1]"
    achievements_xpath = "//input[@name = 'achievements']"
    webLaczy_xpath = "//input[@name = 'webLaczy']"
    web90_xpath = "//input[@name = 'web90']"
    webFB_xpath = "//input[@name = 'webFB']"
    submit_button_xpath = "//button[@type = 'submit']"
    clear_button_xpath = "//button[2]/span[1]"
    add_language_button_xpath = "//div[15]/button/span[1]"
    add_link_button_xpath = "//div[19]/button/span[1]"
    required_paragraph_xpath = "//div/p/text()"
    required_inputs_xpath = "//div/p/../div/input"
    input_type_text_xpath = "//input[@type = 'text']"

    def fill_in_name(self):

        self.field_send_keys(self.email_xpath, 'email@email')
        self.field_send_keys(self.name_xpath, 'Name Test')
        self.field_send_keys(self.surname_xpath, 'Surname Test')
        self.field_send_keys(self.phone_xpath, '999 999 999')
        self.field_send_keys(self.weight_xpath, '85')
        self.field_send_keys(self.height_xpath, '185')
        self.field_send_keys(self.age_xpath, '15.12.1992')
        self.click_on_the_element(self.leg_xpath)
        self.click_on_the_element(self.right_leg_xpath)
        self.field_send_keys(self.club_xpath, 'Test')
        self.field_send_keys(self.level_xpath, 'Test')
        self.field_send_keys(self.mainPosition_xpath, 'Main position test')
        self.field_send_keys(self.secondPosition_xpath, 'Test')
        self.click_on_the_element(self.district_xpath)
        self.click_on_the_element(self.district1_xpath)
        self.field_send_keys(self.achievements_xpath)


        self.click_on_the_element(self.submit_button_xpath)






    """def fill_in_inputs_type_text(self, input):
        self.field_send_keys(self.input_type_text_xpath, input)"""






"""def check_type_of_input(self):
      assert self.get_element_type(self.input_type_text_xpath) == self.required_inputs_xpath"""
