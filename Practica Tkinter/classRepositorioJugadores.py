from classJugador import Jugador
from classObjectEncoder import ObjectEncoder
from ManejadorJugadores import ManejadorJugador
class RepositorioJugadores(object):
    __conn:object
    __manejador: object
    def __init__(self,conn):
        self.__conn = conn
        diccionario = self.__conn.leerJSONArchivo()
        self.__manejador=self.__conn.decodificarDiccionario(diccionario)

    def obtenerListaJugadores(self):
        return self.__manejador.getListaJugadores()
    
    
    def agregarJugador(self, jugador):
        self.__manejador.agregarJugador(jugador)
        return jugador
    
    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())
        