from Agentes import Agente
class PersonalA(Agente):
    __categoria: int

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__categoria = kwargs['categoria']

    def getcategoria(self):
        return self.__categoria
    
    def getTipoAgente(self):
        return (self.__class__.__name__)
    
    def __repr__(self):
        return repr(__class__)

    def mostrar(self):
        super().mostrar()
        print('Personal de Apoyo:')
        print('Categoria: {}'.format(self.__categoria))

    def toJson(self):
            d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                    cuil= self.getcuil(),
                    apellido= self.getapellido(),
                    nombre= self.getnombre(),
                    sueldo= self.getsueldo(),
                    anti= self.getanti(),
                    categoria = self.__categoria
                )
            )
            return d
    
    def calcuoSueldo(self):
        sueldob = self.getsueldo()
        cal = super().calcuoSueldo()
        if self.__categoria > 0 and self.__categoria < 11:
            sueldob = sueldob*0.1
        elif self.__categoria > 10 and self.__categoria < 21:
            sueldob = sueldob*0.2
        elif self.__categoria == 21 or self.__categoria == 22:
            sueldob = sueldob*0.3
        else: raise Exception('Categoria no valida')
        return sueldob+cal