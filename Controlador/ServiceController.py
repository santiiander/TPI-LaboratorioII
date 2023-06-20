from Modelo.Cliente import Cliente
from Modelo.Evento import Evento
from Modelo.Servicio import Servicio
from Vista.ServiceView import ServiceView
from Modelo.Servicio import DJ, Decoracion, Cotillon, Maquina_de_humo, Maquillaje, Musica_en_vivo, Bufet

import datetime

class ServiceController:
    def __init__(self,modelo=Servicio(),vista=ServiceView()):
        self.modelo=modelo
        self.vista=vista
        self.clientes = []
        self.fechas_reservadas = []

    def alquilar_servicios(self):
        self.vista.pedirNombre()
        nombre = input()
        self.vista.pedirApellido()
        apellido = input()
        self.vista.pedirDNI()
        dni = input()
        self.vista.pedirEmail()
        email = input()
        self.vista.pedirNumero()
        telefono = input()
        cliente = Cliente(nombre, apellido, dni, telefono, email)
        self.vista.serviciosOfrecidos()

        while True:
            self.vista.elegirServicio()
            
            eleccion = int(input())
            if eleccion == 0:
                break
            servicio = None

            if eleccion == 1:
                servicio = DJ()
            elif eleccion == 2:
                servicio = Decoracion()
            elif eleccion == 3:
                servicio = Cotillon()
            elif eleccion == 4:
                servicio = Maquina_de_humo()
            elif eleccion == 5:
                servicio = Maquillaje()
            elif eleccion == 6:
                servicio = Musica_en_vivo()
            elif eleccion == 7:
                servicio = Bufet()

            self.vista.elegirHorasServicios()
            horas = int(input())
            servicio.precio *= horas

            cliente.alquilar_servicio(servicio)

        self.vista.pedirFecha()
        fecha_reservada = input()
        evento = Evento(fecha_reservada)

        while not evento.disponible():
            self.vista.fechaNoDisponible()
            self.vista.pedirFecha()
            fecha_reservada = input()
            evento = Evento(fecha_reservada)

        evento.reserva(cliente)
        costo_total = cliente.calcular_costo_total()
        self.vista.reservacionExitosa()
        print(f"Costo total: ${costo_total}")
        self.clientes.append(cliente)
        self.fechas_reservadas.append(fecha_reservada)

    def mostrar_fechas_disponibles(self):
        fecha_actual = datetime.date.today()
        fecha_final = fecha_actual + datetime.timedelta(days=60)
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
            self.vista.fechasDisp()
            for fecha in fechas:
                print(fecha)
        else:
            self.vista.nofechadosmeses()
    

    def run(self):
        while True:
            self.vista.menuPrincipal()
            eleccion = int(input())
            if eleccion == 1:
                self.alquilar_servicios()
            elif eleccion == 2:
                self.mostrar_fechas_disponibles()
            elif eleccion ==3:
                pass
            elif eleccion == 4:
                self.vista.despedida()
                exit()