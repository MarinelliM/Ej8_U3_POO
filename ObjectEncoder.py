from pathlib import Path
import json
from Lista import Lista
from Docentes import Docente
from Investigadores import Investigador
from DocentesInvestigadores import DI
from PersonalApoyo import PersonalA

class ObjectEncoder(object):

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario
        
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            print("--Archivo guardado correctamente--")
            destino.close()

    def decodificarDiccionario(self,lista: Lista):
        diccionario = self.leerJSONArchivo("Ej8/personal.json")
        for elem in diccionario:
            if '__class__' not in elem:
                print("No se encuentra el diccionario")
            else:
                class_name=elem['__class__']
                class_=eval(class_name)
                if class_name == "Docente":
                    atributos = elem['__atributos__']
                    T = class_(**atributos)
                    lista.agregarElemento(T)
                elif class_name == "Investigador":
                    atributos = elem['__atributos__']
                    T = class_(**atributos)
                    lista.agregarElemento(T)
                elif class_name == "DI":
                    atributos = elem['__atributos__']
                    T = class_(**atributos)
                    lista.agregarElemento(T)
                elif class_name == "PersonalA":
                    atributos = elem['__atributos__']
                    T = class_(**atributos)
                    lista.agregarElemento(T)
                # elif class_name == DI:
                #     atributos = elem['__atributos__']
                #     T = class_(**atributos)
                #     lista.agregarElemento(T)

    #Otra forma de hacerlo
    def mostrarJson(self,ar):
        try:
            # # Abre el archivo JSON y carga en datos el contenido
            with open(ar) as archivo:
                datos = json.load(archivo)

            # # Muestra los datos de manera legible
            print(json.dumps(datos, indent=4))
        except FileNotFoundError:
            print("El archivo JSON no existe.")
       