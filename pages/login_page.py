from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@tabindex='0']"
    login_url = "https://scouts-test.futbolkolektyw.pl/login"
    expected_title = 'Scouts panel - sign in'
    # expected_q_text = 'Scouts Panel'
    # s_element_xpath = '//div/div[1]/h5'
    remind_element_xpath = "//div[1]/a"
    reminder_url = "https://scouts-test.futbolkolektyw.pl/en/remind"
    expected_reminder_title = 'Remind password'
    warning_sign_xpath = "//div[3]/span"
    expected_warning = 'Identifier or password invalid.'
    language_changer_xpath = "//ul[2]/div[1]/div[2]/span"

    #   "//a/text()"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def click_on_the_language(self):
        self.click_on_the_element(self.language_changer_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    """def check_Scouts_Panel_text(self, expected_text):
        self.assert_element_text(self.s_element_xpath, expected_text)"""

    def click_on_the_reminder(self):
        self.click_on_the_element(self.remind_element_xpath)

    def wait_for_button_to_be_clickable(self):
        self.wait_for_element_to_be_clickable(self.sign_in_button_xpath)

    def title_of_reminder(self):
        assert self.get_page_title(self.reminder_url) == self.expected_reminder_title


