import json
from pathlib import Path
from classManejadorContactos import ManejadorContactos
from classContacto import Contacto
class ObjectEncoder(object):
    __pathArchivo: object
    def __init__(self, pathArchivo):
        self.__pathArchivo=pathArchivo

    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = globals()[class_name]  # Buscar la clase en el ámbito global
            if class_name == 'ManejadorContactos':
                contactos = d['__contactos__']
                manejador = class_()
                for i in range(len(contactos)):
                    dContacto = contactos[i]
                    class_name = dContacto.pop('__class__')
                    class_ = globals()[class_name]  # Buscar la clase en el ámbito global
                    atributos = dContacto['__atributos__']
                    unContacto = class_(**atributos)
                    manejador.agregarContacto(unContacto)
                return manejador
            
    def guardarJSONArchivo(self, diccionario):
        with Path(self.__pathArchivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
    def leerJSONArchivo(self):
        with Path(self.__pathArchivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
        return diccionario