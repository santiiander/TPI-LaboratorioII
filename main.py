from controller.mainController import mainController
from controller.clientController import clientController
while __name__=="__main__":
    client_controller = clientController()
    tpi = mainController(client_controller)
    tpi.menu()