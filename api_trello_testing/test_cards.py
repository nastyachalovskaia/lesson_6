from api_trello_testing.constants import BASE_URL


def test_create_booking(self):
    auth = create_booking

    get_booking = auth_session.get(f"{BASE_URL}")
    assert get_booking.status_code == 200, "Ошибка при получении данных бронирования"

    booking_data_response = get_booking.json()
    assert booking_data_response['firstname'] == booking_data['firstname'], "Имя не совпадает с заданным"
    assert booking_data_response['lastname'] == booking_data['lastname'], "Фамилия не совпадает с заданной"
    assert booking_data_response['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной"
    assert booking_data_response['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"
    assert booking_data_response['bookingdates']['checkin'] == booking_data['bookingdates'][
        'checkin'], "Дата заезда не совпадает"
    assert booking_data_response['bookingdates']['checkout'] == booking_data['bookingdates'][
        'checkout'], "Дата выезда не совпадает"

    delete_booking(auth)

    get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{auth}")
    assert get_deleted_booking.status_code == 404, "Букинг не был удален"