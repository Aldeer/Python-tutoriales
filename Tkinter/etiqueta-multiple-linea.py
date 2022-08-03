# importamos tkinter
from tkinter import *

wind = Tk()

# una forma sencilla de crear una etiqueta de multiples lineas
# escreando una cadena y colocarla en la etiqueta

mensaje = '''Hola mundo
me da gusto
que aprender sobre Python
'''

# podemos colocar pack en la misma linea
# con justify indicamos como se justifica el texto
# LEFT, CENTER, RIGHT

lblMensaje = Label(wind, text=mensaje, justify=CENTER).pack()

wind.mainloop()
