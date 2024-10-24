from Dades import *
from Transferencies import Transferencia
from Interficie import MostrarInterficie
#--------------------------------------------------------------------------------------------------

def ComprarTerreny(IDCasella, nomJugador):
    c = caselles[IDCasella]
    preu = c["comprar terreny"]
    caselles[IDCasella]["propietari"] = nomJugador
    jugadors[nomJugador]["carrers"].append(c["nom"])
    Transferencia(nomJugador, "Banca", preu)
    AfegirAHistorial(f"  \"{nomJugador[0]}\" compra el terreny per {preu}€")
def ComprarCasa(IDCasella, nomJugador):
    preu = caselles[IDCasella]["comprar casa"]
    caselles[IDCasella]["nombre cases"] += 1
    Transferencia(nomJugador, "Banca", preu)
    AfegirAHistorial(f"  \"{nomJugador[0]}\" compra 1 casa per {preu}€")
def ComprarHotel(IDCasella, nomJugador):
    preu = caselles[IDCasella]["comprar hotel"]
    caselles[IDCasella]["nombre hotels"] += 1
    Transferencia(nomJugador, "Banca", preu)
    AfegirAHistorial(f"  \"{nomJugador[0]}\" compra 1 hotel per {preu}€")

def Preus(IDCasella):
    c = caselles[IDCasella]
    AfegirAHistorial(f"  Preu terreny: {c["comprar terreny"]}")
    AfegirAHistorial(f"  Preu casa: {c["comprar casa"]}")
    AfegirAHistorial(f"  Preu hotel: {c["comprar hotel"]}")
    MostrarInterficie()

def CaureEnCasellaCarrer(IDCasella, nomJugador):
    c = caselles[IDCasella]
    jug = jugadors[nomJugador]

    if c["propietari"] == "Banca":
        lstOpcions.append("passar")
        if jug["diners"] > c["comprar terreny"]:
            lstOpcions.append("comprar terreny")
        lstOpcions.append("preus")
    
    elif c["propietari"] == nomJugador:
        lstOpcions.append("passar")
        if c["nombre cases"] < 4 and jug["diners"] > c["comprar casa"]:
            lstOpcions.append("comprar casa")
        if c["nombre cases"] >= 2 and c["nombre hotels"] < 2 and jug["diners"] > c["comprar hotel"]:
            lstOpcions.append("comprar hotel")
        lstOpcions.append("preus")
    
    else:
        preu = c["lloguer casa"] * c["nombre cases"] + c["lloguer hotel"] * c["nombre hotels"]
        if preu > 0:
            Transferencia(nomJugador,c["propietari"],preu)
