import allure
from playwright.sync_api import sync_playwright

from part_2.page.base_page import BasePage


class HomePage(BasePage):
    HOME_URL_ATLASSIAN = "https://home.atlassian.com"
    CLOSE_MODAL_WINDOW = 'div.sc-fkyLDJ.jgJNIO button.what-is-atlas-button.css-1ak9fcm >> span.css-178ag6o:has-text("Закрыть")'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ''

    @allure.step("Opening the home page Atlassian")
    def direct_to_trello(self):
        self.wait_for_load()
        self.wait_for_exact_url("https://home.atlassian.com/**")
        self.assert_to_have_url_with_re(self.HOME_URL_ATLASSIAN)
        self.wait_for_selector_and_click(self.CLOSE_MODAL_WINDOW)
        self.wait_for_selector_and_click('div.css-1r14e9v >> text="Trello"')
        self.wait_for_exact_url("https://trello.com/")
        self.assert_to_have_url_with_re("https://trello.com/")



