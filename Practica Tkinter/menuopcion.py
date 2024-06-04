import tkinter as tk
from tkinter import *
from tkinter import ttk, font
from listaJugadores import RankingJugadores

class MenuOpcion:
    def __init__(self, ventana,jugadores):
        self.ventana = ventana
        self.jugadores = jugadores
        self.fuente = font.Font(weight="normal")
        barraMenu = Menu(self.ventana)
        menuPuntajes = Menu(barraMenu, tearoff=0)
        menuSalir = Menu(barraMenu, tearoff=0)
        menuPuntajes.add_command(label="Ver Puntajes", command=self.puntajes)
        menuSalir.add_command(label='Salir', command=self.ventana.destroy)
        barraMenu.add_cascade(label="Puntajes", menu=menuPuntajes)
        barraMenu.add_cascade(label="Salir", menu=menuSalir)
        self.ventana.config(menu=barraMenu)

    def puntajes(self):
        RankingJugadores(self.jugadores)
