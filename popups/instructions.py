from tkinter import Toplevel
from styles import label_font, blue_tittle, button_font, btn_width
from tkinter import ttk

def instructions_window():
    
    ins_window = Toplevel()
    ins_window.title("Instrucciones")
    ins_window.geometry("540x355")
    ins_window.resizable(False, False)
    inner_frame = ttk.Frame(ins_window)
    
    tittle = ttk.Label(
        inner_frame,
        text="Instrucciones",
        font=label_font,
        foreground=blue_tittle
    )
    
    body_text = ""
    body_text += "Commando PM:\n\n"
    body_text += "En AutoCAD, busque la polilínea de la que quiere generar el cuadro de construcción,\n"
    body_text += "utilice el comando <<PM>> para generar un archivo de texto con lar coordenadas\n"
    body_text += "de la polilínea, luego seleccione dicho archivo cuando pulse el botón <<Cargar txt>>,\n"
    body_text += "finalmente pulse <<Exportar Tablas>> y guarde el resultando donde le plazca.\n\n"    
    body_text += "Nota: PM no es un comando nativo de AutoCAD.\n\n"
    body_text += "Comando List:\n\n"
    body_text += "En AutoCAD, busque la polilínea de la que quiere generar el cuadro de construcción,\n"
    body_text += "utilice el comando <<LIST>> para generar las coordenadas de la polilínea,\n"
    body_text += "cópielas de la consola y guárdelas en un archivo .txt,\n"
    body_text += "luego seleccione dicho archivo cuando pulse el botón <<Cargar txt>>,\n"
    body_text += "finalmente pulse <<Exportar Tablas>> y guarde el resultando donde le plazca.\n"

    text = ttk.Label(inner_frame, text=body_text, font=button_font)    
    exit_btn = ttk.Button(inner_frame, text="Entiendo", width=btn_width, command=lambda: ins_window.destroy())
    tittle.grid(row=0, column=0, columnspan=3, pady=5)
    text.grid(row=1, column=0, columnspan=3)
    exit_btn.grid(row=2, column=1)
    inner_frame.pack(padx=25, pady=10)
    
    return ins_window
