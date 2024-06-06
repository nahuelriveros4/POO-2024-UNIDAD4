from tkinter import Tk
from simon import Simon
from VentanaNom import VentanaNombre
from listaJugadores import RankingJugadores
from classRepositorioJugadores import RepositorioJugadores
from classObjectEncoder import ObjectEncoder

def menu():
    # Inicializar la ventana para ingresar el nombre del jugador
    nombre_ventana = VentanaNombre()
    nombre = nombre_ventana.nombre_jugador

    # Verificar si se proporcionó un nombre de jugador
    if nombre_ventana.nombre_jugador:
        # Inicializar el repositorio de jugadores
        conn = ObjectEncoder("pysimonpuntajes.json")
        repositorio = RepositorioJugadores(conn)

        # Crear instancia de Simon y pasar el nombre del jugador y el repositorio
        simon = Simon(nombre, repositorio)

if __name__ == '__main__':
    menu()
