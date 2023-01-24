from pages.base_page import BasePage

class Match_form (BasePage):
   Input_my_team_xpath = "//input[@name='myTeam']"
   Input_enemy_team_team_xpath = "//input[@name='enemyTeam']"
   inscription_my_team_xpath =  "//div[1]/div/label"
   match_at_home_radi_but_xpath = '// input[ @ value = "true"]'
   match_out_home_radi_but_xpath = '// input[ @ value = "false"]'
   button_submit_xpath = '//button[@type="submit"]'
   button_clear_xpath = '//div[3]/button[2]'
   date_input_xpath = '//input[@type="date"]'
   Adding_match_player_abc_Makowski_xpath= '//form/div[1]/div/span'
   lable_Raiting_xpath = '//div[13]/div/label'





