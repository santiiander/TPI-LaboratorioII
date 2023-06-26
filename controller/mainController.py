#Este controlador incluye al Evento y al Servicio que trabajaran en conjunto
#metodo CalcularSeña
from model.Event import Event
from model.Service import Service
from view.mainView import mainView

import datetime as tiempo_fecha
from datetime import timedelta, datetime


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
            try:    
                self.view.menuPrincipal()
                dato=int(input())
                if dato == 1:
                    self.alquilarEvento()
                    self.generar_resumen()
                if dato == 2:
                    self.mostrar_fechas_disponibles()
                if dato == 3:
                    self.cancelarReservacion()
                if dato == 4:
                    self.view.despedida()
                    exit()
                if dato > 4:
                    self.view.input_invalido()
            except Exception:
                self.view.input_invalido()

    def alquilarEvento(self):
        self.client = self.client_controller.pedirDatosCliente()
        self.view.serviciosOfrecidos()
        self.run()

    def run(self):
        while True:
            try:
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
                    self.cantidad_servicio(servicio)
                elif eleccion == 2:
                    servicio = Decoracion
                    self.cantidad_servicio(servicio)
                elif eleccion == 3:
                    servicio = Cotillon
                    self.cantidad_servicio(servicio)
                elif eleccion == 4:
                    servicio = MaqHumo
                    self.cantidad_servicio(servicio)
                elif eleccion == 5:
                    servicio = Maquillaje
                    self.cantidad_servicio(servicio)
                elif eleccion == 6:
                    servicio = MusicaVivo
                    self.cantidad_servicio(servicio)
                elif eleccion == 7:
                    servicio = Buffet
                    self.cantidad_servicio(servicio)
                elif eleccion > 7:
                    self.view.input_invalido()
            except Exception:
                self.view.input_invalido()

        self.view.pedirFecha()   
        fecha_reservada = self.get_fecha_valida()
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
        return self.servicios
    
    def cantidad_servicio(self, servicio):
        self.view.elegircantidadServicios()
        cantidad = int(input())
        servicio.precio *= cantidad
        self.servicios.append(servicio)

    def calcularCosto(self):  #Llamar al getprecio de servicios
        self.modelService.get_precio()

    def pasarCostoTotal(self,suma):
        try:    
            with open("Reservas.txt", "a") as file:
                file.write(","+str(suma)+"\n") 
        except FileNotFoundError:
            self.view.file_not_found()

    def showsenia(self,suma):
        print("$"+str(suma*0.30))

    def calcular_costo_total(self):
        suma = 0
        for service in self.servicios:
            suma += service.precio
        return (suma + (suma * 0.31))  

    def mostrar_fechas_disponibles(self):
            try:    
                fecha_actual = tiempo_fecha.date.today()
                fecha_final = fecha_actual + tiempo_fecha.timedelta(days=20)
                fechas = []

                with open("Reservas.txt", "r") as file:
                    eventos = file.readlines()
                    fechas_reservadas = [evento.strip().split(",")[0] for evento in eventos]

                    while fecha_actual <= fecha_final:
                        fecha_formateada = fecha_actual.strftime("%d-%m-%Y")
                        if fecha_formateada not in fechas_reservadas:
                            fechas.append(fecha_formateada)
                        fecha_actual += tiempo_fecha.timedelta(days=1)

                if fechas:
                    self.view.fechasDisp()
                    for fecha in fechas:
                        print(fecha)
                else:
                    self.view.nofechadosmeses()
            except FileNotFoundError:
                self.view.no_hay_reservaciones()

    def crearFechasOcupadas(self):
        try:    
            with open("Reservas.txt", 'r') as file:
                for line in file:
                    x = line.split(",")
                    ocupadas = x[0]
                    self.fechasocupadas.append(ocupadas)  #Con esto podemos imprimir fechas ocupadas
                                                        #Por si el usuario se quiere ahorrar la molestia
        except FileNotFoundError:
            self.view.file_not_found()

    def printearFechasOcupadas(self):
        for i in self.fechasocupadas:
            print (i)

    def cancelarReservacion(self):
        try:
            self.view.pedirFecha()
            fecha = self.get_fecha_valida()
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
        except FileNotFoundError:
            self.view.file_not_found()

    def pagoSenia(self):
        self.view.printSenia()
        self.calcular_costo_total()
        self.view.senia()
        senia=(input())
        if senia == 1:
            pass
        if senia == 2:
            exit()


    #Quitar si no funciona 
    def generar_resumen(self):
        try:
            for i in self.servicios:
                print (i)

        except Exception:
            self.view.file_not_found()

    def get_fecha_valida(self):
        while True:
            fecha_reservada = input()
            try:
                day, month, year = map(int, fecha_reservada.split('-'))
                if (1 <= day <= 31) and (1 <= month <= 12) and (2000 <= year <= 2025):
                    input_fecha = datetime(year, month, day)
                    fecha_actual = datetime.now().date()
                    if input_fecha.date() > fecha_actual:
                        return fecha_reservada
                    else:
                        self.view.fecha_invalida()
                else:
                    self.view.fecha_invalida()
            except ValueError:
                self.view.fecha_invalida()



"""
    def generar_resumen(self):
        try:
            with open("Reservas.txt", "r") as file:
                reservas = file.readlines()

            for reserva in reservas:
                datos_reserva = reserva.strip().split(",")
                fecha_reservada = datos_reserva[0]
                servicios_contratados = servicio[1:-1]
                pago = datos_reserva[-1]

                print("Fecha reservada:", fecha_reservada)
                print("Servicios contratados:")
                for servicio in servicios_contratados:
                    print("-", servicio)
                    print("Pago:", pago)
                    print("")
        except IOError:
            print("Error al leer el archivo ")       
"""
                