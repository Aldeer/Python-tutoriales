# Hemos estado usando pack, pero sin entrar en detalles
# No solo nos permite colocar los elementos en la ventana, tambien
# darles orden.
# Pack es un Layout manager junto con grid y place

# Lo usamos para indicar la posicion de un widget con relacion a otros
# Es sencillo, pero limitado

from tkinter import *

windows = Tk()

# Al colocar pack solamente colocal el widget en el tamaño que
# necesita centrado y una abajo de otra

# con fill hacemos que el widget sea tan ancho (x)
# como el widget que lo contiene, en este caso la ventana
lbl_1 = Label(windows, text="Aldeer", bg="#FFAAAA")
lbl_1.pack()
lbl_2 = Label(windows, text="Aldeer", bg="#AAFFAA")
lbl_2.pack(fill=X)

# con pad creamos un "marco" alrededor del widget

lbl_4 = Label(windows, text="Aldeer", bg="#FFAAAA")
lbl_4.pack(padx=20, pady=20)

# con ipad creamos un "marcoo" interno en el widget

lbl_5 = Label(windows, text="Aldeer", bg="#AAFFAA")
lbl_5.pack(ipadx=90, ipady=20)

# Para poner los widgets al lado en lugar de arriba o abajo
# usamos side, e indicamos la posicion relativa LEFT, RIGHT

lbl_3 = Label(windows, text="Aldeer", bg="#AAAAFF")
lbl_3.pack(side=LEFT)
lbl_6 = Label(windows, text="Aldeer", bg="#FFAAAA")
lbl_6.pack(side=RIGHT)


windows.mainloop()
