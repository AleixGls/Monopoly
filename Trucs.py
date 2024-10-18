import random
from Dades import *
from Interficie import MostrarInterficie

def TrucAnarA(casella):
    pass

def TrucAfegirCasa(casa):
    if casa < 1 or casa > 4:
        print(f"ERROR, has seleccionat {casa} cases, has de seleccionar un numero del 1 al 4")
    else:
        print(f"Has afegit {casa} cases")

def TrucAfegirHotel(hotel):
    if hotel < 1 or hotel > 4:
        print(f"ERROR, has seleccionat {hotel} hotels, has de seleccionar un numero del 1 al 4")
    else:
        print(f"Has afegit {hotel} hotels")

def TrucSeguentJugador(jugador):
    pass

def TrucDinersJugador(jugador, diner):
    jugadors[jugador]["diner"] -= jugadors[jugador]["diner"]
    jugadors[jugador]["diner"] += diner

def TrucDinersBanca(diners):
    jugadors["Banca"]["diner"] -= jugadors["Banca"]["diner"]
    jugadors["Banca"]["diner"] += diners
