import enum


class CreateCardConstants(enum.Enum):
    TRELLO_BOARDS_SELECTOR = 'div[title="Моя доска Trello"]'
    TRELLO_NEW_CARD_SELECTOR = '[data-testid="list-add-card-button"]'
    TRELLO_ADD_CARD_NAME_SELECTOR = '[data-testid="list-card-composer-textarea"]'
    TRELLO_ADD_CARD_SELECTOR = '[data-testid="list-card-composer-add-card-button"]'
    CLICK_ON_CARD_SELECTOR = '[data-testid="card-name"]'
