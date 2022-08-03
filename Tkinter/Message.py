from enum import auto
from tkinter import *
from tkinter.tix import AUTO

# message es una variacion de label que nos permite
# colocar texto multilinea sin preocuparnos por donde
# hacer el cambio de linea

windows = Tk()

mi_texto = "Hola Mundo. Me da mucho gusto estar aprendiendo la aplicacion grafica Tkinter"

# ejemplo1, sin mas parametros adopta a la ventana como esta
msg_1 = Message(windows, text=mi_texto).pack()

# ejemplo 2, podemos indicar el ancho que deseamos,
# vemos como se ajusta el texto
msg_2 = Message(windows, text=mi_texto, width=300).pack()

# Ejemplo 3, podemos hacer una configuracion para el estilo
msg_3 = Message(windows, text=mi_texto, width=300)
msg_3.config(bg="blue", fg="white", font="times 24 bold")
msg_3.pack()
windows.mainloop()
