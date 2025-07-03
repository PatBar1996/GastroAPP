import tkinter as tk
from func import load_orders, Orders #format_orders
from new_order_gui import view_new_order

def view_orders():
    ##WINDOW main
    orders_panel = tk.Toplevel()
    orders_panel.geometry("600x600")
    orders_panel.resizable(False, False)

    ## WCZYTANIE ZAMÓWIEŃ I PRZYPISANIE DO LISTBOX
    orders = load_orders()
    formatted_orders_list = format_orders_list(orders)
    print(formatted_orders_list[0])
    ordersvar = tk.StringVar(value=formatted_orders_list)
    print(formatted_orders_list)
    ##LABEL Aktualne zamówienia
    active_orders = tk.Label(orders_panel,text=f"Aktywne zamówienia:")
    active_orders.pack()
    ## LISTBOX
    listbox_orders = tk.Listbox(orders_panel, height=10, listvariable=ordersvar)
    listbox_orders.pack()
    ## BUTTON : Wczytaj zamówienie
    read_order = tk.Button(orders_panel, text="Podgląd zamówienia", command=lambda:selected_order(listbox_orders, orders,choiced_order))
    read_order.pack()
    ## LABEL
    choiced_order = tk.Label(orders_panel,text="ZAWARTOŚĆ\nWYBRANEGO MENU")
    choiced_order.pack()
    ## BUTTON Stwórz Zamówienie
    create_order_button = tk.Button(orders_panel, text="Stwórz zamówienie", command=view_new_order)
    create_order_button.pack()

def format_orders_list(orders):
    orders_list = []
    for order in orders:
        orders_list.append(f"Zamówienie {order.order_id}")
    return orders_list

def selected_order(listbox_orders, orders,choiced_order):
    selected_order = listbox_orders.curselection()
    order_positions_text = ""
    print(orders[selected_order[0]].order_content)
    for order_position in orders[selected_order[0]].order_content:
        order_positions_text += f"- {order_position}\n"

    order_text = f"Zamówienie nr {orders[selected_order[0]].order_id}\n{order_positions_text}\nKoszt: {orders[selected_order[0]].order_price} zł"
    choiced_order.config(text=order_text)
    return orders[selected_order[0]]
