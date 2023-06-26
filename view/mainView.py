#Vista princial
class mainView:

    def menuPrincipal(self):
        print("\n~~~~~Menu~~~~~")
        print("1) Alquilar servicios.")
        print("2) Mostrar Fechas Disponibles.")
        print("3) Cancelar Reservacion de Evento.")
        print("4) Salir\n")

    def despedida(self):
        print("Gracias por utilizar nuestros servicios\nEquipo WhileTrue.")      

    def pedirNombre(self):
        print("Ingrese el Nombre: ")
    def pedirApellido(self):
        print("Ingrese el Apellido: ")
    def pedirDNI(self):
        print("Ingrese el DNI: ")    
    def pedirEmail(self):
        print("Ingese el Mail: ")
    def pedirNumero(self):
        print("Ingrese el Numero: ")

    def serviciosOfrecidos(self):
        print("Servicios disponibles:")
        print("1) DJ")
        print("2) Decoracion")
        print("3) Cotillon")
        print("4) Maquina de humo")
        print("5) Maquillaje")
        print("6) Musica en vivo")
        print("7) Bufet")    

    def elegirServicio(self):
        print("Seleccione un servicio para alquilar del 1 al 7 o precione 0 para finalizar: ")

    def elegircantidadServicios(self):
        print("Ingrese cuantas veces requiere el servicio: ")
    
    def pedirFecha(self):
        print("Ingrese fecha de reservacion (DD-MM-AAAA): ")
    
    def fechaNoDisponible(self):
        print("La fecha elegida no esta disponible, pero le sugerimos las siguientes. ")
        

    def reservacionExitosa(self):
        print("Reservacion exitosa\n")
    
    def mostrarCostoTotal(self):
        print("Costo total:" ) 

    def fechasDisp(self):
        print("Fechas Disponibles: ")    

    def nofechadosmeses(self):
        print("No hay fechas disponibles en los proximos 2 meses.")    

    def reservacionCancelada(self):
        print("Su reservacion fue cancelada con exito.")
        self.despedida()    

    def errorCancelar(self):
        print("La reservacion ingresada no coincide con ninguna en nuestra base de datos\n")    

    def printSenia(self):
        print("Casi terminamos la reservacion, necesitamos que confirme el pago de la seña")
        print("Será de: ")

    def senia(self):
        print("¿Desea abonar la seña?\n1)Si\n2)No, cancelar reserva en curso.\n")    

    def mostrarReembolso(self, monto_reembolso):
        print(monto_reembolso)

    def view_senia(self, costo_total):
        print(f"Costo total: ${costo_total}")