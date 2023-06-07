from zope.interface import Interface

class IDirector(Interface):
    def modificarBasico(self, cuil, nuevoBasico):
       pass
    def modificarImporteExtra(self,cuil, nuevoImporteExtra):
       pass