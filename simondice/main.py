from tkinter import *
from tkinter import messagebox
import random
import time
import winsound
from VentanaNom import VentanaNombre
class Simon:
    def __init__(self,nombre_jugador):
        self.ventana=Tk()        
        self.arreglo = []
        self.marcador= 0
        self.mayor = 0 
        self.contador = 0
        self.juegoI = False
        self.nombre_jugador = nombre_jugador
        self.ventana.title("Simon - {}".format(self.nombre_jugador))
        self.colores = ["Azul","Amarillo","Verde","Rojo"]
        self.ventana.title("Simon")
        self.ventana.geometry("400x400")
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

        self.botonIniciar = Button(self.ventana,command=self.iniciar,height=2,width=7,bg="white",text="Iniciar")
        self.botonIniciar.place(x=175,y=40)

        self.etiqueta = Label(self.ventana,text="Marcador: 0 Record : 0" )
        self.etiqueta.place(x=40,y=40)
        # Mostrar nombre del jugador
        self.etiqueta_nombre = Label(self.ventana, text="Jugador: {}".format(self.nombre_jugador))
        self.etiqueta_nombre.place(x=40, y=20)


    def presionar(self,color):
        if self.juegoI == True:
            if len(self.arreglo) >= self.contador - 1:
                if self.arreglo[self.contador] == color:
                    self.contador += 1
                    if color == "Amarillo":
                        self.sonido(600,500)
                    if color == "Verde":
                        self.sonido(500,500)
                    if color == "Azul":
                        self.sonido(700,500)
                    if color == "Rojo":
                        self.sonido(800,500)    
                    self.revisarTurno()
                    self.etiqueta.config(text=" Marcador : " + str(self.marcador) + " Record : " + str(self.mayor))
                else:
                    messagebox.showinfo("GAME OVER", "Tu puntuación: " + str(self.marcador) + "\nRecord: " + str(self.mayor))
                    if self.marcador > self.mayor:
                        self.mayor = self.marcador
                    self.etiqueta.config(text=" Marcador : " + str(self.marcador) + " Record : " + str(self.mayor))
                    self.juegoI = False
                    self.contador = 0
                    self.marcador = 0
                    self.arreglo = []
                

    def iniciar(self):
        self.contador = 0
        self.marcador = 0
        self.arreglo = []
        self.juegoI = True
        self.crearColor()

    def revisarTurno(self):
        if len(self.arreglo) == self.contador:
            self.contador = 0
            self.marcador += 1
            self.botonIniciar.after(1000,self.crearColor)

    def crearColor(self):
        if self.juegoI == True:
            i = 0
            while i < len(self.arreglo):
                if self.arreglo[i] == "Azul":
                    self.cambio(self.botonAzul,"lightblue", "blue",500,500)
                if self.arreglo[i] == "Amarillo":
                    self.cambio(self.botonAmarillo,"orange", "yellow",600,500)
                if self.arreglo[i] == "Rojo":
                    self.cambio(self.botonRojo,"orange", "red",700,500)
                if self.arreglo[i] == "Verde":
                    self.cambio(self.botonVerde,"#00FF00", "green",800,500)
                i +=1
                time.sleep(1)
            aleatorio = random.randrange(0,4)
            self.arreglo.append(self.colores[aleatorio])
            if self.arreglo[i] == "Azul":
                self.cambio(self.botonAzul,"lightblue", "blue",500,500)
            if self.arreglo[i] == "Amarillo":
                self.cambio(self.botonAmarillo,"orange", "yellow",600,500)
            if self.arreglo[i] == "Rojo":
                self.cambio(self.botonRojo,"orange", "red",700,500)
            if self.arreglo[i] == "Verde":
                self.cambio(self.botonVerde,"#00FF00", "green",800,500)



    def cambio(self, btn,colorCambio, ColorInicial,f,d):
        btn.configure(bg=colorCambio)
        self.ventana.update()
        self.sonido(f,d)
        btn.configure(bg=ColorInicial)
        self.ventana.update()

    def sonido(self,frecuencia,duracion):
        winsound.Beep(frecuencia,duracion)

if __name__ == '__main__':
    nombreVentana = VentanaNombre()
    nombre = nombreVentana.nombre_jugador
    obj =  Simon(nombre) 