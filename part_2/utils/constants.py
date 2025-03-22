import enum

class Constants(enum.Enum):
    USERNAME_SELECTOR = '#username'
    PASSWORD_SELECTOR = '#password'
    LOGIN_BUTTON_SELECTOR = '#login-button'
    LOGIN_SUBMIT_BUTTON_SELECTOR = '#login-submit'
    HOME_BUTTON_SELECTOR = '#home-nav-button'
    AUTH_SUBMIT_BUTTON_SELECTOR = '#mfa-promote-dismiss'
    TRELLO_BOARDS_SELECTOR = 'div[title="Моя доска Trello"]'
    TRELLO_NEW_CARD_SELECTOR = '[data-testid="list-add-card-button"]'
    TRELLO_ADD_CARD_NAME_SELECTOR = '[data-testid="list-card-composer-textarea"]'
    TRELLO_ADD_CARD_SELECTOR = '[data-testid="list-card-composer-add-card-button"]'
    CLICK_ON_CARD_SELECTOR = '[data-testid="card-name"]'
    MOVE_LIST_SELECTOR = '.WTF5k9ZC8MHUNi'

    CHOOSE_IN_LIST_SELECTOR = '[data-testid="DownIcon"]'
    # HAS_MOVE_CARD_ELEMENT_LIST_SELECTOR = 'h2.TzntopStGOcVjM:has-text("Перемещение карточки")'

    CHOOSE_VALUE_SELECTOR = 'div[class="value-container css-xo17ij"] div.css-1c8bys3-singleValue:has-text("В процессе")'

    DROPDOWN_SELECTOR = 'div[class="yMPj1pPmPFjeI1 css-1vrwmt7-control"]'

    MOVE_CARD_BUTTON_SELECTOR = '[data-testid="move-card-popover-move-button"]'

