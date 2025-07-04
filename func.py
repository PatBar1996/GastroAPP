from dotenv import load_dotenv
import os
import requests
import tkinter as tk
import tkinter.messagebox as messagebox
from administration_panel_gui import *
from datetime import datetime
#from new_order_gui import *

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


class Orders:
    def __init__(self, order_id, order_time, order_content, order_price):
        self.order_id = order_id
        self.order_time = order_time
        self.order_content = order_content
        self.order_price = order_price


    def __repr__(self):
        return f"<Order id={self.order_id} time={self.order_time} content={self.order_content} price={self.order_price}>"

    def __str__(self):
        return f"Zamówienie [{self.order_id}]\n[{self.order_time}]\n{self.order_content}\nKwota zamówienia: {self.order_price} zł"

    def format_order_content(self):
        print(self.order_content[0])

def update_menu_label(menu_label):
    menu_items = load_menu_content()
    formatted_text = format_menu(menu_items)
    menu_label.config(text=formatted_text)

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

## POBIERANIE AKTUALNYCH ZAMÓWIEŃ Z SUPABASE
def load_orders():
    response = requests.get(f"{api_url}/rest/v1/orders?select=*&order=order_id.asc", headers=headers)
    if response.status_code == 200:
        data = response.json()
        orders_list = [Orders(**order) for order in data]
        return orders_list
    else:
        print("Błąd ładowania danych: ", response.status_code, response.text)
        return []

## FORMATOWANIE ZAWARTOŚCI AKTUALNYCH ZAMÓWIEŃ
# def format_orders(orders_list):
#     print(orders_list)
#     return "\n".join(f"Zamówienie [{orders_list[0].order_id}] ({orders_list[0].order_time}):\n{orders_list[0].order_content}\nKwota zamówienia: {orders_list[0].order_price} zł" for order in orders_list)

## GENERATOR ID DLA NOWEJ POZYCJI MENU (ID ostatniego elementu listy + 1)
def generate_position_id(menu_positions):
    return menu_positions[-1].id+1

## GENERATOR ID DLA NOWEJ POZYCJI ZAMÓWIENIE (ID ostatniego elementu listy + 1)
def generate_order_id(orders_list):
    return orders_list[-1].order_id+1

##tworzenie obiektu z wiersza MenuPositions
def get_object(object_id):
    response = requests.get(f"{api_url}/rest/v1/menu_positions?id=eq.{object_id}", headers=headers)
    data = response.json()
    object = MenuPositions(**data[0]) ##tworzenie obiektu z elementu [0] listy
    return object




## WYSYŁKA NOWEJ POZYCJI
def create_new_position(id, name, position_type, price, menu_label):
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
            menu_label.config(text=update_menu_label(menu_label))

            if response.status_code == 201:
                print(f"Nowa pozycja przesłana do SUPABASE ({data})")
                return new_menu_position

            else:
                print(f"Błąd przesyłu pozycji: {response.status_code}, {response.text}!")
                return None

    except ValueError:
        tk.messagebox.Message(title="BŁĄD", message="Błąd danych").show()
        return None

def update_position(updated_menu_position, menu_label,edit_window):
    try:
        if (
                not updated_menu_position.position_name.strip() or
                updated_menu_position.position_price is None or
                float(updated_menu_position.position_price) <= 0 or
                updated_menu_position.position_type not in ["food","drink", "snack", "other"]
        ):
            tk.messagebox.Message(parent=edit_window,title="BŁĄD", message="Błąd danych1").show()
        else:
            data = {
                "id": updated_menu_position.id,
                "position_type": updated_menu_position.position_type,
                "position_name": updated_menu_position.position_name,
                "position_price": updated_menu_position.position_price,
            }
            print(data)
            response = requests.patch(f"{api_url}/rest/v1/menu_positions?id=eq.{updated_menu_position.id}", headers=headers,json=data)
            print("Status:", response.status_code)
            print("Response:", response.text)
            update_menu_label(menu_label)
            return response

    except ValueError:
        tk.messagebox.Message(parent=edit_window,title="BŁĄD", message="Błąd danych2").show()

def create_order(new_order_objects, order_content_listbox, new_order_id):
    order_content = []
    for object in new_order_objects:
        order_content.append(object.position_name)
    data = {
        "order_id": new_order_id,
        "order_time": datetime.now(),
        "order_content": order_content,
        "order_price": order_price

    }
    response = requests.post(f"{api_url}/rest/v1/orders", json=xxx, headers=headers)





def delete_position(administration_panel, position_id,menu_label):
    products_list = load_menu_content()
    operation_ask = tk.messagebox.askquestion(
        parent=administration_panel,
        title=f"Potwierdź operację",
        message=f"Czy na pewno chcesz usunąć\npozycję o ID {position_id}?")

    if operation_ask == "yes":
        response = requests.delete(f"{api_url}/rest/v1/menu_positions?id=eq.{position_id}", headers=headers)
        update_menu_label(menu_label)

        tk.messagebox.showinfo(
            parent=administration_panel,
            title="Sukces!",
            message=f"Produkt o ID {position_id}\nzostał pomyślnie usunięty!"
        )



