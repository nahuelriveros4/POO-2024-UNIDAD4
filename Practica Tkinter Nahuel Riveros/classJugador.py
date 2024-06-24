class Jugador(object):
    __nombre: str
    __fecha:str
    __hora:str
    __puntaje: str
    def __init__(self, nombre,fecha,hora,puntaje):
        self.__nombre = self.requerido(nombre,"Nombre es un valor requerido")
        self.__fecha = fecha
        self.__hora = hora
        self.__puntaje = puntaje

    def requerido(self, nombre, mensaje):
        if not nombre:
            raise ValueError(mensaje)
        return nombre
    
    def getNombre(self):
        return self.__nombre
    
    def getFecha(self):
        return self.__fecha
    
    def getHora(self):
        return self.__hora
    
    def getPuntaje(self):
        return self.__puntaje
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__, 
            __atributos__ = dict(
                nombre = self.__nombre,
                fecha = self.__fecha,
                hora = self.__hora,
                puntaje = self.__puntaje
            )
        )
        return d
    
    def __gt__(self,otro):
        return self.__puntaje > otro.__puntaje