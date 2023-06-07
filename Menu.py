from Lista import Lista
from Docentes import Docente
from Investigadores import Investigador
from DocentesInvestigadores import DI
from PersonalApoyo import PersonalA
#from Interfaz import Interfaz
from ObjectEncoder import ObjectEncoder
from Director import IDirector

class Menu:
    __lista: Lista
    #__interfaz: Interfaz
    __objEnc: ObjectEncoder

    def __init__(self) -> None:
        self.__lista = Lista()
        #self.__interfaz = Interfaz(self.__lista)
        self.__objEnc = ObjectEncoder()

    def opciones(self):
        print("0. Salir")
        print("1. Insertar a agentes a la colección.")
        print("2. Agregar agentes a la colección.")
        print("3. Mostrar tipo de agente en posicion")
        print("4. Docentes investigadores de una carrera")
        print("5. Investigadores y docentes investigadores de una area de investigacion")
        print("6. Listar personal")
        print("7. Calcular importe extra de categoria de investigacion")
        print("8. Guardar datos")
        print('9. Usar Interfaz de Director\n')

    def inicializar(self):
        self.__objEnc.mostrarJson('personal.json')
        self.__objEnc.decodificarDiccionario(self.__lista)
        self.__lista.mostrarLista()

    def menu(self):
        
        self.opciones()
        op = int(input('Ingrese una opcion:'))
        
        while op != 0:
            if op == 1:
                ag = self.op1()
                pos = int(input('Ingrese la posicion donde quiere almacenar el elemento:'))
                print('\n')
                self.__interfaz.insertarElemento(ag,pos)
                self.__interfaz.mostrarElemento(pos)
            elif op == 2:
                ag = self.op1()
                self.__interfaz.agregarElemento(ag)
            elif op == 3:
                pos = int(input('Ingrese una posicion para mostrar el tipo de agente:'))
                self.__interfaz.mostrarElemento(pos)
            elif op == 4:
                print('Carreras: LCC, LSI o TPW\n')
                carrera = str(input('Ingrese el nombre de una carrera:'))
                self.__lista.GenerarListado(carrera)
            elif op == 5:
                print('Áreas: Estructuras o Computacional\n')
                area = str(input('Ingrese el area:'))
                self.__lista.BuscarXarea(area)
            elif op == 6:
                self.__lista.listaOrdenada()
            elif op == 7:
                print('Categorias en el programa de incentivos de investigación: (I, II, IV)\n')
                categoria = str(input('Ingrese una categoria:'))
                self.__lista.BuscarXcategoria(categoria)
            elif op == 8:
                diccionario = self.__lista.guardarLista()
                self.__objEnc.guardarJSONArchivo(diccionario,'nuevosagentes.json')
                self.__objEnc.mostrarJson('nuevosagentes.json')
            else: 
                print('Opcion incorrecta\n')
            self.opciones()
            op = int(input('Ingrese una opcion:'))
        print('Fin del Programa\n')

    def op1(self):
        atributos = {   
            'cuil': str(input('Ingrese un cuil:')),
            'apellido': str(input('Ingrese un apellido:')),
            'nombre': str(input('Ingrese un nombre:')),
            'sueldo': int(input('Ingrese un sueldo:')),
            'anti': int(input('Ingrese antiguedad:'))
        }
        print('\n')
        print('Los tipos de Agente aceptables son: Docente, PersonalA, Investigador y DI\n')
        tipo = str(input('Ingrese un tipo de Agente:'))
        Agente = None
        if tipo == 'Docente':
            atributos['carrera'] = str(input('Ingrese la carrera:'))
            atributos['cargo'] = str(input('Ingrese el cargo:'))
            atributos['catedra'] = str(input('Ingrese la catedra:'))
            Agente = Docente(**atributos)
            
        elif tipo == 'PersonalA':
            atributos['categoria'] = str(input('Ingrese la categoria:'))
            Agente = PersonalA(**atributos)
            
        elif tipo == 'Investigador':
            atributos['area'] = str(input('Ingrese el area de investigacion:'))
            atributos['tipo'] = str(input('Ingrse el tipo de investigacion:'))
            Agente = Investigador(**atributos)
            
        elif tipo == 'DI':
            atributos['carrera'] = str(input('Ingrese la carrera:'))
            atributos['cargo'] = str(input('Ingrese el cargo:'))
            atributos['catedra'] = str(input('Ingrese la catedra:'))
            atributos['area'] = str(input('Ingrese el area de investigacion:'))
            atributos['tipo'] = str(input('Ingrse el tipo de investigacion:'))
            atributos['cateprog'] = str(input('Ingrese el programa:'))
            atributos['importextra'] = int(input('Ingrese el importe extra:'))
            Agente = DI(**atributos)
           
        else: raise Exception('Tipo de Agente ingresado incorrecto')

        return Agente
    
    def OpsDirector(self,director:IDirector):
        print('0. Salir')
        print('1. Modificar el sueldo básico de todos los agentes')
        print('2. Modificar el importe extra que se paga a un docente investigador\n')
        op = int(input('Ingrese una opcion:'))
        while op != 0:
            if op == 1:
                cuil = str(input('Ingrese el cuil a buscar:'))
                nuevoBasico = int(input('Ingrese el nuevo sueldo basico que tendra el agente:'))
                print('\n')
                director.modificarBasico(cuil,nuevoBasico)
            elif op == 2:
                cuil = str(input('Ingrese el cuil a buscar:'))
                nuevoBasico = int(input('Ingrese el nuevo importe extra que tendra el agente:'))
                print('\n')
                director.modificarImporteExtra(cuil,nuevoBasico)
            else: 
                print('Opcion incorrecta\n')
            print('0. Salir')
            print('1. Modificar el sueldo básico de todos los agentes')
            print('2. Modificar el importe extra que se paga a un docente investigador\n')
            op = int(input('Ingrese una opcion:'))
        print('Fin del Programa\n')

