from dotenv import load_dotenv
import os
import requests

load_dotenv() #loading API_key from .env
api_key = os.getenv("API_KEY")
api_url = "https://lxqogkicdmzcguqdmhaw.supabase.co"

headers = {
    "apikey": api_key,
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

class MenuPositions:
    def __init__(self, id, position_name, position_type, position_price):
        self.id = id
        self.position_name = position_name
        self.position_type = position_type
        self.position_price = position_price

    def __repr__(self):
        return f"<MenuPosition id={self.id} name={self.position_name} type={self.position_type} price={self.position_price}>"


def format_menu(menu_items):
    return "\n".join(f"ID [{item.id}] {item.position_name}: {item.position_price} zł" for item in menu_items)

def load_menu_content():
    response = requests.get(f"{api_url}/rest/v1/menu_positions?select=*&order=id.asc", headers=headers)
    if response.status_code == 200:
        data = response.json()
        menu_positions = [MenuPositions(**item) for item in data]
        return menu_positions
    else:
        print("Błąd ładowania danych: ", response.status_code, response.text)
        return []

print(load_menu_content())

