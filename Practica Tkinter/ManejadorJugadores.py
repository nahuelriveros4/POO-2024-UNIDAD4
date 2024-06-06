from classJugador import Jugador
class ManejadorJugador:
    __ListaJugadores:list
    def __init__(self):
        self.__ListaJugadores = []

    def agregarJugador(self,unJugador):
        self.__ListaJugadores.append(unJugador)
                
    def getListaJugadores(self):
        return self.__ListaJugadores
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            jugadores = [jugador.toJSON() for jugador in self.__ListaJugadores]
        )
        return d