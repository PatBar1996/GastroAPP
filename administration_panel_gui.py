from libraries import tk
from func import load_menu_content, MenuPositions, format_menu, get_object, delete_position, update_menu_label
from add_position_gui import add_position
from edit_position_gui import edit_position

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
    add_button = tk.Button(administration_panel, text="Dodaj pozycję", command=lambda:add_position(menu_label))
    add_button.pack()

    ##BUTTON Edytuj Pozycję
    edit_button = tk.Button(administration_panel, text="Edytuj pozycję", command=lambda:edit_position(get_object(int(position_id.get())),menu_label))
    edit_button.pack()
    ##BUTTON Usuń Pozycję
    delete_button = tk.Button(administration_panel, text="Usuń pozycję", command=lambda:delete_position(administration_panel, int(position_id.get()), menu_label))
    delete_button.pack()
    ##ENTRY ID to edit/delete
    position_id = tk.Entry(administration_panel)
    position_id.pack()
    ##TEXT Podaj ID (dla usuń/edytuj)
    position_id_text = tk.Label(administration_panel, text="Podaj ID (dla usuń/edytuj)")
    position_id_text.pack()

def update_menu_label():
    menu_items = load_menu_content()
    formatted_text = format_menu(menu_items)
    menu_label.config(text=formatted_text)