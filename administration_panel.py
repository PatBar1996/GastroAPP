from libraries import tk
from func import load_menu_content, MenuPositions, format_menu, add_position

## view administration panel window
def view_administration_panel():
    administration_panel = tk.Toplevel()
    administration_panel.geometry("500x300")
    administration_panel.title("GastroAPP - Panel Administracyjny")

    ##ADMINISTRATION PANEL WIDGETS
    ##LABEL Zawartość Menu
    menu_items = load_menu_content()
    formatted_text = format_menu(menu_items)
    menu_label = tk.Label(administration_panel, text=formatted_text)
    menu_label.pack()

    ##BUTTON Dodaj Pozycję
    add_button = tk.Button(administration_panel, text="Dodaj pozycję", command=add_position)
    add_button.pack()

    ##BUTTON Edytuj Pozycję
    edit_button = tk.Button(administration_panel, text="Edytuj pozycję", command=None)
    edit_button.pack()
    ##BUTTON Usuń Pozycję
    delete_button = tk.Button(administration_panel, text="Usuń pozycję", command=None)
    delete_button.pack()