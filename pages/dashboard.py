import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/"

    def titele_of_page (self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title











    '''
    Scouts_Panel_xpath = "//header/div/h6"
    Main_page_xpath = "//ul[1]/div[1]/div[2]/span"
    Players_xpath = "//ul[1]/div[2]/div[2]/span"
    Language_xpath = "//ul[2]/div[1]/div[2]/span"
    Sing_out_xpath = "//ul[2]/div[2]/div[2]/span"
    Dev_team_contact_xpath = "//a[contains(@href, '://')]"
    Ania_Testerska1_link_xpath = "//div[3]/div/div/a[1]"
    Last_creater_player_xpath = "//div/div/h6[1]"
    Activity_xpath = "//div[3]/div/div/h2"
    count_of_player_number_xpath = "//div[1]/div/div/b"

    '''





