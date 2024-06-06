from tkinter import *

class VentanaNombre:
    def __init__(self):
        self.ventana = Tk()
        self.nombre_jugador = ""
        self.ventana.title("Simon")
        self.ventana.geometry("200x100")

        self.label_nombre = Label(self.ventana, text="Nombre del Jugador:")
        self.label_nombre.pack()

        self.entry_nombre = Entry(self.ventana)
        self.entry_nombre.pack(pady=5)

        self.boton_ingresar = Button(self.ventana, text="Iniciar Juego", command=self.obtenerNombre)
        self.boton_ingresar.pack()
        
        self.ventana.mainloop()
        
    def obtenerNombre(self):
        self.nombre_jugador = self.entry_nombre.get()
        self.ventana.destroy()


