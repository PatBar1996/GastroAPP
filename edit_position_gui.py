import tkinter as tk
import tkinter.messagebox as messagebox
from func import update_position, MenuPositions


##EDIT POSITION WINDOW
def edit_position(edited_position,menu_label):

    edit_window = tk.Toplevel()
    edit_window.geometry("300x300")
    edit_window.title(f"Edycja dla ID: {edited_position.id}")
    id_label = tk.Label(edit_window, text=f"ID: {edited_position.id} ")
    id_label.pack()
    name_label = tk.Label(edit_window, text="Nazwa pozycji:")
    name_label.pack()
    name_var = tk.StringVar()
    new_name = tk.Entry(edit_window, textvariable=name_var)
    new_name.insert(0, edited_position.position_name)
    new_name.pack()
    newtype_label = tk.Label(edit_window, text="Rodzaj pozycji:")
    newtype_label.pack()
    position_type = tk.StringVar(edit_window)
    position_type.set(edited_position.position_type)
    new_type = tk.OptionMenu(edit_window, position_type, "food","drink","snack","other")
    new_type.pack()
    price_label = tk.Label(edit_window, text="Cena pozycji:")
    price_label.pack()
    new_price = tk.Entry(edit_window)
    new_price.insert(0, edited_position.position_price)
    new_price.pack()
    apply_button = tk.Button(edit_window, text="Zatwierdź zmiany", command=lambda: update_position(MenuPositions(edited_position.id, name_var.get(), position_type.get(), new_price.get()), menu_label,edit_window))
    apply_button.pack()