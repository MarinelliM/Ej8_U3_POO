class Agente:
    __cuil: str
    __apellido: str
    __nombre: str
    __sueldoB:int
    __antiguedad:int

    def __init__(self,**kwargs) -> None:
        self.__cuil = kwargs['cuil']
        self.__apellido = kwargs['apellido']
        self.__nombre = kwargs['nombre']
        self.__sueldoB = kwargs['sueldo']
        self.__antiguedad = kwargs['anti']

    def getnombrecompleto(self):
        return f'Apellido y Nombre: {self.__apellido} {self.__nombre}'
    
    def setbasico(self,sueldonuevo):
        self.__sueldoB = sueldonuevo
    
    def getsueldo(self):
        return self.__sueldoB
    
    def getcuil(self):
        return self.__cuil
    
    def getnombre(self):
        return self.__nombre
    
    def getapellido(self):
        return self.__apellido
    
    def getTipoAgente(self):
        pass

    def getanti(self):
        return self.__antiguedad
    
    def __gt__(self, otro):
        return self.__apellido > otro.__apellido
    
    def toJson(self):
        return
    
    def calcuoSueldo(self):
        ant = self.__antiguedad
        sueldo = self.__sueldoB
        total = (ant*sueldo)/100
        return total
    
    def mostrar(self):
        print('Datos Agente:')
        print('Nombre y Apellido: {}, Cuil: {}, Sueldo Basico: {}, Antiguedad: {}'.format(self.getnombrecompleto(),self.getcuil(),self.__sueldoB,self.__antiguedad))