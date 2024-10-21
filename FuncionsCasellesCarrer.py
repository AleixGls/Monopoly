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
    MostrarInterficie()

def CalculPreuBanc(nomJugador): # Funció auxiliar
    pass
def PreuBanc(nomJugador):
    pass
    MostrarInterficie()
def CalculPreuJugador(nomJugador): # Funció auxiliar
    pass
def PreuJugador(nomJugador):
    pass
    MostrarInterficie()

def VendreAlBanc(IDCasella, nomJugador):
    pass
def VendreAJugador(IDCasellaDesti,nomJugadorVenedor,nomJugadorComprador):
    pass

def CaureEnCasellaCarrer(IDCasella, nomJugador):
    c = caselles[IDCasella]
    jug = jugadors[nomJugador]

    if c["propietari"] == "Banca":
        lstOpcions = ["passar","comprar terreny","preus"]
    
    elif c["propietari"] == nomJugador:
        lstOpcions = ["passar"]
        if c["nombre cases"] < 4 and jug["diners"] > c["comprar casa"]:
            lstOpcions.append("comprar casa")
        if c["nombre cases"] >= 2 and c["nombre hotels"] < 2 and jug["diners"] > c["comprar hotel"]:
            lstOpcions.append("comprar hotel")
        lstOpcions.append("preus")
    
    else:
        preuBase = c["lloguer hotel"]
        pagament = preuBase + c["lloguer casa"] * c["nombre cases"] + c["lloguer hotel"] * c["nombre hotels"]

        if jug["diners"] > pagament:
            jugadors[nomJugador]["diners"] -= pagament
            jugadors[c["propietari"]]["diners"] += pagament
            AfegirAHistorial(f"  \"{nomJugador[0]}\" paga {pagament}€ a \"{c["propietari"][0]}\"")
            lstOpcions = []
        else:
            AfegirAHistorial(f"  \"{nomJugador[0]}\" ha de pagar {pagament}€ a \"{c["propietari"][0]}\"")
            AfegirAHistorial(f"  \"{nomJugador[0]}\" no té prou diners")

            lstJugsCompradorsPossibles = []
            for jugadorComprador in jugadors:
                    if jugadorComprador != nomJugador and jugadors[jugadorComprador]["diners"] + jug["diners"] > pagament:
                        lstJugsCompradorsPossibles.append(jugador)
            
            if (CalculPreuBanc(nomJugador) + jug["diners"]) > pagament:
                lstOpcions = ["preu banc","preu jugador","vendre al banc"]
                for jugador in lstJugsCompradorsPossibles:
                    lstOpcions.append(f"vendre a {jugador}")
            elif (CalculPreuJugador(nomJugador) + jug["diners"]) > pagament and lstJugsCompradorsPossibles:
                AfegirAHistorial(f"  Vendre tot al banc no és prou per pagar")
                lstOpcions = ["preu jugador"]
                for jugador in lstJugsCompradorsPossibles:
                    lstOpcions.append(f"vendre a {jugador}")
            else:
                AfegirAHistorial(f"  Fins i tot venent tot a un altre jugador,")
                AfegirAHistorial(f"  \"{nomJugador[0]}\" no pot pagar")
                lstOpcions = ["declarar bancarrota"]

    return lstOpcions
