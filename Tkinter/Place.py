from tkinter import *

windows = Tk()
windows.geometry("640x480")

# Colocamos una etiqueta
lbl_1 = Label(windows, text="Aldeer", bg="#FFAAAA")

# Indicamos las coordenadas donde deseamos que aparezca el widget
# Luego el ancho y el alto del area que ocupara en la ventana
lbl_1.place(x=0, y=0, width=100, height=30)

lbl_2 = Label(windows, text="Aldeer", bg="#AAFFAA")
lbl_2.place(x=100, y=150, width=300, height=100)

lbl_3 = Label(windows, text="Aldeer", bg="#AAAAFF")
lbl_3.place(x=350, y=170, width=100, height=25)
windows.mainloop()
