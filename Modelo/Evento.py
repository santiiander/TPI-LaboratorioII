class Evento:
    def __init__(self,tipo,fecha,servicios,total,senia,id):
        self.tipo=tipo
        self.fecha=fecha
        self.servicios=servicios
        self.total=total
        self.senia=senia
        self.id=id
        servicioss=[]

    def __str__(self) -> str:
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
    def get_id(self):
        return self.id
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
    def set_id(self, dato):
        self.id = dato
    def set_servicioss(self, dato):
        self.servicioss = dato

Evento1=Evento("Congreso","11-03-2024","no se como usar esto",10000,3333,1)

print(Evento1)