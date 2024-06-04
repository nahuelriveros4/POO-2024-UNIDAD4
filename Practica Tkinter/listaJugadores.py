from tkinter import *
from tkinter import ttk

class RankingJugadores:
    def __init__(self, jugadores):
        self.ventana = Toplevel()
        self.ventana.title("Ranking de Jugadores")
        self.ventana.geometry("500x300")

        self.tabla = ttk.Treeview(self.ventana, columns=("Nombre", "Fecha", "Hora", "Puntaje"), show="headings")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Fecha", text="Fecha")
        self.tabla.heading("Hora", text="Hora")
        self.tabla.heading("Puntaje", text="Puntaje")
        self.tabla.pack(fill=BOTH, expand=True)

        for jugador in jugadores:
            self.tabla.insert("", "end", values=(jugador.getNombre(), jugador.getFecha(), jugador.getHora(), jugador.getPuntaje()))
