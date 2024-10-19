from Dades import *
from Interficie import AfegirAHistorial
from Interficie import MostrarInterficie
#--------------------------------------------------------------------------------------------------

def ComprarTerreny(IDCasella, nomJugador):
    pass
def ComprarCasa(IDCasella, nomJugador):
    pass
def ComprarHotel(IDCasella, nomJugador):
    pass

def Preus(IDCasella):
    pass
def PreuBanc(nomJugador):
    pass
def PreuJugador(nomJugador):
    pass

def VendreAlBanc(IDCasella, nomJugador):
    pass
def VendreAJugador(IDCasellaDesti,nomJugadorVenedor,nomJugadorComprador):
    pass

def CaureEnCasellaCarrer(IDCasella, nomJugador):
    if caselles[IDCasella]["propietari"] == "Banca":
        lstOpcions = ["passar","comprar terreny"]
    elif caselles[IDCasella]["propietari"] == nomJugador:
        pass
    else:
        pass

    return lstOpcions
