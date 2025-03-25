from dataclasses import dataclass
import requests

from part_1.constants import BASE_URL


@dataclass
class TrelloBoard:
    auth_session: requests.Session
    base_url: str = BASE_URL

    def get_board_id(self, board_name: str = "Моя доска Trello") -> str:
        response = self.auth_session.get(f"{self.base_url}/1/members/me/boards")
        response.raise_for_status()

        for board in response.json():
            if board["name"] == board_name:
                if board_id := board.get("id"):
                    return board_id
        raise ValueError(f"Доска '{board_name}' не найдена")

    def get_list_id(self) -> str:
        board_id = self.get_board_id()

        get_lists = self.auth_session.get(
            f"{self.base_url}/1/boards/{board_id}/lists"
        )

        list_name = "Нужно сделать"
        for lst in get_lists.json():
            if lst["name"] == list_name:
                return lst["id"]
        raise ValueError(f"Список '{list_name}' не найден")