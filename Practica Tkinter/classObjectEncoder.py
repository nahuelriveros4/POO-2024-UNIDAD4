import json
from ManejadorJugadores import ManejadorJugador
from classJugador import Jugador
from pathlib import Path
class ObjectEncoder(object):
    __Archivo : object
    def __init__(self, archivo):
        self.__Archivo = archivo

    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'ManejadorJugador':
                jugadores = d['jugadores']
                manejador = class_()
                for i in range(len(jugadores)):
                    dJugadores = jugadores[i]
                    class_name = dJugadores.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dJugadores['__atributos__']
                    unJugador = class_(**atributos)
                    manejador.agregarJugador(unJugador)
        return manejador
        
    def guardarJSONArchivo(self, diccionario):
        with Path(self.__Archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self):
        try:
            with Path(self.__Archivo).open(encoding="UTF-8") as fuente:
                diccionario=json.load(fuente)
            return diccionario
        except Exception as e:
            print("Error al leer el archivo JSON:", e)
            return None