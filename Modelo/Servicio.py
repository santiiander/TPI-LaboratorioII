class Servicio:
    def __init__(self,nombre,precio,id) -> None:
        self.nombre=nombre
        self.precio=precio
        
    def __str__(self) -> str:
        return f"Nombre: {self.nombre}\nPrecio: {self.precio}\n"

     #Definimos los Getters
    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return self.precio

     #Definimos los Setters
    def set_nombre(self, dato):
        self.nombre = dato
    def set_precio(self, dato):
        self.precio = dato

     #Procedemos a crear los eventos predeterminados
     #En el controlador  