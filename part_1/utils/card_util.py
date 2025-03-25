from typing import Dict, Any
from dataclasses import dataclass
import requests
from part_1.constants import BASE_URL


@dataclass
class TrelloCardUtils:
    id_list: str
    card_name: str
    card_description: str
    auth_session: requests.Session
    base_url: str = BASE_URL

    def create_card(self)  -> Dict[str, Any]:

        payload = {
            "name": self.card_name,
            "desc": self.card_description,
            "idList": self.id_list,
        }

        response = self.auth_session.post(f"{BASE_URL}/1/cards", json=payload)
        response.raise_for_status()

        return response.json()
