from Investigadores import Investigador
from Docentes import Docente
class DI(Docente,Investigador):
    __categoria_programa: str
    __importextra: int
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__categoria_programa = kwargs['cateprog']
        self.__importextra = kwargs['importextra']

    def getTipoAgente(self):
        return (self.__class__.__name__)
    
    def getCateProgr(self):
        return self.__categoria_programa
    
    def getimportextra(self):
        return self.__importextra
    
    def setimportextra(self,imx):
        self.__importextra = imx
    
    def toJson(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                    cuil= self.getcuil(),
                    apellido= self.getapellido(),
                    nombre= self.getnombre(),
                    sueldo= self.getsueldo(),
                    anti= self.getanti(),
                    carrera = self.getcarrera(),
                    cargo = self.getcargo(),
                    catedra = self.getcatedra(),
                    area = self.getarea(),
                    tipo = self.gettipo(),
                    cateprog = self.__categoria_programa,
                    importextra = self.__importextra
                )   
        )
        return d
    
    def calcuoSueldo(self):
        suma = (Docente.calcuoSueldo(self) + self.__importextra)
        return suma
    
    def mostrar(self):
        super().mostrar()
        print('Datos Docente Investigador:')
        print('Categoria en el programa de incentivos de investigación: {}, importe extra por docencia e investigación: {}'.format(self.__categoria_programa,self.__importextra))
