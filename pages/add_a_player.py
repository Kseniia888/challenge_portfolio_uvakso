from pages.base_page import BasePage
import time


class AddAPlayer(BasePage):
    but_Players_xpath = "//span[contains(text(),'Add player')]"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"


    def click_on_the_span(self):
        self.click_on_the_element(self.but_Players_xpath)

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.add_player_url) == self.expected_title




