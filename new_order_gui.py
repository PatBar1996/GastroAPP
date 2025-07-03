import tkinter as tk
from administration_panel_gui import load_menu_content, format_menu
from func import generate_order_id, load_orders, create_order, Orders
from datetime import datetime
def view_new_order():

    ##LISTA OBJEKTÓW ZAMÓWIENIA
    new_order_objects = []
    new_order = Orders(generate_order_id(load_orders()), datetime.now(), new_order_objects, 0.0)
  #  order_price = 0.0
    ##ID dla nowego zamówienia
    new_order_id = generate_order_id(load_orders())

    ##WINDOW main
    new_order_panel = tk.Toplevel()
    new_order_panel.geometry("600x600")
    new_order_panel.title(f"Nowe zamówienie ID: {new_order_id}")
    new_order_panel.resizable(False, False)

    ##LISTBOX MENU POSITIONS
    menu_items = load_menu_content() ## lista obiektów
    menu_pos = [] ## pusta tablica
    for item in menu_items:
        menu_pos.append(item.position_name) ## dodaj position.name każdego obiektu do pustej tablicy
    menu_pos_list = tk.StringVar(value=menu_pos)
    menu_positions_listbox = tk.Listbox(new_order_panel, listvariable=menu_pos_list)
    menu_positions_listbox.pack()

    ##BUTTON >
    add_button = tk.Button(new_order_panel, text=">>", command=lambda:add_position(menu_positions_listbox,menu_items,order_content_listbox,new_order_objects, order_price))
    add_button.pack()
    ##BUTTON <
    delete_button = tk.Button(new_order_panel, text="<<", command=lambda:delete_position(order_content_listbox,new_order_objects))
    delete_button.pack()
    ##LISTBOX NEW ORDER content
    order_content_listbox = tk.Listbox(new_order_panel)
    order_content_listbox.pack()
    ##BUTTON Stwórz zamówienie
    create_order_button = tk.Button(new_order_panel, text="Stwórz zamówienie",command=lambda:create_order(new_order_objects, order_content_listbox, new_order_id, order_price))
    create_order_button.pack()

def add_position(menu_positions_listbox,menu_items,order_content_listbox,new_order_objects, order_price):
    selected_pos = menu_positions_listbox.curselection()
    ##menu_items[selected_pos[0]].position_name
    new_order_objects.append(menu_items[selected_pos[0]])
    order_price += menu_items[selected_pos[0]].position_price
    print(order_price)
    order_content_listbox.insert(tk.END, menu_items[selected_pos[0]].position_name)

def delete_position(order_content_listbox,new_order_objects):
    selected_pos = order_content_listbox.curselection()
    ##menu_items[selected_pos[0]].position_name
    new_order_objects.pop(selected_pos[0])
    order_content_listbox.delete(selected_pos[0])

#def calculate_price(order_content_listbox, order_price):



