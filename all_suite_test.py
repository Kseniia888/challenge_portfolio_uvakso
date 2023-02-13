import unittest

from unittest.loader import makeSuite

from test_cases.adding_player_to_database import AddPlayerToBase
from test_cases.change_language import ChangeLanguage
from test_cases.checking_remind_password import TestRemindButton
from test_cases.chek_uncorrect_login import TestUncorrectLogin
from test_cases.sing_out import SingOut
from test_cases.framework import Test


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(AddPlayerToBase))
   test_suite.addTest(makeSuite(ChangeLanguage))
   test_suite.addTest(makeSuite(TestRemindButton))
   test_suite.addTest(makeSuite(TestUncorrectLogin))
   test_suite.addTest(makeSuite(SingOut))
   return test_suite


if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())