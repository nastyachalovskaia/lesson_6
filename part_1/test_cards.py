import time

from part_1.constants import BASE_URL


def test_create_card(trello_auth_session, trello_get_list_id, trello_create_card, trello_card_data, delete_trello_card):
    id_list = trello_get_list_id

    card_data = trello_card_data

    assert card_data['id'], "Отсутствует ID карточки"
    assert card_data['name'] == trello_create_card['name'], f"Название должно быть '{trello_create_card['name']}'"
    assert card_data['desc'] == trello_create_card['desc'], f"Описание должно быть '{trello_create_card['desc']}'"
    assert card_data['idList'] == id_list, f"Карточка должна быть в списке {id_list}"

    is_deleted = delete_trello_card(card_data['id'])  # Получаем результат удаления
    assert is_deleted is True, "Карточка не была удалена"

def test_change_card(trello_auth_session, trello_get_list_id, trello_card_data):
    id_list = trello_get_list_id

    updated_card_data = trello_card_data.copy()
    updated_card_data.update({
        "id": trello_card_data['id'],
        "name": f"updated_card {int(time.time())}",
        "desc": "Новое описание",
        "idList": id_list
    })
    update_card = trello_auth_session.put(f"{BASE_URL}/1/cards/{trello_card_data.get('id')}", json=updated_card_data)
    assert update_card.status_code == 200, "Ошибка при обновлении данных карточки"
