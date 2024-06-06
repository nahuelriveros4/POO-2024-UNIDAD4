from tkinter import *
from tkinter import messagebox
import random
from datetime import datetime
import time
import winsound
from classJugador import Jugador
from menuopcion import *
from ManejadorJugadores import ManejadorJugador

class Simon:
    def __init__(self, nombre_jugador, repositorio):
        self.ventana = Tk()
        self.arreglo = []
        self.marcador = 0
        self.mayor = 0
        self.contador = 0
        self.nombre_jugador = nombre_jugador
        self.repositorio = repositorio
        self.juegoI = False
        self.colores = ["Azul","Amarillo","Verde","Rojo"]
        self.ventana.title("Simon")
        self.ventana.geometry("400x400")
        self.lista = repositorio.obtenerListaJugadores()
        self.ventana.title("Simon - {}".format(self.nombre_jugador))
        self.menu = MenuOpcion(self.ventana, self.lista)
        
        self.iniciarBotones()
        self.ventana.mainloop()


    def iniciarBotones(self):
        self.botonAzul = Button(self.ventana,command=lambda:self.presionar("Azul"), height=6,width=13,bg="blue")
        self.botonAzul.place(x=100,y=100)

        self.botonVerde = Button(self.ventana,command=lambda:self.presionar("Verde"), height=6,width=13,bg="green")
        self.botonVerde.place(x=200,y=100)
        
        self.botonAmarillo = Button(self.ventana,command=lambda:self.presionar("Amarillo"), height=6,width=13,bg="yellow")
        self.botonAmarillo.place(x=100,y=200)

        self.botonRojo = Button(self.ventana,command=lambda:self.presionar("Rojo"), height=6,width=13,bg="red")
        self.botonRojo.place(x=200,y=200)

        self.botonIniciar = Button(self.ventana,command=self.iniciar,height=2,width=6,bg="white",text="Iniciar")
        self.botonIniciar.place(x=175,y=40)

        self.etiqueta = Label(self.ventana,text="Marcador: 0 Record : 0" )
        self.etiqueta.place(x=40,y=40)
        
        # Mostrar nombre del jugador
        self.etiqueta_nombre = Label(self.ventana, text="Jugador: {}".format(self.nombre_jugador))
        self.etiqueta_nombre.place(x=40, y=20)

    def iniciar(self):
        self.contador = 0
        self.marcador = 0
        self.arreglo = []
        self.juegoI = True
        self.crearColor()


    def crearColor(self):
        if self.juegoI:
            color_map = {
                "Azul": (self.botonAzul, "lightblue", "blue", 500, 500),
                "Amarillo": (self.botonAmarillo, "orange", "yellow", 600, 500),
                "Rojo": (self.botonRojo, "orange", "red", 700, 500),
                "Verde": (self.botonVerde, "#00FF00", "green", 800, 500)
            }
            for color in self.arreglo:
                if color in color_map:
                    boton, color1, color2, tiempo_encendido, tiempo_apagado = color_map[color]
                    self.cambio(boton, color1, color2, tiempo_encendido, tiempo_apagado)
                    time.sleep(1)

            aleatorio = random.choice(self.colores)
            self.arreglo.append(aleatorio)

            if aleatorio in color_map:
                boton, color1, color2, tiempo_encendido, tiempo_apagado = color_map[aleatorio]
                self.cambio(boton, color1, color2, tiempo_encendido, tiempo_apagado)


    def cambio(self, btn,colorCambio, ColorInicial,f,d):
        btn.configure(bg=colorCambio)
        self.ventana.update()
        self.sonido(f,d)
        btn.configure(bg=ColorInicial)
        self.ventana.update()

    def presionar(self, color):
        if self.juegoI:
            if len(self.arreglo) >= self.contador:
                if self.arreglo[self.contador] == color:
                    self.contador += 1
                    sonido_map = {
                        "Amarillo": (600, 500),
                        "Verde": (500, 500),
                        "Azul": (700, 500),
                        "Rojo": (800, 500)
                    }
                    if color in sonido_map:
                        frecuencia, duracion = sonido_map[color]
                        self.sonido(frecuencia, duracion)
                    self.revisarTurno()
                    self.etiqueta.config(text=f"Marcador: {self.marcador} Record: {self.mayor}")
                else:
                    self.mostrar_game_over()
                    self.reset_juego()

    def revisarTurno(self):
        if len(self.arreglo) == self.contador:
            self.contador = 0
            self.marcador += 1
            self.botonIniciar.after(1000,self.crearColor)

    def sonido(self,frecuencia,duracion):
        winsound.Beep(frecuencia,duracion)

    def mostrar_game_over(self):
        if self.marcador > self.mayor:
            self.mayor = self.marcador
        self.registrar_puntaje(self.mayor)
        messagebox.showinfo("GAME OVER", f"Tu puntuación: {self.marcador}\nRecord: {self.mayor}")
        self.etiqueta.config(text=f"Marcador: {self.marcador} Record: {self.mayor}")

    def reset_juego(self):
        self.juegoI = False
        self.contador = 0
        self.marcador = 0
        self.arreglo = []


    def registrar_puntaje(self,puntaje):
        # Método para registrar el puntaje del jugador en el repositorio
        ahora = datetime.now()
        fecha = ahora.strftime("%d/%m/%Y")
        hora_actual = ahora.strftime("%H:%M:%S")
        jugador = Jugador(self.nombre_jugador, fecha, hora_actual, puntaje)
        self.repositorio.agregarJugador(jugador)
        self.repositorio.grabarDatos()