import random
from Dades import *
from Interficie import AfegirAHistorial
from Interficie import MostrarInterficie
#--------------------------------------------------------------------------------------------------

def Sortida(nomJugador):
    altresDades["diners banca"] -= 200
    jugadors[nomJugador]["diners"] += 200
    AfegirAHistorial(f"  \"{nomJugador[0]}\" guanya 200€")

def Sort(IDCasellaActual, nomJugador):
    match random.randint(1,6):
        case 1: 
            AfegirAHistorial(f"  Sort: Sortir de la presó")
            jugadors[nomJugador]["especial"].append("Sortir de la presó")
        case 2: 
            AfegirAHistorial(f"  Sort: Anar a la presó")
            AnarPreso(IDCasellaActual, nomJugador)
        case 3: 
            AfegirAHistorial(f"  Sort: Anar a la sortida")
            caselles[IDCasellaActual]["jugadors"].remove(nomJugador)
            jugadors[nomJugador]["ID_casella"] = 0
            caselles[0]["jugadors"].append(nomJugador)
            Sortida(nomJugador)
        case 4:
            AfegirAHistorial(f"  Sort: Anar 3 espais enrere")
            caselles[IDCasellaActual]["jugadors"].remove(nomJugador)

            IDCasellaDesti = IDCasellaActual - 3
            jugadors[nomJugador]["ID_casella"] = IDCasellaDesti
            caselles[IDCasellaDesti]["jugadors"].append(nomJugador)
            
            if IDCasellaDesti == 0: Sortida(nomJugador) # 3 espais enrere des de Sort és o Parking o Sortida
        case 5:
            AfegirAHistorial(f"  Sort: Fer reparacions a les propietats")

            pagamentCarrers = 0
            pagamentHotels = 0
            for carrer in jugadors[nomJugador]["carrers"]:
                pagamentCarrers += 25
                for casella in caselles:
                    if casella["nom"] == carrer:
                        pagamentHotels += 100 * casella["nombre hotels"]; break
            AfegirAHistorial(f"  25€ per cada propietat: {pagamentCarrers}€")
            AfegirAHistorial(f"  100€ per cada hotel: {pagamentHotels}€")

            pagamentTotal = pagamentCarrers + pagamentHotels
            jugadors[nomJugador]["diners"] -= pagamentTotal
            altresDades["diners banca"] += pagamentTotal
            AfegirAHistorial(f"  \"{nomJugador[0]}\" paga {pagamentTotal}€ a la banca")
        case 6:
            AfegirAHistorial(f"  Sort: Ets escollit alcalde")

            for jugador, info in jugadors.items():
                if jugador != nomJugador:
                    jugadors[jugador]["diners"] -= 50
                    jugadors[nomJugador]["diners"] += 50
            AfegirAHistorial(f"  Cada jugador paga 50€ a \"{nomJugador[0]}\"")

def Caixa(IDCasellaActual, nomJugador):
    match random.randint(1,7):
        case 1:
            AfegirAHistorial(f"  Caixa: Sortir de la presó")
            jugadors[nomJugador]["especial"].append("Sortir de la presó")
        case 2:
            AfegirAHistorial(f"  Caixa: Anar a la presó")
            AnarPreso(IDCasellaActual, nomJugador)
        case 3:
            AfegirAHistorial(f"  Caixa: Error de la banca al teu favor")
            altresDades["diners banca"] -= 150
            jugadors[nomJugador]["diners"] += 150
            AfegirAHistorial(f"  \"{nomJugador[0]}\" guanya 150€")
        case 4:
            AfegirAHistorial(f"  Caixa: Despeses mèdiques")
            jugadors[nomJugador]["diners"] -= 50
            altresDades["diners banca"] += 50
            AfegirAHistorial(f"  \"{nomJugador[0]}\" paga 50€")
        case 5:
            AfegirAHistorial(f"  Caixa: Despeses escolars")
            jugadors[nomJugador]["diners"] -= 50
            altresDades["diners banca"] += 50
            AfegirAHistorial(f"  \"{nomJugador[0]}\" paga 50€")
        case 6:
            AfegirAHistorial(f"  Caixa: Reparacions al carrer")
            jugadors[nomJugador]["diners"] -= 40
            altresDades["diners banca"] += 40
            AfegirAHistorial(f"  \"{nomJugador[0]}\" paga 40€")
        case 7:
            AfegirAHistorial(f"  Caixa: Concurs de bellesa")
            altresDades["diners banca"] -= 10
            jugadors[nomJugador]["diners"] += 10
            AfegirAHistorial(f"  \"{nomJugador[0]}\" guanya 10€")

def AnarPreso(IDCasellaActual,nomJugador):
    caselles[IDCasellaActual]["jugadors"].remove(nomJugador)

    jugadors[nomJugador]["ID_casella"] = 6
    caselles[6]["jugadors"].append(nomJugador)
    AfegirAHistorial(f"  \"{nomJugador[0]}\" entra a la presó.")

    if "Sortir de la presó" in jugadors[nomJugador]["especial"]:
        AfegirAHistorial(f"  \"{nomJugador[0]}\" surt de la presó.")
        jugadors[nomJugador]["especial"].remove("Sortir de la presó")
    else:
        jugadors[nomJugador]["és_presoner"] = True
        jugadors[nomJugador]["torns_presoner"] = 3
