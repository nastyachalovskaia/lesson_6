import pytest
import requests

from api_trello_testing.constants import BASE_URL, HEADERS


@pytest.fixture(scope="session")
def auth_session():
    """Создаёт сессию с авторизацией и возвращает объект сессии."""
    session = requests.Session()
    session.headers.update(HEADERS)

    auth_response = session.get(f"{BASE_URL}/login", json={"username": "a3371188@gmail.com", "password": "Scra[chyE%esX2"})
    assert auth_response.status_code == 200, "Ошибка авторизации, статус код не 200"
    token = auth_response.json().get("token")
    assert token is not None, "Токен не найден в ответе"

    session.headers.update({"Cookie": f"token={token}"})
    return session

@pytest.fixture()
def create_card(auth_session):

    create_card = auth_session.post(f"{BASE_URL}/cards", json={})
    assert create_card.status_code == 200
    card_id = create_card.json().get("idList")
    assert card_id is not None, "ID карточки не найден в ответе"

    return card_id