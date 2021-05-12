import unittest
import pytest

from AppiumFrameWork.base.BasePage import BasePage
from AppiumFrameWork.pages.LoginPage import LoginClass
import AppiumFrameWork.utilities.CustomLogger as cl

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lc = LoginClass(self.driver)
        self.bp = BasePage(self.driver)

    @pytest.mark.run(order=1)
    def test_login_with_incorrect_datas(self):
        cl.allureLogs("App Opened")
        self.lc.click_login_button()
        self.lc.enter_email("test@example.com")
        self.lc.enter_password("123")
        self.lc.click_on_submit_login_button()
        self.lc.verify_wrong_credential()

    @pytest.mark.run(order=2)
    def test_login_with_confirm_datas(self):
        self.bp.keyCode(4)
        self.lc.click_login_button()
        self.lc.enter_email("admin@gmail.com")
        self.lc.enter_password("admin123")
        self.lc.click_on_submit_login_button()
        # self.lc.verify_wrong_credential()

    @pytest.mark.run(order=3)
    def test_enter_data_in_edit_box(self):
        self.lc.enter_admin_name('dupa')
        self.lc.click_on_submit_button()
    # @pytest.mark.run(order=1)
    # def test_open_login_form_site(self):
    #     self.lc.click_login_button()
        # self.lc.verifyContactPage()