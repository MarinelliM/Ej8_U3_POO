from Menu import Menu
from Tesorero import ITesorero
from ObjectEncoder import ObjectEncoder
from Director import IDirector
from Lista import Lista
if __name__ == '__main__':    
    oe = ObjectEncoder()
    lista = Lista()
    tesorero = ITesorero(lista)
    director = IDirector(lista)
    oe.decodificarDiccionario(lista)
    menu = Menu()
    menu.inicializar()
    print('Usuario/Contraseña para Tesorero: uTesoreso/ag@74ck\n')
    print('Usuario/contraseña para Director: uDirector/ufC77#!1\n')
    Usuario = str(input('Ingrese usuario:'))
    Contraseña = str(input('Ingrese contraseña:'))
    print('\n')
    uc = Usuario+'/'+Contraseña
    if uc == 'uTesoreso/ag@74ck':
        cuil = str(input('Ingrese un cuil a buscar:'))
        tesorero.gastosSueldoPorEmpleado(cuil)
    elif uc == 'uDirector/ufC77#!1':
        menu.OpsDirector(director)


