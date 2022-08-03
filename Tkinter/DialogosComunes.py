from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename


def MostrarDialogo():
    ruta = askopenfilename()
    print(ruta)


def SeleccionarColor():
    color_s = askcolor(color="#FFFFFF", title="Seleccionar un color")
    print(color_s)


windows = Tk()

btn_abrir = Button(text="Abrir Archivo", command=MostrarDialogo).pack()
btn_color_s = Button(text="Seleccionar Color", command=SeleccionarColor).pack()

windows.mainloop()
