import random
from Dades import *
from Interficie import MostrarInterficie
from FuncionsCasellesCarrer import *
from FuncionsCasellesEspecials import *
from Trucs import EscollirTrucs
#--------------------------------------------------------------------------------------------------

def DeclararBancarrota(IDCasella, nomJugador):
    AfegirAHistorial(f"  \"{nomJugador}\" declara bancarrota")
    VendreAlBanc(IDCasella, nomJugador, bancarrota = True)
    jugadors[nomJugador]["carrers"] = ["BANCARROTA"]
    jugadors[nomJugador]["diners"] = "BANCARROTA"
    jugadors[nomJugador]["especial"] = ["BANCARROTA"]
    ordreTurns.remove(nomJugador)

def MoureJugador(nomJugador):
    input(f"\"{nomJugador[0]}\", tira els daus! (polsa Intro)")

    dau1 = random.randint(1,6)
    dau2 = random.randint(1,6)
    moviment = dau1+dau2
    AfegirAHistorial(f"> Juga \"{nomJugador[0]}\", ha sortit {dau1} i {dau2}")
    IDCasellaActual = jugadors[nomJugador]["ID_casella"]
    
    if jugadors[nomJugador]["és_presoner"] and dau1 != dau2:
        jugadors[nomJugador]["torns_presoner"] -= 1
        if jugadors[nomJugador]["torns_presoner"] == 0:
            AfegirAHistorial(f"  \"{nomJugador[0]}\" ha sigut alliberat de la presó")
            jugadors[nomJugador]["és_presoner"] = False
        else:
            AfegirAHistorial(f"  \"{nomJugador[0]}\" romana a la presó, {jugadors[nomJugador]["torns_presoner"]} torns restants")
        IDCasellaDesti = IDCasellaActual
    else:
        if jugadors[nomJugador]["és_presoner"]:
            AfegirAHistorial(f"  \"{nomJugador[0]}\" surt de la presó")
            jugadors[nomJugador]["és_presoner"] = False
            jugadors[nomJugador]["torns_presoner"] = 0
        
        caselles[IDCasellaActual]["jugadors"].remove(nomJugador)
        IDCasellaDesti = IDCasellaActual + moviment
        if IDCasellaDesti >= 24: 
            IDCasellaDesti -= 24
            if IDCasellaDesti > 0: Sortida(nomJugador)
        
        jugadors[nomJugador]["ID_casella"] = IDCasellaDesti
        caselles[IDCasellaDesti]["jugadors"].append(nomJugador)
        AfegirAHistorial(f"  \"{nomJugador[0]}\" avança fins {caselles[IDCasellaDesti]["nom"]}")

    return IDCasellaDesti

def TornJugador(nomJugador):
    MostrarInterficie()
    IDCasellaDesti = MoureJugador(nomJugador)

    opcio = ""
    while True:
        if opcio and opcio != "trucs": break

        if caselles[IDCasellaDesti]["tipus"] == "especial":
            match caselles[IDCasellaDesti]["nom"]:
                case "Sortida": Sortida(nomJugador)
                case "Sort": Sort(IDCasellaDesti, nomJugador)
                case "Preso": pass
                case "Caixa": Caixa(IDCasellaDesti, nomJugador)
                case "Parking": pass
                case "Anar presó": AnarPreso(IDCasellaDesti, nomJugador)
            break
        else:
            lstOpcions = CaureEnCasellaCarrer(IDCasellaDesti, nomJugador)
            MostrarInterficie()
            if len(lstOpcions) > 1:
                while True:
                    while True:
                        print(f"Juga \"{nomJugador[0]}\", opcions: {", ".join(lstOpcions)}")
                        opcio = input("Escull una opció: ")
                        if opcio in lstOpcions or opcio == "trucs": break
                        MostrarInterficie()
                        print("Opció invàlida.")
                    match opcio:
                        case "passar": break
                        case "comprar terreny": ComprarTerreny(IDCasellaDesti,nomJugador); break
                        case "comprar casa": ComprarCasa(IDCasellaDesti,nomJugador); break
                        case "comprar hotel": ComprarHotel(IDCasellaDesti,nomJugador); break
                        case "preus": Preus(IDCasellaDesti)
                        case "preu banc": PreuBanc(nomJugador)
                        case "preu jugador": PreuJugador(nomJugador)
                        case "vendre al banc": VendreAlBanc(IDCasellaDesti, nomJugador); break
                        case "vendre a B": VendreAJugador(IDCasellaDesti,nomJugador,"Blau"); break
                        case "vendre a G": VendreAJugador(IDCasellaDesti,nomJugador,"Groc"); break
                        case "vendre a T": VendreAJugador(IDCasellaDesti,nomJugador,"Taronja"); break
                        case "vendre a V": VendreAJugador(IDCasellaDesti,nomJugador,"Vermell"); break
                        case "trucs": 
                            EscollirTrucs(IDCasellaDesti,nomJugador)
                            IDCasellaDesti = jugadors[nomJugador]["ID_casella"]; break
            elif lstOpcions == ["declarar bancarrota"]:
                opcio = "declarar bancarrota"
                input(f"\"{nomJugador[0]}\", has de declarar bancarrota. (polsa Intro)")
                DeclararBancarrota(IDCasellaDesti, nomJugador)
                break
            else: break

# Funcions auxiliars ------------------------------------------------------------------------------
def AleatoritzarOrdreTurns():
    random.shuffle(ordreTurns)

    for i,jug in enumerate(ordreTurns):
        jugadors[jug]["torn"] = i
    
    caselles[0]["jugadors"] = ordreTurns.copy()

def RemplirDinersBanca():
    if altresDades["diners banca"] < 500000:
        altresDades["diners banca"] += 1000000
# -------------------------------------------------------------------------------------------------

def IniciarJoc():
    AleatoritzarOrdreTurns()
    while True:
        if len(ordreTurns) == 1: break
        for nomJugador in ordreTurns:
            if jugadors[nomJugador]["torn"] == altresDades["torn actual"]:
                TornJugador(nomJugador); break
        altresDades["torn actual"] += 1
        if altresDades["torn actual"] == 4: altresDades["torn actual"] = 0
        RemplirDinersBanca()
    print(f"Fi del joc. Ha guanyat {ordreTurns[0]}")

IniciarJoc()
