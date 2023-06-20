class Servicio:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

    def calcular_costo(self):
        return self.precio
        
    def __str__(self):
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

class DJ(Servicio):
    def __init__(self):
        super().__init__("DJ", 15)

class Decoracion(Servicio):
    def __init__(self):
        super().__init__("Decoracion", 20)

class Cotillon(Servicio):
    def __init__(self):
        super().__init__("Cotillon", 10)

class Maquina_de_humo(Servicio):
    def __init__(self):
        super().__init__("Maquina de humo", 25)

class Maquillaje(Servicio):
    def __init__(self):
        super().__init__("Maquillaje", 30)

class Musica_en_vivo(Servicio):
    def __init__(self):
        super().__init__("Musica en vivo", 35)

class Bufet(Servicio):
    def __init__(self):
        super().__init__('Bufet', 35)