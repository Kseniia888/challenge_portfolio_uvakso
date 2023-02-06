import os
import time
import unittest

from selenium import webdriver
from pages.base_page import BasePage
from pages.add_a_player import AddAPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class AddPlayerToDataBase(BasePage):
    email_xpath = "//input[@name = 'email']"
    name_xpath = "//input[@name = 'name']"
    surname_xpath = "//input[@name = 'surname']"
    phone_xpath = "//input[@name = 'phone']"
    weight_xpath = "//input[@name = weight]"
    height_xpath = "//input[@name = 'height']"
    age_xpath = "//input[@name = 'age']"
    leg_xpath = "//*[@id = 'mui-component-select-leg']"
    club_xpath = "//input[@name='club'"
    level_xpath = "//input[@name = 'level']"
    mainPosition_xpath = "//input[@name = 'mainPosition']"
    secondPosition_xpath = "//input[@name = 'secondPosition']"
    district_xpath = "//*[@id = 'mui-component-select-district']"
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

    def fill_inn_required_inputs(self):








