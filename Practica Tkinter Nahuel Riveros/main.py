from simon import Simon
from VentanaNom import VentanaNombre
from classRepositorioJugadores import RepositorioJugadores
from classObjectEncoder import ObjectEncoder

def menu():
    nombre_ventana = VentanaNombre()
    nombre = nombre_ventana.nombre_jugador

    if nombre_ventana.nombre_jugador:
        conn = ObjectEncoder("pysimonpuntajes.json")
        repositorio = RepositorioJugadores(conn)
        simon = Simon(nombre, repositorio)

if __name__ == '__main__':
    menu()
