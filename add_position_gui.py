import tkinter as tk
from func import create_new_position, generate_position_id, load_menu_content

## TWORZENIE NOWEJ POZYCJI - OKNO
def add_position(menu_label):
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
    create_pos_button = tk.Button(add_position_window, text="Utwórz pozycję",command=lambda:create_new_position(generate_position_id(load_menu_content()), name_new.get(), position_type.get(), price_new.get(), menu_label))
    create_pos_button.pack()