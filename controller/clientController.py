from model.Client import Client
from view.mainView import mainView
class clientController:
    def __init__(self,model=Client(),view=mainView()):
        self.model=model
        self.view=view

    def pedirDatosCliente(self):
        self.view.pedirNombre()
        nombre = input()
        self.view.pedirApellido()
        apellido = input()
        self.view.pedirDNI()    #Pide datos personales del cliente
        dni = input()
        self.view.pedirEmail()
        email = input()
        self.view.pedirNumero()
        telefono = input()
        client = Client(nombre, apellido, dni, telefono, email)
        return client