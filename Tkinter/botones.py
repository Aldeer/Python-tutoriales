from tkinter import *

# creamos una clase para este ejemplo


class Test():
    def __init__(self):
        self.windows = Tk()

        # tenemos que crear una variable de tipo StringVar para
        # poder cambiar el texto de un widget
        self.texto = StringVar()
        # le damos un valor inicial
        self.texto.set("Hola a todos")

        # creamos la etiqueta
        # con textvariable indicamos cual es la variable que tendra el texto
        self.lbl_etiqueta = Label(
            self.windows, textvariable=self.texto, font="arial 24").pack()

        # Creamos el boton
        self.btn = Button(self.windows, text="haz mensaje",
                          font="arial 24", command=self.changeText).pack()

        self.windows.mainloop()

    def changeText(self):
        self.texto.set("Nuevo Mensaje")


app = Test()
