from tkinter import *

windows = Tk()

# Creamos el scroll y el texto
scroll = Scrollbar(windows)
texto = Text(windows, height=20, width=30)

# Ahora colocamos el scroll y el texto
scroll.pack(side=RIGHT, fill=Y)
texto.pack(side=LEFT, fill=Y)

# Configuramos el widget
# Indicamos que modificara  el texto en su scroll y invocando el metodo yview
# yview, xview
scroll.config(command=texto.yview)

# Asociamos con el scroll para poder colocarlo en la posicion invocando
# el metodo set
texto.config(yscrollcommand=scroll.set)

msg = '''¿Por que esta magnifica tecnologia cientifica,
que ahorra trabajo y nos hace la vida mas facil,
nos aporta tan poca felicidad? La respuesta es esta,
simplemente porque aun no hemos aprendido a usarla con tino,
Nunca consideres al estudio como una obligacion, sino como una
oportunidad para penetrar en el bello y maravilloso mundo del saber
la electricidad y la energia atomica: la voluntad.
-Albert Einstein
'''

# Insertamos el mensaje al final del texto
texto.insert(END, msg)

windows.mainloop()
