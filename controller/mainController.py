#Este controlador incluye al Evento y al Servicio que trabajaran en conjunto
#metodo CalcularSeña
from model.Event import Event
from model.Service import Service
from view.mainView import mainView

from datetime import datetime, timedelta

class mainController:
    def __init__(self, client_controller, modelEvent=Event(), modelService=Service(), view=mainView()):
        self.modelEvent = modelEvent
        self.modelService = modelService
        self.view = view
        self.client_controller = client_controller
        self.servicios = []
        self.fechas_reservadas = []
        self.fechasocupadas = []

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
            if dato == 4:
                self.view.despedida()
                exit()

    def alquilarEvento(self):
        self.client = self.client_controller.pedirDatosCliente()
        self.view.serviciosOfrecidos()
        self.run()

    def run(self):
        while True:
                self.view.elegirServicio()
                eleccion = int(input())
                if eleccion == 0:
                    break
                servicio = None
                
                Deejay = Service("DJ",5000)
                Decoracion = Service("Decoracion",25000)
                Cotillon = Service("Cotillon",5000)
                MaqHumo = Service("Maquina De Humo",10000)
                Maquillaje = Service("Maquillaje",3500)
                MusicaVivo = Service("Musica En Vivo",50000)
                Buffet = Service("Buffet",15000)

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

                self.view.elegircantidadServicios()
                cantidad = int(input())
                servicio.precio *= cantidad
                self.alquilar_servicio(servicio)

        self.view.pedirFecha()   
        fecha_reservada = input() 
        self.crearFechasOcupadas()

        for i in self.fechasocupadas:
            while fecha_reservada == i:
                self.view.fechaNoDisponible()
                self.mostrar_fechas_disponibles()
                self.view.pedirFecha()
                fecha_reservada = input()

        evento = Event(fecha_reservada)
        self.view.printSenia()
        self.showsenia(self.calcular_costo_total())
        self.view.senia()
        senia = int(input())

        if senia == 1:

            evento.reserva(self.client)                     
            self.pasarCostoTotal(self.calcular_costo_total())
            costo_total = self.calcular_costo_total()      #ACA PRINTEA EN EL TXT TODA LA INFO (SIN SALTO DE LINEA AHORA)
            self.view.reservacionExitosa()
            self.fechas_reservadas.append(fecha_reservada) 
            self.view.view_senia(costo_total)  

        else:
            self.view.reservacionCancelada()

    def alquilar_servicio(self, servicio):
        self.servicios.append(servicio)


    def calcularCosto(self):  #Llamar al getprecio de servicios
        self.modelService.get_precio()

    def pasarCostoTotal(self,suma):
        with open("Reservas.txt", "a") as file:
            file.write(","+str(suma)+"\n") 

    def showsenia(self,suma):
        print("$"+str(suma*0.30))

    def calcular_costo_total(self):
        for service in self.servicios:
            suma = 0
            suma += service.precio
        return (suma + (suma * 0.31))  

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

    def crearFechasOcupadas(self):
        with open("Reservas.txt", 'r') as file:
            for line in file:
                x = line.split(",")
                ocupadas = x[0]
                self.fechasocupadas.append(ocupadas)  #Con esto podemos imprimir fechas ocupadas
                                                      #Por si el usuario se quiere ahorrar la molestia
    def printearFechasOcupadas(self):
        for i in self.fechasocupadas:
            print (i)

    def cancelarReservacion(self):
        self.view.pedirFecha()
        fecha = input()
        porcentaje_reembolso = 0
        fecha_actual = datetime.now().date()

        with open("Reservas.txt", "r+") as archivo:
            lineas = archivo.readlines()
            archivo.seek(0)

            for linea in lineas:
                datos = linea.strip().split(",")
                reserva_fecha = datetime.strptime(datos[0], "%d-%m-%Y").date()
                    
                if fecha != datos[0]:
                    archivo.write(linea)
                else:
                    fecha_a_cancelar = reserva_fecha - timedelta(days=15)
                    if fecha_a_cancelar < fecha_actual:
                        porcentaje_reembolso = 0
                    else:
                        porcentaje_reembolso = 0.06

            archivo.truncate()
            archivo.close()
            self.view.reservacionCancelada()

        if porcentaje_reembolso > 0:
            monto_total = float(datos[-1])
            monto_reembolso = monto_total * porcentaje_reembolso
            self.view.mostrarReembolso(monto_reembolso)
        elif porcentaje_reembolso == 0:
            self.view.mostrarReembolso(porcentaje_reembolso)
        else:
            self.view.errorCancelar()

    def pagoSenia(self):
        self.view.printSenia()
        self.calcular_costo_total()
        self.view.senia()
        senia=(input())
        if senia == 1:
            pass
        if senia == 2:
            exit()