from controller.mainController import mainController
from controller.clientController import clientController
while __name__=="__main__":
    xd=clientController()
    tpi=mainController(xd)
    tpi.menu()

    