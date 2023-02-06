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





