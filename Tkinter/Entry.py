from tkinter import *


def Calcular():
    dias = int(edad.get())*365
    msg = nombre.get()+" has vivido "+str(dias)+" dias"
    lbl_msg.config(text=msg)


windows = Tk()

# Creamos una etiqueta para indicar que ahi va el nombre
Label(windows, text="Nombre").pack()
# Colocamos un Entry para poder tener la entrada de usuario
nombre = StringVar()
input_name = Entry(windows, textvariable=nombre).pack()

Label(windows, text="Edad").pack()
edad = IntVar()
input_edad = Entry(windows, textvariable=edad).pack()

# Etiqueta para mostrar el mensaje
lbl_msg = Label(windows)
lbl_msg.pack()

btn_calcular = Button(windows, text="Calcular", command=Calcular).pack()

windows.mainloop()
