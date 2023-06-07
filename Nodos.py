from Agentes import Agente
class Nodo:
    __nodo: Agente
    __siguiente: object

    def __init__(self,nodo) -> None:
        self.__nodo = nodo
        self.__siguiente = None

    def getnodo(self):
        return self.__nodo
    
    def getsiguiente(self):
        return self.__siguiente
    
    def setsiguiente(self, sig):
        self.__siguiente = sig
