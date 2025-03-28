import enum


class MoveCardConstants(enum.Enum):
    CHOOSE_IN_PROGRESS_VALUE_SELECTOR = 'div[role="option"]:has-text("В процессе") li'

    MOVE_CARD_BUTTON_SELECTOR = '[data-testid="quick-card-editor-move"]'
    HAS_MOVEMENT_CARD_HEADER_SELECTOR = 'h2.TzntopStGOcVjM:has-text("Перемещение карточки")'
    PLACE_TO_CLICK_TO_CHANGE_FOCUS_SELECTOR = 'div[class="q2PzD_Dkq1FVX3 pt-0"]'
    MOVEMENT_LIST_DESTINATION_SELECTOR = '[data-testid="move-card-popover-select-list-destination"] [aria-label="open"]'
    MOVE_BUTTON_IN_OTHER_COLUMN_SELECTOR = '[data-testid="move-card-popover-move-button"]'
