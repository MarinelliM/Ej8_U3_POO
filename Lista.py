from Agentes import Agente
from DocentesInvestigadores import DI
from Investigadores import Investigador
from Nodos import Nodo
#from Interfaz import Interfaz
from zope.interface import implementer
from Tesorero import ITesorero
from Director import IDirector

@implementer(ITesorero)
@implementer(IDirector)
#@implementer(Interfaz)
class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __tope: int
    __indice: int

    def __init__(self) -> None:
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getnodo()
            self.__actual = self.__actual.getsiguiente()
            return dato
        
    def agregarElemento(self,persona):
        nodo=Nodo(persona)
        nodo.setsiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1

    def insertarElemento(self,persona,posicion):
        i = 0
        aux:Nodo
        aux = self.__comienzo
        if posicion < 0 or posicion > self.__tope:
                raise Exception('La posicion no es valida')
        else:
            
            if posicion == 0:
                self.agregarElemento(persona)
                i = posicion
            
            while i < posicion-1:
                aux = aux.getsiguiente()
                i += 1
            nodo = Nodo(persona)
            nodo.setsiguiente(aux.getsiguiente())
            aux.setsiguiente(nodo)
            #Se verifica si la posición es igual a la última posición.
            # Si es así, se actualiza la referencia al nodo actual
            # para que apunte al nuevo nodo, ya que el nuevo nodo ha sido insertado en la última posición.
            if posicion == self.__tope:
                self.__actual = nodo        
            self.__tope+=1

    def mostrarLista(self):
        print('\n')
        aux = self.__comienzo
        while aux != None:
            nodo = aux.getnodo()
            nodo.mostrar()
            aux = aux.getsiguiente()
            print('\n')
    
    def mostrarElemento(self,posicion):
        if posicion < 0 or posicion > self.__tope:
                raise Exception('La posicion no es valida')
        else:
            nodo = self.buscarnodo(posicion)
            noda = nodo.getnodo()
            if noda != None:
                print("El Tipo de Agente que se encuentra en la posicion: {}, es: {}".format(posicion,noda.getTipoAgente()))

    def buscarnodo(self,pos):
        actual:Nodo
        actual = self.__comienzo
        while actual != None and pos != 0:
            actual = actual.getsiguiente()
            pos -= 1
        if actual == None:
            raise Exception("Posicion invalida")
        return actual

    def GenerarListado(self, carrera):
        aux:Nodo
        aux = self.__comienzo
        print('\n')
        while aux != None:
            nodo = aux.getnodo()
            if isinstance(nodo,DI) and carrera == nodo.getcarrera():
                nodo.mostrar()
                print('\n')
            aux = aux.getsiguiente()
            

    def BuscarXarea(self,area):
        aux: Nodo
        cont1 = 0
        c2 = 0
        aux = self.__comienzo
        while aux != None:
            nodo = aux.getnodo()
            if type(nodo) is DI:
                if nodo.getarea() == area:
                    cont1 += 1
            elif type(nodo) is Investigador:
                if nodo.getarea() == area:
                    c2 += 1
            aux = aux.getsiguiente()
        print('La cantidad de Docentes Investigadores trabajando en el área: {}, es de {}'.format(area,cont1))
        print('La cantidad de Investigadores trabajando en el área: {}, es de: {}'.format(area,c2))

    def listaOrdenada(self):
        aux: Nodo
        lista = []
        aux = self.__comienzo

        while aux != None:
            dato = aux.getnodo()
            #dato.calcuoSueldo()
            lista.append(dato)
            aux = aux.getsiguiente()

        listaord = sorted(lista)
        for elem in listaord:
            print("Nombre y apellido: {}, Tipo de agente: {}, Sueldo:{}".format(elem.getnombrecompleto(), elem.getTipoAgente(), elem.calcuoSueldo()))

    def BuscarXcategoria(self,categoria):
        aux:Nodo
        imp = 0
        aux = self.__comienzo
        while aux != None:
            nodo = aux.getnodo()
            if isinstance(nodo,DI):
                if nodo.getCateProgr() == categoria:
                    print('Nombre y apellido: {}, importe extra por docencia e investigación: {}'.format(nodo.getnombrecompleto(),nodo.getimportextra()))
                    imp += nodo.getimportextra()
            aux = aux.getsiguiente()
        print('Total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada: {}'.format(imp))

    def guardarLista(self):
        aux: Nodo
        lista = []
        aux = self.__comienzo
        while aux != None:
            nodo = aux.getnodo()
            if isinstance(nodo, Agente):
                dicc = nodo.toJson()
            else:
                raise ValueError('Tipo de vehículo no válido')

            lista.append(dicc)
            aux = aux.getsiguiente()
            print(lista)
        return lista
    
    def gastosSueldoPorEmpleado(self,cuil):
        aux = self.__comienzo
        while aux != None:
            nodo = aux.getnodo()
            if cuil == nodo.getcuil():
                print('gasto de sueldos para el agente al que pertenece dicho número de cuil:{}'.format(nodo.calcuoSueldo()))
                aux = None
            else: aux = aux.getsiguiente()

    def modificarBasico(self,cuil, nuevoBasico):
       aux = self.__comienzo
       while aux != None:
           nodo = aux.getnodo()
           if nodo.getcuil() == cuil:
               nodo.setbasico(nuevoBasico)
               nodo.mostrar()
               aux = None
           else: aux = aux.getsiguiente()

    def modificarImporteExtra(self,cuil, nuevoImporteExtra):
       aux = self.__comienzo
       while aux != None:
           nodo = aux.getnodo()
           if cuil == nodo.getcuil() and isinstance(nodo,DI):
               nodo.setimportextra(nuevoImporteExtra)
               nodo.mostrar()
               aux = None
           else: aux = aux.getsiguiente()

