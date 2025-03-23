import time

from part_2.page.base_page import BasePage
from part_2.utils.move_card_constants import *
from part_2.utils.delete_card_constants import *
from part_2.utils.create_card_constants import *

class TrelloPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ''

    EXPECTED_URL = "https://trello.com/"
    CARD_VALUE = f"[@etoznado] Тестовая карточка {int(time.time())}"

    def create_card(self):
        self.wait_for_load()
        self.wait_for_selector_and_click(CreateCardConstants.TRELLO_BOARDS_SELECTOR.value)
        self.wait_for_exact_url("https://trello.com/**")
        self.assert_to_have_url_with_re(self.EXPECTED_URL)
        self.wait_for_selector_and_click(CreateCardConstants.TRELLO_NEW_CARD_SELECTOR.value)
        self.wait_for_selector_and_fill(CreateCardConstants.TRELLO_ADD_CARD_NAME_SELECTOR.value, self.CARD_VALUE)
        self.wait_for_selector_and_click(CreateCardConstants.TRELLO_ADD_CARD_SELECTOR.value)

    def move_card(self):
        created_card_name = self.CARD_VALUE
        self.wait_for_selector_and_click_right_click(f'text={created_card_name}')
        self.wait_for_selector_and_click(MoveCardConstants.MOVE_CARD_BUTTON_SELECTOR.value)
        self.assert_element_is_visible(MoveCardConstants.HAS_MOVEMENT_CARD_HEADER_SELECTOR.value)
        # пробую подвинуть мешающее окно с надписью "Моя доска Trello"
        self.wait_for_selector_and_click(MoveCardConstants.PLACE_TO_CLICK_TO_CHANGE_FOCUS_SELECTOR.value) # клик на пустое место
        self.assert_element_is_visible(MoveCardConstants.MOVEMENT_LIST_DESTINATION_SELECTOR.value) # это нужный селектор для вызова вариантов перемещения из списка
        self.wait_for_selector_and_click(MoveCardConstants.MOVEMENT_LIST_DESTINATION_SELECTOR.value)


    # def delete_card(self):
    #     # сперва хочу положить карточку в архив
    #     created_card_name = self.CARD_VALUE  # ссылаюсь на только что созданную карточку
    #     self.wait_for_selector_and_click_right_click(f'text={created_card_name}')
    #     self.wait_for_selector_and_click(DeleteCardConstants.MOVE_TO_ARCHIVE_ELEMENT_SELECTOR.value)
    #
    #     # попытка открыть меню справа через три точки
    #     self.wait_for_selector_and_click(DeleteCardConstants.OPEN_OVERFLOW_MENU_HORIZONTAL_ICON_BUTTON_SELECTOR.value)
    #     self.wait_for_selector_and_click(DeleteCardConstants.ARCHIVE_BUTTON_IN_HORIZONTAL_MENU_SELECTOR.value)
    #     self.wait_for_selector_and_click(DeleteCardConstants.DELETE_FROM_ARCHIVE_BUTTON_SELECTOR.value)
    #     self.wait_for_selector_and_click(DeleteCardConstants.DELETE_CONFIRM_BUTTON_SELECTOR.value)
















