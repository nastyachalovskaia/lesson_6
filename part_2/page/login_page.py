from part_2.page.base_page import BasePage
from part_2.utils.constants import *


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'login'

    def login(self, username, password):
        self.navigate_to()
        self.wait_for_selector_and_fill(Constants.USERNAME_SELECTOR.value, username)
        self.wait_for_selector_and_click(Constants.LOGIN_SUBMIT_BUTTON_SELECTOR.value)
        self.wait_for_selector_and_fill(Constants.PASSWORD_SELECTOR.value, password)
        self.wait_for_selector_and_click(Constants.LOGIN_SUBMIT_BUTTON_SELECTOR.value)
