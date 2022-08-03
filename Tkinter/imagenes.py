from tkinter import *

windows = Tk()

# cargamos la imagen

logo = PhotoImage(file="charmander.png")

# con image indicamos cual es la imagen que se colocara en esa etiqueta

lblMensaje = Label(windows, image=logo).pack()

# ahora colocaremos un label contexto y otro con imagen

mensaje = '''Ahora colocamos texto
junto con una imagen
y experimetamos como vana lucir 
juntos
'''

lbl_mensaje_2 = Label(windows, image=logo).pack(side="left")
lbl_mensaje_3 = Label(windows, text=mensaje).pack(side="right")

# podemos hacer que el texto se coloque sobre la imagen
# al usar compound
lbl_mensaje_4 = Label(windows, text=mensaje, image=logo,
                      compound=CENTER).pack()
windows.mainloop()
