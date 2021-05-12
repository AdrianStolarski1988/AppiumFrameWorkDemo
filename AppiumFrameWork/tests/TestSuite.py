import unittest
from AppiumFrameWork.tests.LoginPageTest import LoginPage
from AppiumFrameWork.tests.ContactUsFormTest import TestContactFormTest


gt = unittest.TestLoader().loadTestsFromTestCase(LoginPage)
cf = unittest.TestLoader().loadTestsFromTestCase(TestContactFormTest)


regressionTest = unittest.TestSuite([cf, gt])

unittest.TextTestRunner(verbosity=1).run(regressionTest)