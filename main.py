from Controlador.ServiceController import Sistema_de_reserva

def main():
    reservation_system = Sistema_de_reserva()
    reservation_system.run()

if __name__ == '__main__':
    main()