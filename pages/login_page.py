
from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@tabindex='0']"
    login_url = "https://scouts-test.futbolkolektyw.pl/login"
    expected_title = 'Scouts panel - sign in'
    #expected_q_text = 'Scouts Panel'
    s_element_xpath = '//div/div[1]/h5'



    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title


    """def check_Scouts_Panel_text(self, expected_text):
        self.assert_element_text(self.s_element_xpath, expected_text)"""













