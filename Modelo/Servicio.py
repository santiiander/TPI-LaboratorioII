class Servicio:
    def __init__(self,nombre,precio,id) -> None:
        self.nombre=nombre
        self.precio=precio
        self.id=id
        
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nPrecio: {self.precio}\n"

     #Definimos los Getters
    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return self.precio
    def get_id(self):
        return self.id

     #Definimos los Setters
    def set_nombre(self, dato):
        self.nombre = dato
    def set_precio(self, dato):
        self.precio = dato
    def set_id(self, dato):
        self.id = dato

     #Procedemos a crear los eventos predeterminados
     #En el controlador  