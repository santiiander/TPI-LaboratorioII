class Cliente:
    def __init__(self,nombre,apellido,dni,telefono,email):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.telefono=telefono
        self.email=email
        self.servicios = []

    def alquilar_servicio(self, servicio):
        self.servicios.append(servicio)

    def calcular_costo_total(self):
        costo_total = 0
        for servicio in self.servicios:
            costo_total += servicio.calcular_costo()
        return costo_total

    def get_informacion_personal(self):
        return f"Nombre: {self.nombre} {self.apellido}, DNI: {self.dni}, Email: {self.email}, Telefono: {self.telefono}"





    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nDNI: {self.dni}\nTeléfono: {self.telefono}\nEMAIL: {self.email}\n"

    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def get_nombre(self):
        return self.nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_apellido(self):
        return self.apellido

    def set_dni(self, dni):
        self.dni = dni

    def get_dni(self):
        return self.dni

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_telefono(self):
        return self.telefono

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

'''
Yo=Cliente("Santiago","Andermatten",44297673,3472468850,"santiagoandermatten1@gmail.com")
print(Yo)
'''     