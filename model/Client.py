class Client:
    def __init__(self,nombre="",apellido="",dni=0,telefono=0,email=""):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.telefono=telefono
        self.email=email

    def __str__(self):
        return f"{self.nombre},{self.apellido},{self.dni},{self.telefono},{self.email}"

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

    