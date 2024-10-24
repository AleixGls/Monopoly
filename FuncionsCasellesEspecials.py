import random
from Dades import *
from Transferencies import Transferencia
from Interficie import MostrarInterficie
#--------------------------------------------------------------------------------------------------

def Sortida(nomJugador):
    Transferencia("Banca",nomJugador,200,especial=True)

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
                c = BuscarCasellaSegonsNom(carrer)
                pagamentHotels += 100 * c["nombre hotels"]; break
            AfegirAHistorial(f"  25€ per cada propietat: {pagamentCarrers}€")
            AfegirAHistorial(f"  100€ per cada hotel: {pagamentHotels}€")

            pagamentTotal = pagamentCarrers + pagamentHotels
            Transferencia(nomJugador, "Banca", pagamentTotal, especial=True)
        case 6:
            AfegirAHistorial(f"  Sort: Ets escollit alcalde")

            for jugador in jugadors:
                if jugador != nomJugador:
                    Transferencia(jugador, nomJugador, 50, especial=True)

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
            Transferencia("Banca", nomJugador, 150, especial=True)
        case 4:
            AfegirAHistorial(f"  Caixa: Despeses mèdiques")
            Transferencia(nomJugador, "Banca", 50, especial=True)
        case 5:
            AfegirAHistorial(f"  Caixa: Despeses escolars")
            Transferencia(nomJugador, "Banca", 50, especial=True)
        case 6:
            AfegirAHistorial(f"  Caixa: Reparacions al carrer")
            Transferencia(nomJugador, "Banca", 40, especial=True)
        case 7:
            AfegirAHistorial(f"  Caixa: Concurs de bellesa")
            Transferencia("Banca", nomJugador, 10, especial=True)

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
