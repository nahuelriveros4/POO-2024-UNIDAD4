from classContacto import Contacto
from classObjectEncoder import ObjectEncoder
from classManejadorContactos import ManejadorContactos
class RespositorioContactos(object):
    __conn: object
    __manejador: object
    def __init__(self, conn):
        self.__conn = conn
        diccionario= self.__conn.leerJSONArchivo()
        self.__manejador= self.__conn.decodificarDiccionario(diccionario)
    def obtenerListaContactos(self):
        return self.__manejador.getListaContactos()
    def agregarContacto(self, contacto):
        self.__manejador.agregarContacto(contacto)
        return contacto
    def modificarContacto(self, contacto):
        self.__manejador.updateContacto(contacto)
        return contacto
    def borrarContacto(self, contacto):
        self.__manejador.deleteContacto(contacto)
    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())
