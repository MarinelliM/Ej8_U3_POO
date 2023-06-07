from Agentes import Agente
class Docente(Agente):
    __carrera: str
    __cargo: str
    __catedra: str

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__carrera = kwargs['carrera']
        self.__cargo = kwargs['cargo']
        self.__catedra = kwargs['catedra']

    def getcargo(self):
        return self.__cargo
    
    def getcarrera(self):
        return self.__carrera
    
    def getcatedra(self):
        return self.__catedra
    
    def getTipoAgente(self):
        return (self.__class__.__name__)

    def mostrar(self):
        super().mostrar()
        print('Datos Docente:')
        print('Carrera: {}, Cargo: {}, Catedra: {}'.format(self.__carrera,self.__cargo,self.__catedra))

    def toJson(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                    cuil= self.getcuil(),
                    apellido= self.getapellido(),
                    nombre= self.getnombre(),
                    sueldo= self.getsueldo(),
                    anti= self.getanti(),
                    carrera = self.__carrera,
                    cargo = self.__cargo,
                    catedra = self.__catedra,
                )
            )
        return d
    
    def calcuoSueldo(self):
        sueldob = self.getsueldo()
        sup = super().calcuoSueldo()
        if self.__cargo == 'simple':
            sueldob = sueldob*0.1
        elif self.__cargo == 'semiexclusivo':
            sueldob = sueldob*0.2
        elif self.__cargo == 'exclusivo':
            sueldob = sueldob*0.5
        else: 
            raise Exception('Cargo no valido')
        
        return sueldob+sup
    

