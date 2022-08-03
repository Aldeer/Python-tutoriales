from tkinter import *
from tkinter import messagebox


def mostrarError():
    # Para mostrar error
    messagebox.showerror("Error de sintaxis", "Te falto cerrar el parentesis")


def mostrarInfo():
    # Para Mostrar informacion
    messagebox.showinfo("Informacion", "Programador Aldeer")


def mostrarAdvertencia():
    # Para Mostrar una advertencia
    messagebox.showwarning("ADVERTENCIA", "mira mi pagina de github")


def mostrarPregunta():
    # Para preguntar algo
    r = messagebox.askquestion("pregunta", "Programamos en python?")

    if r == "yes":
        messagebox.showinfo("programa", "muy bien")
    else:
        messagebox.showinfo("Programa", "aprende con Aldeer")


def mostrarPreguntaSi():
    r = messagebox.askokcancel("Ejecutar", "Ejecutamos el programa?")

    if r == True:
        messagebox.showinfo("Respuesta", "Ejecutando...")
    else:
        messagebox.showinfo("Respuesta", "No se ha ejecutado")

# Para preguntar con retry y cancel


def mostrarPreguntasRetry():
    r = messagebox.askretrycancel("Ejecutar", "Ejecutamos el programa?")

    if r == True:
        messagebox.showinfo("Respuesta", "Se ejecuta de nuevo")
    else:
        messagebox.showinfo("Respuesta", "Ya no se ejecuta de nuevo")


def mostrarAskyesno():
    r = messagebox.askyesno("Ejecutar", "Ejecutamos el programa?")
    if r == True:
        messagebox.showinfo("Respuesta", "Se ejectua de nuevo")
    else:
        messagebox.showinfo("Respuesta", "Ya no se ejecuta")


def mostrarAskyesnocancel():
    r = messagebox.askyesnocancel("Ejecutar", "ejecutamos el programa?")

    if r == True:
        messagebox.showinfo("Respuesta", "Se ejecuta de nuevo")
    if r == False:
        messagebox.showinfo("Respuesta", "Ya no se ejecuta")
    if r == None:
        messagebox.showinfo("Respuesta", "Cancelaste la ejecucion")


windows = Tk()
windows.geometry("200x250")

btn_error = Button(text="Mostrar Error", command=mostrarError).pack()
btn_info = Button(text="Mostrar info", command=mostrarInfo).pack()
btn_warning = Button(text="Mostrar advertencia",
                     command=mostrarAdvertencia).pack()
btn_pregunta = Button(text="Mostrar pregunta", command=mostrarPregunta).pack()
btn_pregunta_si = Button(text="Mostrar Ejecucion",
                         command=mostrarPreguntaSi).pack()
btn_preguntar_retry = Button(
    text="Mostrar Retry", command=mostrarPreguntasRetry).pack()
btn_preguntar_askyesno = Button(
    text="Ask yes/no", command=mostrarAskyesno).pack()
btn_askyesnocancel = Button(
    text="Ask yes/no/cancel", command=mostrarAskyesnocancel).pack()
windows.mainloop()
