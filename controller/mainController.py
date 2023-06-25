#Este controlador incluye al Evento y al Servicio que trabajaran en conjunto
#metodo CalcularSeña
from model.Event import Event
from model.Service import Service
from view.mainView import mainView

import datetime

class mainController:
    def __init__(self,xd,modelEvent=Event(),modelService=Service(),view=mainView()):
        self.modelEvent=modelEvent
        self.modelService=modelService
        self.view=view
        self.xd=xd
        self.servicios = []
        self.fechas_reservadas = []
        self.fechasocupadas=[]


    def menu(self):
        while True:
            self.view.menuPrincipal()
            dato=int(input())
            if dato == 1:
                self.alquilarEvento()
            if dato == 2:
                self.mostrar_fechas_disponibles()
            if dato == 3:
                self.cancelarReservacion()
            if dato ==4:
                self.view.despedida()
                exit()

                    

    def alquilarEvento(self):
        self.client=self.xd.pedirDatosCliente()
        self.view.serviciosOfrecidos()
        self.pinga()

    def pinga(self):

        while True:
                self.view.elegirServicio()
                eleccion = int(input())
                if eleccion == 0:
                    break

                servicio = None
                Deejay=Service("DJ",5000)
                Decoracion=Service("Decoracion",25000)
                Cotillon=Service("Cotillon",5000)
                MaqHumo=Service("Maquina De Humo",10000)
                Maquillaje=Service("Maquillaje",3500)
                MusicaVivo=Service("Musica En Vivo",50000)
                Buffet=Service("Buffet",15000)

                if eleccion == 1:
                    servicio=Deejay
                elif eleccion == 2:
                    servicio = Decoracion
                elif eleccion == 3:
                    servicio = Cotillon
                elif eleccion == 4:
                    servicio = MaqHumo
                elif eleccion == 5:
                    servicio = Maquillaje
                elif eleccion == 6:
                    servicio = MusicaVivo
                elif eleccion == 7:
                    servicio = Buffet

                self.view.elegirHorasServicios()
                horas = int(input())
                servicio.precio *= horas
                self.alquilar_servicio(servicio)

        self.view.pedirFecha()   #VER SI LA FECHA NO ESTÁ RESERVADA YA.
        fecha_reservada = input() #CORREGIR

        


        """while not evento.disponible():
            self.view.fechaNoDisponible()   #Llamada evento
            self.view.pedirFecha()          #Revisar que no 
            fecha_reservada = input()       #Funciona
            evento = Event(fecha_reservada)
        """


        evento = Event(fecha_reservada)
        evento.reserva(self.client)                     #ACA PRINTEA EN EL TXT TODA LA INFO (SIN SALTO DE LINEA AHORA)
        self.pasarCostoTotal(self.calcular_costo_total())
        costo_total = self.calcular_costo_total()
        self.view.reservacionExitosa()
        self.fechas_reservadas.append(fecha_reservada) 
        print(f"Costo total: ${costo_total}")


        

        

        #self.client.append(self.client) PRESTAR ATENCION, BORRAR SI NO SIRVE

           

    
    def alquilar_servicio(self, servicio): #Revisar
        self.servicios.append(servicio)
        print(servicio) #BORRAR

    def calcularCosto(self):  #Llamar al getprecio de servicios
        self.modelService.get_precio()

    def pasarCostoTotal(self,suma):
        with open("Reservas.txt", "a") as file:
            file.write(","+str(suma)+"\n") #Agregar \n de nuevo despues

    def calcular_costo_total(self):
        for service in self.servicios:
            suma=0
            suma+=service.precio
        return suma    


    def mostrar_fechas_disponibles(self):
            fecha_actual = datetime.date.today()
            fecha_final = fecha_actual + datetime.timedelta(days=10)
            fechas = []

            with open("Reservas.txt", "r") as file:
                eventos = file.readlines()
                fechas_reservadas = [evento.strip().split(",")[0] for evento in eventos]

                while fecha_actual <= fecha_final:
                    fecha_formateada = fecha_actual.strftime("%d-%m-%Y")
                    if fecha_formateada not in fechas_reservadas:
                        fechas.append(fecha_formateada)
                    fecha_actual += datetime.timedelta(days=1)

            if fechas:
                self.view.fechasDisp()
                for fecha in fechas:
                    print(fecha)
            else:
                self.view.nofechadosmeses()


    def mostrarFechasOcupadas(self):
        with open("Reservas.txt", 'r') as file:
            for line in file:
                x=line.split(",")
                ocupadas=x[0]
                self.fechasocupadas.append(ocupadas)  #Con esto podemos imprimir fechas ocupadas
        self.printFechas()                            #Por si el usuario se quiere ahorrar la molestia

    def printFechas(self):
        for fecha in self.fechasocupadas:
            print(fecha)

    def cancelarReservacion(self):
        self.view.pedirFecha()
        fecha=input()
        with open("Reservas.txt", "r+") as archivo:
            lineas = archivo.readlines()
            archivo.seek(0)           #Nos posicionamos al principio del txt para buscar.
            for linea in lineas:
                if fecha not in linea:
                    archivo.write(linea)

                    #Agregar condicional de fecha para registrar rembolso o no

                    self.view.reservacionCancelada()
                else:
                    self.view.errorCancelar()
                
            archivo.truncate()
            archivo.close()

    def pagoSenia(self):
        self.view.printSenia()
        self.calcular_costo_total()
        self.view.senia()
        senia=(input())
        if senia==1:
            pass
        if senia==2:
            exit()



        