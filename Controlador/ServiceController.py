from Modelo.Servicio import Servicio
from Vista.ServiceView import ServiceView

class ServiceController():
    def __init__(self,view=ServiceView(),model=Servicio()):
        self.view=view
        self.model=model
        services=[]

    def cargaServicios(self):
        self.view.MenuService()

    def inputServices(self):
        return int(input())

    def menuPrincipal(self):
        self.view.MenuEjecicion()
        x=self.inputServices()
        if x==1:
            pass #Ejecucion principal (Todo)
        if x==2:
            pass #Consultar Si hay fecha disponible (Solo eso)
        if x==3:
            self.view.despedida()
            exit()