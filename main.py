from tkinter import IntVar
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox
from tkinter import filedialog
from utils.extract_coordinates import extract_coords_from_pm
from utils.extract_coordinates import extrac_coord_from_list
from utils.create_tm import create_tables
from openpyxl import Workbook
from popups.instructions import instructions_window
from popups.donations import donations_window
from styles import *

# Configuración de la ventana principal con ttkthemes
window = ThemedTk(theme="breeze")
window.geometry("500x270")
window.title("ITM")
window.resizable(False, False)

#Variables:
selected_format = IntVar()
selected_format.set(1)#El PM por default.
set_coordenadas = []
file_names = []

#Widgets:
inner_frame = ttk.Frame(window)
tittle = ttk.Label(inner_frame, text = 'Tablas de Mensura', font = font_tittle, foreground = blue_tittle)
descipcion_tm_text = """Con este programa usted podrá generar la Tabla de Mensura\no Cuadro de Construcción de una o varias parcelas en base a un archivo\nde texto (.txt) que contenga sus coordenadas, el cual puede ser\ningresado en dos formatos:\n\n1-El archivo que genera el comando <<PM>>.                                    \n2-Un archivo .txt con el texto que genera el comando <<LIST>>."""
descipcion_tm = ttk.Label(inner_frame, text = descipcion_tm_text, font = button_font)
format_choice_label = ttk.Label(inner_frame, text="Seleccione el formato de origen:", font=label_font, foreground = blue_tittle)
pm_choice = ttk.Radiobutton(inner_frame, text="Comando <<PM>>", variable=selected_format, value=1)
list_choice = ttk.Radiobutton(inner_frame, text="Comando <<LIST>>", variable=selected_format, value=2)

#Callers:
def upload_text():
    global set_coordenadas
    global file_names
    set_coordenadas = []
    file_names = []

    directions = filedialog.askopenfilename(title="Seleccione Archivo de Texto (.txt)", initialdir = "desktop", multiple = True, filetypes = (("Ficheros de Texto", "*.txt"), ("Todos los Ficheros", "*.*")))

    if directions == '':
        return
    
    if selected_format.get() == 1:
        for dir in directions:
            current_coords = extract_coords_from_pm(dir)
            if not current_coords:
                return
            set_coordenadas.append(current_coords)
            file_names.append(dir.split("/").pop())

    elif selected_format.get() == 2:
        for dir in directions:
            current_coords = extrac_coord_from_list(dir)
            if not current_coords:
                return
            set_coordenadas.append(current_coords)
            file_names.append(dir.split("/").pop())
            
    export_button["state"] = "active"
    messagebox.showinfo('Coordenadas Cargadas', 'Las coordenadas han sido cargadas exitosamente.')
    return None

def export_tables():
    
    dir = filedialog.asksaveasfilename(defaultextension = ".xlsx", filetypes = (("Libro de Excel", "*.xlsx"), ("Todos los Ficheros", "*.*")))
    
    if dir == '':
        return
    
    book = Workbook()
    create_tables(book, file_names, set_coordenadas)
    book.save(dir)
    messagebox.showinfo("Hecho", "Las tablas han sido guardadas exitosamente en: {}".format(dir))

ins_window = None
dnt_window = None

def open_window(comand):
    global ins_window
    global dnt_window
    
    if comand == "ins":
        if ins_window == None:
            ins_window = instructions_window()    
        else:
            ins_window.destroy()
            ins_window = instructions_window()
        return

    if comand == "dnt":
        if dnt_window == None:
            dnt_window = donations_window()
        else:
            dnt_window.destroy()
            dnt_window = donations_window()
        return
    
#Buttons:
upload_button = ttk.Button(
                    inner_frame, 
                    text="Cargar txt", 
                    width=btn_width, 
                    command=upload_text)

instructions_button = ttk.Button(
                        inner_frame, 
                        text="Instrucciones", 
                        width=btn_width, 
                        command=lambda: open_window("ins"))

export_button = ttk.Button(
                    inner_frame, 
                    text="Exportar Tablas", 
                    width=btn_width, 
                    state="disabled", 
                    command=export_tables)

donate_button = ttk.Button(
                    inner_frame,
                    text="Donaciones", 
                    width=btn_width,
                    command=lambda: open_window("dnt"))

#Grid positions:
tittle.grid(row = 0, column = 0, columnspan = 4, pady = 5)
descipcion_tm.grid(row = 1, column = 0, columnspan = 4, rowspan = 5, padx = 10)
format_choice_label.grid(row = 6, column = 0, columnspan = 4, pady=10)
pm_choice.grid(row=7, column=0, columnspan=2,pady = 5)
list_choice.grid(row=7, column=2, columnspan=2, pady = 5)
upload_button.grid(row=8, column=0, padx=1)
instructions_button.grid(row=8, column=1,padx=1)
export_button.grid(row=8, column=2,padx=1)
donate_button.grid(row=8, column=3,padx=1)

inner_frame.pack(padx=5, pady=5)
window.mainloop()
