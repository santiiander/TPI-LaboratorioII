class Cliente:
    def __init__(self,nombre,apellido,dni,telefono,email,id):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.telefono=telefono
        self.email=email
        self.id=id

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nDNI: {self.dni}\nTeléfono: {self.telefono}\nEMAIL: {self.email}\n"

Yo=Cliente("Santiago","Andermatten",44297673,3472468850,"santiagoandermatten1@gmail.com",1)
print(Yo)     