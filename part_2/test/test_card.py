import json

from part_2.page.login_page import LoginPage
from part_2.page.home_page_atlassian import HomePage
from part_2.page.trello_page import TrelloPage


def test_trello_cards_operations(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    home_page = HomePage(page)
    trello_page = TrelloPage(page)

    login_page.login(USERNAME, PASSWORD)
    home_page.direct_to_trello()
    trello_page.create_card()
    trello_page.move_card()
    trello_page.delete_card()

with open("part_2/config.json") as f:
    config = json.load(f)

USERNAME = config["trello"]["username"]
PASSWORD = config["trello"]["password"]