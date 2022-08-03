from tkinter import *


def Mostrar():
    msg = " "

    if(int_chk1.get() == 1):
        msg = msg+" Manzana"
    if(int_chk2.get() == 1):
        msg = msg+" Pera"
    else:
        msg = msg+" no olvide comprar pera"

    lbl_msg.config(text=msg)


windows = Tk()

# Estas variables las usaremos para concer el estado de los checkbox
int_chk1 = IntVar()
int_chk2 = IntVar()

# Etiqueta para mostrar el mensaje
lbl_msg = Label(windows)
lbl_msg.pack()

# Creamos los checkbox
check_1 = Checkbutton(windows, text="Manzana", variable=int_chk1).pack()
check_2 = Checkbutton(windows, text="Pera", variable=int_chk2).pack()

# boton para ejecutar la accion de mostrar
btn_mostrar = Button(windows, text="Comprar", command=Mostrar).pack()

windows.mainloop()
