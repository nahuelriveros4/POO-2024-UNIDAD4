from tkinter import *
from tkinter import ttk
import tkinter as tk
from classJugador import Jugador
from ManejadorJugadores import ManejadorJugador

class RankingJugadores:
    def __init__(self, jugadores):
        self.ventana = Tk()
        self.ventana.title("Ranking de Jugadores")
        self.ventana.geometry("900x300")
        self.ventana.resizable(False,False)
        style = ttk.Style()
        style.configure("Centered.TLabel", anchor="center")
        self.tabla = ttk.Treeview(self.ventana, columns=("Nombre", "Fecha", "Hora", "Puntaje"), show="headings")

        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Fecha", text="Fecha")
        self.tabla.heading("Hora", text="Hora")
        self.tabla.heading("Puntaje", text="Puntaje")
        
        self.tabla.column("Nombre", anchor="center")
        self.tabla.column("Fecha", anchor="center")
        self.tabla.column("Hora", anchor="center")
        self.tabla.column("Puntaje", anchor="center")
        
        self.tabla.pack(fill=BOTH, expand=True)

        self.boton_cerrar = Button(self.ventana,text="Cerrar", height=2,width=6,bg="white",command=self.ventana.destroy)
       # self.boton_cerrar.place(x=420, y=255)
        self.boton_cerrar.pack()

        jugadoresOrdenados = sorted(jugadores, reverse=True)
        
        for jugador in jugadoresOrdenados:
            self.tabla.insert("", "end", values=(jugador.getNombre(), jugador.getFecha(), jugador.getHora(), jugador.getPuntaje()))
