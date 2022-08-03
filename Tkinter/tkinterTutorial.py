# importando tkinter
from tkinter import *

# tenemos que crear un widget que sea la raiz
# se tiene que crear antes que los otros widgets y solo hay una
# raiz por aplicacion
# la raiz va a ser la ventana donde colocaremos los otros widgets

window = Tk()

# ahora vamos a crear una etiqueta
# el primer parametro es la ventana padre
# el segundo parametro es el texto que deseamos mostrar en la etiqueta

lblMensaje = Label(window, text="Hola Mundo")

# con pack la ventana se acopla al tamaño de la etiqueta

lblMensaje.pack()

# para desplegar la ventana es necesario invocar el ciclo principal
# adentro de ese ciclo se lleva a cabo la administracion de eventos

window.mainloop()
