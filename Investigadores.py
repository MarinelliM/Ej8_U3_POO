from Agentes import Agente
class Investigador(Agente):
    __area_investigacion: str
    __tipo_investigacion: str

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__area_investigacion = kwargs['area']
        self.__tipo_investigacion = kwargs['tipo']

    def getTipoAgente(self):
        return (self.__class__.__name__)

    def getarea(self):
        return self.__area_investigacion
    
    def gettipo(self):
        return self.__tipo_investigacion
    
    def toJson(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                        cuil = self.getcuil(),
                        apellido = self.getapellido(), 
                        nombre = self.getnombre(),
                        sueldo = self.getsueldo(),
                        anti = self.getanti(),
                        area = self.__area_investigacion,
                        tipo = self.__tipo_investigacion
                    )
            )
        return d

    def mostrar(self):
        super().mostrar()
        print('Datos Investigador:')
        print('Area de investigacion: {}, Tipo de investigacion: {}' .format(self.__area_investigacion,self.__tipo_investigacion))
