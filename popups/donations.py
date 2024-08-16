from tkinter import Toplevel
from styles import label_font, blue_tittle, button_font, btn_width
from tkinter import ttk

def donations_window():
    
    dnt_window = Toplevel()
    dnt_window.title("Donaciones")
    dnt_window.geometry("400x230")
    dnt_window.resizable(False, False)
    inner_frame = ttk.Frame(dnt_window)

    tittle = ttk.Label(
        inner_frame,
        text="Donaciones",
        font=label_font,
        foreground=blue_tittle
    )
    
    body_text = ""
    body_text += "Esta pequeña pieza de software es totalmente gratis,\n"
    body_text += "pero si le ha sido útil y usted está en disposición\n"
    body_text += "de darle un cariñito a su autor, puede hacerlo depositando\n"
    body_text += "lo que le parezca en alguna de las siguientes cuentas:\n\n"
    body_text += "1-> 827930439 (Cuenta corriente Banco Popular)\n"
    body_text += "2-> 783006984 (Cuenta corriente Banco Popular)\n"
    body_text += "3-> 9601298676 (Cuenta de ahorros Banreservas)\n"
    
    text = ttk.Label(inner_frame, text=body_text, font=button_font)    
    exit_btn = ttk.Button(inner_frame, text="ok : )", width=btn_width, command=lambda: dnt_window.destroy())
    tittle.grid(row=0, column=0, columnspan=3, pady=5)
    text.grid(row=1, column=0, columnspan=3)
    exit_btn.grid(row=2, column=1)
    inner_frame.pack(padx=25, pady=10)
    
    return dnt_window
