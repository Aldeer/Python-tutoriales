# Algunos widgets se conectan a las variables por medio de diferentes opciones
#	variables
#	textVariable
#	onvalue
#	offvalue
# Para esto necesitamos variables que sean sublcases de variable, lo cual se define
# en Tkinter
#	StringVar
#	IntVar
#	DoubleVar
#	Booleanvar

from tkinter import *


def Mostrar():
    if seleccion.get() == 1:
        msg = "Haz seleccionado Python"
    if seleccion.get() == 2:
        msg = "Haz seleccionado C#"
    if seleccion.get() == 3:
        msg = "Haz seleccionado Java"

    lbl_msg.config(text=msg)


windows = Tk()
seleccion = IntVar()

r_btn_python = Radiobutton(windows, text="Python", variable=seleccion,
                           value=1, command=Mostrar).pack(anchor=W)
r_btn_c = Radiobutton(windows, text="C#", variable=seleccion,
                      value=2, command=Mostrar).pack(anchor=W)
r_btn_java = Radiobutton(windows, text="Java", variable=seleccion,
                         value=3, command=Mostrar).pack(anchor=W)

lbl_msg = Label(windows)
lbl_msg.pack()
windows.mainloop()
