class Evento:
    def __init__(self,fecha):   #borre tipo y seña porque me rompia la pija, despues vemos como lo agregamos
        self.fecha=fecha

    def __str__(self):
        return f"Tipo: {self.tipo}\nFecha: {self.fecha}\nServicios: {self.servicios}\nPrecioEvento: ${self.total} ARS\nSeñaEvento: ${self.senia} ARS\n"

     #Definimos los Getters
    def get_tipo(self):
        return self.tipo
    def get_fecha(self):
        return self.fecha
    def get_servicios(self):
        return self.servicios
    def get_total(self):
        return self.total
    def get_senia(self):
        return self.senia
    def get_servicioss(self):
        return self.servicioss

     #Definimos los Setters
    def set_tipo(self, dato):
        self.tipo = dato
    def set_fecha(self, dato):
        self.fecha = dato
    def set_servicios(self, dato):
        self.servicios = dato
    def set_total(self, dato):
        self.total = dato
    def set_senia(self, dato):
        self.senia = dato
    def set_servicioss(self, dato):
        self.servicioss = dato


    def disponible(self):
        with open("Reservas.txt", "r") as file:
            eventos = file.readlines()
            for evento in eventos:
                if self.fecha == evento.strip():
                    return False
        return True
    
    def reserva(self, cliente):
        with open("Reservas.txt", "a") as file:
            file.write(self.fecha + ", " + cliente.get_informacion_personal() + "\n")
            #file.write(f"{self.fecha},{cliente.get_informacion_personal}\n)