import time

from playwright.async_api import expect

from part_2.page.base_page import BasePage
from part_2.utils.constants import Constants


class TrelloPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ''

    EXPECTED_URL = "https://trello.com/"
    CARD_VALUE = "[@etoznado] Контрольный экзамен блок 6"


    def create_card(self):
        self.wait_for_load()
        self.wait_for_selector_and_click(Constants.TRELLO_BOARDS_SELECTOR.value)
        self.wait_for_exact_url("https://trello.com/**")
        self.assert_to_have_url_with_re(self.EXPECTED_URL)
        self.wait_for_selector_and_click(Constants.TRELLO_NEW_CARD_SELECTOR.value)
        self.wait_for_selector_and_fill(Constants.TRELLO_ADD_CARD_NAME_SELECTOR.value, self.CARD_VALUE)
        self.wait_for_selector_and_click(Constants.TRELLO_ADD_CARD_SELECTOR.value)

    def move_card(self):
        self.wait_for_selector_and_click(Constants.CLICK_ON_CARD_SELECTOR.value)
        self.wait_for_exact_url("https://trello.com/**")
        self.assert_to_have_url_with_re("https://trello.com/c")

        self.wait_for_selector_and_click(Constants.MOVE_LIST_SELECTOR.value)
        self.wait_for_selector_and_click(Constants.CHOOSE_IN_LIST_SELECTOR.value)
        self.wait_for_selector_and_click(Constants.DROPDOWN_SELECTOR.value)


        # self.change_column()
        # self.wait_for_selector_and_click(Constants.MOVE_CARD_BUTTON_SELECTOR.value)

    def change_column(self):
        in_progress_element = self.wait_for_selector_and_click(Constants.CHOOSE_VALUE_SELECTOR.value)
        in_progress_element.wait_for(state='visible', timeout=60000)
        in_progress_element.click()
















