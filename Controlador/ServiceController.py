'''
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
'''
                
"""
    Ejemplo lectura (Santiago)
    def guardarArchivo(self):  #Revisar
        with open ("pacientes.txt","w") as archivo:
            for paciente in self.pacientes:
                nombre=paciente.nombre
                edad=paciente.edad
                dni=paciente.dni
                genero=paciente.genero
                peso=paciente.peso
                altura=paciente.altura
                x=f"{nombre};{edad};{dni};{genero};{peso};{altura}\n"
                archivo.writelines(x)
    
"""    
from Modelo.Cliente import Cliente
from Modelo.Evento import Evento
from Modelo.Servicio import DJ, Decoracion, Cotillon, Maquina_de_humo, Maquillaje, Musica_en_vivo, Bufet

import datetime

class Sistema_de_reserva:
    def __init__(self):
        self.clientes = []
        self.fechas_reservadas = []

    def alquilar_servicios(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        DNI = input("Ingrese su DNI: ")
        email = input("Ingrese su email: ")
        telefono = input("Ingrese su telefono: ")

        cliente = Cliente(nombre, apellido, DNI, email, telefono)

        print("Servicios disponibles:")
        print("1) DJ")
        print("2) Decoracion")
        print("3) Cotillon")
        print("4) Maquina de humo")
        print("5) Maquillaje")
        print("6) Musica en vivo")
        print("7) Bufet")

        while True:
            eleccion = int(input("Seleccione un servicio para alquilar del 1 al 7 o precione 0 para finalizar: "))

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

            horas = int(input("Ingrese el numero de horas que desea alquilar el servicio: "))
            servicio.precio *= horas

            cliente.alquilar_servicio(servicio)

        fecha_reservada = input("Ingrese fecha de reservacion (DD-MM-AAAA): ")
        evento = Evento(fecha_reservada)

        while not evento.disponible():
            print("La fecha elegida no esta disponible, ingrese otra.")
            fecha_reservada = input("Ingrese fecha de reservacion (DD-MM-AAAA): ")
            evento = Evento(fecha_reservada)

        evento.reserva(cliente)
        costo_total = cliente.calcular_costo_total()
        print("Reservacion exitosa")
        print(f"Costo total: ${costo_total}")

        self.clientes.append(cliente)
        self.fechas_reservadas.append(fecha_reservada)

    def mostrar_fechas_disponibles(self):
        fecha_actual = datetime.date.today()
        fecha_final = fecha_actual + datetime.timedelta(dias=60)
        fechas = []

        with open("Reservas.txt", "r") as file:
            eventos = file.readlines()
            fechas_reservadas = [evento.strip().split(",")[0] for evento in eventos]

            while fecha_actual <= fecha_final:
                fecha_formateada = fecha_actual.strftime("%d-%m-%Y")
                if fecha_formateada not in fechas_reservadas:
                    fechas.append(fecha_formateada)
                fecha_actual += datetime.timedelta(dias=1)

        if fechas:
            print("Fechas disponibles:")
            for fecha in fechas:
                print(fecha)
        else:
            print("No hay fechas disponibles en los porximos 2 meses.")

    def end(self):
        print("Gracias por usas nuestros servicios.")

    def run(self):
        while True:
            print("\nMenu:")
            print("1) Alquilar servicios.")
            print("2) Mostrar fechas disponibles.")
            print("3) Finalizar.")

            eleccion = int(input())

            if eleccion == 1:
                self.alquilar_servicios()
            elif eleccion == 2:
                self.mostrar_fechas_disponibles()
            elif eleccion == 3:
                self.end()
                break