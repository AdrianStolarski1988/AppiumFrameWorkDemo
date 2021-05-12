from AppiumFrameWork.base.BasePage import BasePage
from AppiumFrameWork.utilities import CustomLogger as cl

class ContactForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locator values
    _contactFromButton = "com.code2lead.kwad:id/ContactUs"  # id
    _pagetitle = "Contact Us form"  # text
    _enterName = "Enter Name"  # text
    _enterEmail = "Enter Email"  # text
    _enterAddress = "Enter Address"  # text
    _enterMobileNumber = "Enter Mobile No"  # index number
    _submitButton = "SUBMIT"  # text

    def clickContactFormButton(self):
        self.clickElement(self._contactFromButton, "id")
        cl.allureLogs("Clicked on Contact us From Button")

    def verifyContactPage(self):
        element = self.isDisplayed(self._pagetitle, "text")
        assert element == True
        cl.allureLogs("Element was found")

    def enterName(self):
        self.sendText("Code2Lead", self._enterName, "text")

    def enterEmail(self):
        self.sendText("abc@gmail.com", self._enterEmail, "text")

    def enterAddress(self):
        self.sendText("Kraków", self._enterAddress, "text")

    def enterMNumber(self):
        self.sendText("123123", self._enterMobileNumber, "text")

    def clickSubmitButton(self):
        self.clickElement(self._submitButton, "text")