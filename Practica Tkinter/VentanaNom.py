from tkinter import *

class VentanaNombre:
    def __init__(self):
        self.ventana = Tk()
        self.nombre_jugador = ""
        self.ventana.title("Ingrese su nombre")
        self.ventana.geometry("300x150")

        self.label_nombre = Label(self.ventana, text="Ingrese su nombre:")
        self.label_nombre.pack()

        self.entry_nombre = Entry(self.ventana)
        self.entry_nombre.pack()

        self.boton_ingresar = Button(self.ventana, text="Iniciar Juago", command=self.obtenerNombre)
        self.boton_ingresar.pack()

        self.ventana.mainloop()

    def obtenerNombre(self):
        self.nombre_jugador = self.entry_nombre.get()
        self.ventana.destroy()