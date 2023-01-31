from pages.base_page import BasePage


class AddAPlayer(BasePage):
    but_Players_xpath = "//span[contains(text(),'Add player')]"


    def click_on_the_span(self):
        self.click_on_the_element(self.but_Players_xpath)




