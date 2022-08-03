from tkinter import *

wind = Tk()

# con fg indicamos el color de la fuente
lblMensaje = Label(wind, text="Hola mundo", fg="blue").pack()

# font nos sirve para indicar el tipo de fuente y su estilo

lblMensaje2 = Label(wind, text="Hola mundo", fg="red",
                    font="Helvetica 10 bold").pack()

# bg nos permite indicar el color de fondo en elt exto

lblMensaje3 = Label(wind, text="Hola mundo", fg="white",
                    bg="black", font="Helvetica 40 bold").pack()
wind.mainloop()
