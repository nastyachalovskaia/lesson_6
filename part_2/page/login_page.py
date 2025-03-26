import allure

from part_2.page.base_page import BasePage
from part_2.utils.auth_constants import *


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'login'

    @allure.step("Opening the login page")
    def login(self, username, password):
        self.navigate_to()
        self.wait_for_selector_and_fill(AuthConstants.USERNAME_SELECTOR.value, username)
        self.wait_for_selector_and_click(AuthConstants.LOGIN_SUBMIT_BUTTON_SELECTOR.value)
        self.wait_for_selector_and_fill(AuthConstants.PASSWORD_SELECTOR.value, password)
        self.wait_for_selector_and_click(AuthConstants.LOGIN_SUBMIT_BUTTON_SELECTOR.value)
