from Dades import *
from Interficie import AfegirAHistorial
from Interficie import MostrarInterficie
#--------------------------------------------------------------------------------------------------

def ComprarTerreny(IDCasella, nomJugador):
    c = caselles[IDCasella]
    preu = c["comprar terreny"]
    caselles[IDCasella]["propietari"] = nomJugador
    jugadors[nomJugador]["carrers"].append(c["nom"])
    jugadors[nomJugador]["diners"] -= preu
    altresDades["diners banca"] += preu
    AfegirAHistorial(f"  \"{nomJugador[0]}\" compra el terreny")
def ComprarCasa(IDCasella, nomJugador):
    preu = caselles[IDCasella]["comprar casa"]
    jugadors[nomJugador]["diners"] -= preu
    altresDades["diners banca"] += preu
    caselles[IDCasella]["nombre cases"] += 1
    AfegirAHistorial(f"  \"{nomJugador[0]}\" compra 1 casa")
def ComprarHotel(IDCasella, nomJugador):
    preu = caselles[IDCasella]["comprar hotel"]
    jugadors[nomJugador]["diners"] -= preu
    altresDades["diners banca"] += preu
    caselles[IDCasella]["nombre hotels"] += 1
    AfegirAHistorial(f"  \"{nomJugador[0]}\" compra 1 hotel")

def Preus(IDCasella):
    c = caselles[IDCasella]
    AfegirAHistorial(f"  Preu terreny: {c["comprar terreny"]}")
    AfegirAHistorial(f"  Preu casa: {c["comprar casa"]}")
    AfegirAHistorial(f"  Preu hotel: {c["comprar hotel"]}")
    MostrarInterficie()

def CalculPreuBanc(nomJugador): # Funció auxiliar
    preu = 0
    for carrer in jugadors[nomJugador]["carrers"]:
        for casella in caselles:
            if casella["nom"] == carrer:
                c = casella
                preu += (c["comprar terreny"] + c["lloguer casa"] * c["nombre cases"] + c["lloguer hotel"] * c["nombre hotels"]) * 0.5
    return preu
def PreuBanc(nomJugador):
    AfegirAHistorial(f"  Si vens tot al banc guanyaràs {CalculPreuBanc(nomJugador)}€")
    MostrarInterficie()

def CalculPreuJugador(nomJugador): # Funció auxiliar
    preu = 0
    for carrer in jugadors[nomJugador]["carrers"]:
        for casella in caselles:
            if casella["nom"] == carrer:
                c = casella
                preu += (c["comprar terreny"] + c["lloguer casa"] * c["nombre cases"] + c["lloguer hotel"] * c["nombre hotels"]) * 0.9
    return preu
def PreuJugador(nomJugador):
    for jugador in jugadors:
        if jugador != nomJugador:
            AfegirAHistorial(f"  Si vens tot a \"{jugador[0]}\" guanyaràs {min(CalculPreuBanc(nomJugador),jugador["diners"])}€")
    MostrarInterficie()

def VendreAlBanc(IDCasella, nomJugador, bancarrota = False):
    c = caselles[IDCasella]
    pagament = c["lloguer casa"] * c["nombre cases"] + c["lloguer hotel"] * c["nombre hotels"]

    for carrer in jugadors[nomJugador]["carrers"]:
        for casella in caselles:
            if casella["nom"] == carrer:
                caselles[caselles.index(casella)]["propietari"] = "Banca"
                jugadors[nomJugador]["carrers"].remove(casella["nom"])
                caselles[caselles.index(casella)]["nombre cases"] = 0
                caselles[caselles.index(casella)]["nombre hotels"] = 0

    preuVentaBanc = CalculPreuBanc(nomJugador)
    altresDades["diners banca"] -= preuVentaBanc
    jugadors[nomJugador]["diners"] += preuVentaBanc
    AfegirAHistorial(f"  \"{nomJugador[0]}\" ven tot al banc per {preuVentaBanc}€")

    if bancarrota:
        jugadors[c["propietari"]]["diners"] += jugadors[nomJugador]["diners"]
        AfegirAHistorial(f"  \"{nomJugador[0]}\" paga {jugadors[nomJugador]["diners"]}€ a \"{c["propietari"][0]}\"")
        jugadors[nomJugador]["diners"] = 0
    else:
        jugadors[nomJugador]["diners"] -= pagament
        jugadors[c["propietari"]]["diners"] += pagament
        AfegirAHistorial(f"  \"{nomJugador[0]}\" paga {pagament}€ a \"{c["propietari"][0]}\"")
    
def VendreAJugador(IDCasella,nomJugadorVenedor,nomJugadorComprador):
    c = caselles[IDCasella]
    pagament = c["lloguer casa"] * c["nombre cases"] + c["lloguer hotel"] * c["nombre hotels"]

    for carrer in jugadors[nomJugadorVenedor]["carrers"]:
        for casella in caselles:
            if casella["nom"] == carrer:
                caselles[caselles.index(casella)]["propietari"] = nomJugadorComprador
                caselles[caselles.index(casella)]["nombre cases"] = 0
                caselles[caselles.index(casella)]["nombre hotels"] = 0

    preuVentaJugador = min(CalculPreuJugador(nomJugadorVenedor),jugadors[nomJugadorComprador]["diners"])
    altresDades["diners banca"] -= preuVentaJugador
    jugadors[nomJugadorVenedor]["diners"] += preuVentaJugador
    AfegirAHistorial(f"  \"{nomJugadorVenedor[0]}\" ven tot a \"{nomJugadorComprador[0]}\" per {preuVentaJugador}€")

    jugadors[nomJugadorVenedor]["diners"] -= pagament
    jugadors[c["propietari"]]["diners"] += pagament
    AfegirAHistorial(f"  \"{nomJugadorVenedor[0]}\" paga {pagament}€ a \"{c["propietari"][0]}\"")

def CaureEnCasellaCarrer(IDCasella, nomJugador):
    c = caselles[IDCasella]
    jug = jugadors[nomJugador]

    if c["propietari"] == "Banca":
        lstOpcions = ["passar"]
        if jug["diners"] > c["comprar terreny"]:
            lstOpcions.append("comprar terreny")
        lstOpcions.append("preus")
    
    elif c["propietari"] == nomJugador:
        lstOpcions = ["passar"]
        if c["nombre cases"] < 4 and jug["diners"] > c["comprar casa"]:
            lstOpcions.append("comprar casa")
        if c["nombre cases"] >= 2 and c["nombre hotels"] < 2 and jug["diners"] > c["comprar hotel"]:
            lstOpcions.append("comprar hotel")
        lstOpcions.append("preus")
    
    else:
        pagament = c["lloguer casa"] * c["nombre cases"] + c["lloguer hotel"] * c["nombre hotels"]
        if pagament > 0:
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
                            lstJugsCompradorsPossibles.append(jugadorComprador)
                
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
                    dif = pagament - jugadors[nomJugador]["diners"] - int(CalculPreuJugador(nomJugador))
                    AfegirAHistorial(f"  Fins i tot venent tot a un altre jugador,")
                    AfegirAHistorial(f"  \"{nomJugador[0]}\" es queda a {dif}€ de poder pagar")
                    lstOpcions = ["declarar bancarrota"]
        else: lstOpcions = []

    return lstOpcions
