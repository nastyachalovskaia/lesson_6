import os
import time

from dotenv import load_dotenv
import pytest
import requests

from part_1.constants import BASE_URL, HEADERS
from part_1.utils.board_util import TrelloBoard
from part_1.utils.card_util import TrelloCardUtils

load_dotenv() # загружает переменные из файлика .env

@pytest.fixture(scope="session")
def trello_auth_session():
    session = requests.Session()

    api_key = os.getenv("TRELLO_API_KEY")
    api_token = os.getenv("TRELLO_TOKEN")

    if not api_key or not api_token:
        pytest.fail("Не найдены TRELLO_API_KEY или TRELLO_TOKEN в .env")

    session.params = {
        "key": api_key,
        "token": api_token
    }

    response = session.get(f"{BASE_URL}/1/members/me")
    assert response.status_code == 200, "Ошибка авторизации"

    return session

@pytest.fixture(scope="session")
def trello_get_list_id(trello_auth_session):

    trello_board = TrelloBoard(trello_auth_session)
    board_id = trello_board.get_board_id()
    assert board_id, "ID доски не должно быть пустым"

    id_list = trello_board.get_list_id()
    assert id_list, "ID списка не должно быть пустым"

    return id_list

@pytest.fixture(scope="session")
def trello_create_card(trello_auth_session,trello_get_list_id):
    id_list = trello_get_list_id
    card_name = f"[@etoznado] Тестовая карточка {int(time.time())}"
    card_desc = f"Описание карточки {int(time.time())}"
    trello_card = TrelloCardUtils(id_list, card_name, card_desc,auth_session=trello_auth_session)

    new_card = trello_card.create_card()
    assert new_card is not None, "Не удалось создать карточку"
    assert isinstance(new_card, dict)

    created_card = {
        'card': new_card,
        'desc': card_desc,
        'name': card_name
    }

    return created_card


@pytest.fixture
def delete_trello_card(trello_auth_session):
    def _delete_trello_card(card_id):
        response = trello_auth_session.delete(f"{BASE_URL}/1/cards/{card_id}")
        assert response.status_code == 200, f"Ошибка при удалении карточки с ID {card_id}"
        return True

    return _delete_trello_card

@pytest.fixture(scope='session')
def trello_card_data(trello_create_card):
    return {
        'id': trello_create_card['card'].get('id'),
        'name': trello_create_card['card'].get('name'),
        'desc': trello_create_card['card'].get('desc'),
        'idList': trello_create_card['card'].get('idList')
    }