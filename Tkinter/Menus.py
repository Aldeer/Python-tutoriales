from tkinter import *

windows = Tk()


def Menu1():
    print("Ejecucion Menu 1")


def Menu2():
    print("Ejecucion Menu 2")


def Salir():
    windows.destroy()


# creamos el menu de la ventana
mi_menu = Menu(windows)
windows.config(menu=mi_menu)

# Le ponemos una primera seccion y lo asignamos al menu de la ventana
menu_principal = Menu(mi_menu)
mi_menu.add_cascade(label="Archivo", menu=menu_principal)

# Creamos elementos para ese menu
menu_principal.add_command(label="Accion 1", command=Menu1)
menu_principal.add_command(label="Accion 2", command=Menu2)
menu_principal.add_command(label="Salir", command=Salir)

windows.mainloop()
