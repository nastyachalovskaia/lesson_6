import enum


class DeleteCardConstants(enum.Enum):
    OPEN_OVERFLOW_MENU_HORIZONTAL_ICON_BUTTON_SELECTOR= 'button[aria-label="Меню"]'
    DELETE_CONFIRM_BUTTON_SELECTOR= 'button[aria-label="delete-confirm"]'
    DELETE_FROM_ARCHIVE_BUTTON_SELECTOR= 'text="Удалить"'
    MOVE_TO_ARCHIVE_ELEMENT_SELECTOR= '[data-testid="quick-card-editor-archive"]'
    ARCHIVE_BUTTON_IN_HORIZONTAL_MENU_SELECTOR = '[data-testid="ArchiveIcon"]'
    CLOSE_HORIZONTAL_MENU_SELECTOR = '[data-testid="board-menu-close-button"]'
