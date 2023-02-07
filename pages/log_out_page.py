from pages.base_page import BasePage

class LogOut(BasePage):
    sing_out_button_xpath = "//span[text()='Sign out']"


    def sing_out(self):
        self.click_on_the_element(self.sing_out_button_xpath)