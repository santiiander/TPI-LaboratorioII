from Modelo.Servicio import Servicio
from Vista.ServiceView import ServiceView

class ServiceController():
    def __init__(self,view=ServiceView(),model=Servicio()):
        self.view=view
        self.model=model
        self.serviciosEstablecidos=[]
        services=[]

    def cargaServicios(self):
        self.view.MenuService()

    def inputServices(self):
        return int(input())
    
    def inputStrServices(self):
        return str(input())

    def menuPrincipal(self):
        self.insertarServicios()
        self.view.MenuEjecicion()
        x=self.inputServices()
        if x==1:
            pass #Ejecucion principal (Todo)
        if x==2:
            pass #Consultar Si hay fecha disponible (Solo eso)
        if x==3:
            self.view.despedida()
            exit()
        if x==4:
            #Menu prueba
            self.recorrerServicios()

    def insertarServicios(self):
        Cotillon=Servicio("Cotillon",10)
        Dj=Servicio("DJ",15)
        Decoracion=Servicio("Decoracion",20)
        MaqHumo=Servicio("Maquina de Humo",25)
        Maquillaje=Servicio("Maquillaje",30)
        MusicaEnVivo=("Musica en Vivo",35)
        Bufet=Servicio("Bufet",35)
        f=[Cotillon,Dj,Decoracion,MaqHumo,Maquillaje,MusicaEnVivo,Bufet]
        self.serviciosEstablecidos.append(f)

    def recorrerServicios(self):
        self.view.pedirInput()
        a=self.inputStrServices()
        for Servicios in self.serviciosEstablecidos:
            if a==Servicios:
                print("Queso xd")

        