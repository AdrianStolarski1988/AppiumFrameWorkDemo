import unittest
import pytest

from AppiumFrameWork.pages.ContactUsFormPage import ContactForm
import AppiumFrameWork.utilities.CustomLogger as cl

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TestContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)

    @pytest.mark.run(order=5)
    def test_enter_data_in_form(self):
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMNumber()
        self.cf.clickSubmitButton()

    @pytest.mark.run(order=4)
    def test_open_contact_form(self):
        self.cf.clickContactFormButton()
        self.cf.verifyContactPage()