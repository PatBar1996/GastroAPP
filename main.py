from libraries import tk
import os
from administration_panel_gui import view_administration_panel
from orders_panel_gui import view_orders

##TODO
## ZROBIĆ ZLICZANIE ORDER PRICE, DOKOŃCZYĆ DATA W STWÓRZ ZAMÓWIENIE, PUŚCIĆ ZAPYTANIE

##PANEL GŁÓWNY APP
root = tk.Tk()
root.title("Gastronomia - Panel Główny")
root.geometry("500x500")

menu_edit_button = tk.Button(root, text="Zarządzaj MENU", command=view_administration_panel)
menu_edit_button.pack()

add_order_button = tk.Button(root, text="Zamówienia", command=view_orders)
add_order_button.pack()


root.mainloop()