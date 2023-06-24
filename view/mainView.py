#Vista princial
class mainView:

    def menuPrincipal(self):
        print("\nMenu:")
        print("1) Alquilar servicios.")
        print("2) Mostrar Fechas Disponibles.")
        print("3) Mostrar Fechas Ocupadas.")
        print("4) Cancelar Reservacion de Evento.")
        print("5) Salir")

    def despedida(self):
        print("Gracias por utilizar nuestros servicios\nEquipo WhileTrue.")      

    def pedirNombre(self):
        print("Ingrese su Nombre: ")
    def pedirApellido(self):
        print("Ingrese su Apellido: ")
    def pedirDNI(self):
        print("Ingrese su DNI: ")    
    def pedirEmail(self):
        print("Ingese su MAIL: ")
    def pedirNumero(self):
        print("Ingrese su numero: ")

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

    def elegirHorasServicios(self):
        print("Ingrese el numero de horas que desea alquilar el servicio: ")
    
    def pedirFecha(self):
        print("Ingrese fecha de reservacion (DD-MM-AAAA): ")
    
    def fechaNoDisponible(self):
        print("La fecha elegida no esta disponible, ingrese otra.")

    def reservacionExitosa(self):
        print("Reservacion exitosa")
    
    def mostrarCostoTotal(self):
        print("Costo total:" ) 

    def fechasDisp(self):
        print("Fechas Disponibles: ")    

    def nofechadosmeses(self):
        print("No hay fechas disponibles en los porximos 2 meses.")    

    def reservacionCancelada(self):
        print("Su reservacion fue cancelada con exito!")
        self.despedida()    