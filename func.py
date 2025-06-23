from dotenv import load_dotenv
import os
import requests
import tkinter as tk
import tkinter.messagebox as messagebox

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

## FORMATOWANIE ZAWARTOŚCI AKTUALNEGO MENU
def format_menu(menu_items):
    return "\n".join(f"ID [{item.id}] {item.position_name}: {item.position_price} zł" for item in menu_items)

## POBIERANIE ZAWARTOŚCI AKTUALNEGO MENU Z SUPABASE
def load_menu_content():
    response = requests.get(f"{api_url}/rest/v1/menu_positions?select=*&order=id.asc", headers=headers)
    if response.status_code == 200:
        data = response.json()
        menu_positions = [MenuPositions(**item) for item in data]
        return menu_positions
    else:
        print("Błąd ładowania danych: ", response.status_code, response.text)
        return []

## GENERATOR ID DLA NOWEJ POZYCJI MENU (ID ostatniego elementu listy + 1)
def generate_position_id(menu_positions):
    return menu_positions[-1].id+1

def create_new_position(id, name, position_type, price):
    try:
        if (
                not name.strip() or
                price is None or
                int(price) <= 0 or
                position_type not in ["food", "drink", "snack", "other"]
        ):
            tk.messagebox.Message(title="BŁĄD", message="Błąd danych").show()
            print("Błąd")
            return None
        else:
            ##Utworzenie obiektu klasy MenuPositions
            new_menu_position = MenuPositions(id,name,position_type,price)
            ##Sformatowanie data pod wysyłkę
            data = {"id": new_menu_position.id, "position_type": new_menu_position.position_type, "position_name": new_menu_position.position_name, "position_price": new_menu_position.position_price}
            response = requests.post(f"{api_url}/rest/v1/menu_positions", json=data, headers=headers)

            if response.status_code == 201:
                print(f"Nowa pozycja przesłana do SUPABASE ({data})")
                return new_menu_position

            else:
                print(f"Błąd przesyłu pozycji: {response.status_code}, {response.text}!")
                return None

    except ValueError:
        tk.messagebox.Message(title="BŁĄD", message="Błąd danych").show()
        return None


def add_position():
    ##OKNO Dodaj Nową Pozycję
    add_position_window = tk.Toplevel()
    add_position_window.geometry("300x300")
    ##TEXT Nazwa Pozycji
    textname_new = tk.Label(add_position_window, text="Nazwa pozycji")
    textname_new.pack()
    ##ENTRY Nazwa Pozycji
    name_new = tk.Entry(add_position_window)
    name_new.pack()
    ##TEXT Rodzaj Pozycji
    texttype_new = tk.Label(add_position_window, text="Rodzaj pozycji")
    texttype_new.pack()
    ##OPTIONMENU Rodzaj Pozycji
    ##wartość
    position_type = tk.StringVar(add_position_window)
    position_type.set("Rodzaj pozycji")
    ##optionmenu
    type_new = tk.OptionMenu(add_position_window, position_type, "food", "drink", "snack", "other")
    type_new.pack()
    ##TEXT Cena Pozycji
    textprice_new = tk.Label(add_position_window,text="Cena pozycji")
    textprice_new.pack()
    ##ENTRY Cena Pozycji
    price_new = tk.Entry(add_position_window)
    price_new.pack()
    ##BUTTON Utwórz Pozycję
    create_pos_button = tk.Button(add_position_window, text="Utwórz pozycję",command=lambda:create_new_position(generate_position_id(load_menu_content()), name_new.get(), position_type.get(), price_new.get()))
    create_pos_button.pack()


