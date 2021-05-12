from AppiumFrameWork.base.BasePage import BasePage
from AppiumFrameWork.utilities import CustomLogger as cl


class LoginClass(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _login_button = 'com.code2lead.kwad:id/Login'
    _enter_email_field = "com.code2lead.kwad:id/Et4"
    _enter_password_field = "com.code2lead.kwad:id/Et5"
    _submit_login_button = "com.code2lead.kwad:id/Btn3"
    _wrong_credentials = "Wrong Credentials"
    _page_title = "Enter Admin"  # text
    _enter_text = "com.code2lead.kwad:id/Edt_admin"  # id
    _submit_button = "SUBMIT"  # text

    def click_login_button(self):
        self.clickElement(self._login_button, "id")
        cl.allureLogs("Clicked on Login Button")

    def enter_email(self, email):
        self.sendText(email, self._enter_email_field, "id")
        cl.allureLogs("Entered email")

    def enter_password(self, password):
        self.sendText(password, self._enter_password_field, "id")
        cl.allureLogs("Entered password")

    def click_on_submit_button(self):
        self.clickElement(self._submit_button, "text")
        cl.allureLogs("Submit Pressed")

    def click_on_submit_login_button(self):
        self.clickElement(self._submit_login_button, "id")
        cl.allureLogs("Pressed Login Button")

    def verify_wrong_credential(self):
        element = self.isDisplayed(self._wrong_credentials, "text")
        assert element
        cl.allureLogs("Element was found")

    def verify_admin_screen(self):
        admin_screen = self.isDisplayed(self._page_title, "text")
        assert admin_screen == "Enter Email"
        cl.allureLogs(f'Element {self._page_title} was found')

    def enter_admin_name(self, admin_name):
        self.sendText(admin_name, self._enter_text, "id")
        cl.allureLogs("entered admin name")