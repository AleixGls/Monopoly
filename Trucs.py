import re
from Dades import *
from Interficie import AfegirAHistorial
from Interficie import MostrarInterficie

def TrucAnarA(IDCasellaActual, nomJugador, nomCasellaDesti):
    ometrePrimera = False
    if nomCasellaDesti == "Sort" or nomCasellaDesti == "Caixa":
        while True:
            casellaDesitjada = input(f"Hi ha dues caselles anomenades \"{nomCasellaDesti}\". Vols anar a la primera o la segona? (escriu 1 o 2)")
            if casellaDesitjada == "1" or casellaDesitjada == "2": break
            print("Entrada invàlida. Escriu 1 o 2.")
        if casellaDesitjada == "2": ometrePrimera = True

    for casella in caselles:
        if casella["nom"] == nomCasellaDesti or casella["nom curt"] == nomCasellaDesti:
            if ometrePrimera: ometrePrimera = False; continue
            caselles[IDCasellaActual]["jugadors"].remove(nomJugador)
            IDCasellaDesti = caselles.index(casella)
            jugadors[nomJugador]["ID_casella"] = IDCasellaDesti
            casella["jugadors"].append(nomJugador)
            AfegirAHistorial(f"  \"{nomJugador[0]}\" va a {casella["nom"]}")
            return ""
    
    return f"  {nomCasellaDesti} no és una casella vàlida."

def TrucFixarCases(IDCasellaActual, nCases):
    if caselles[IDCasellaActual]["tipus"] == "especial":
        return "No es poden afegir cases a una casella especial."
    elif 1 <= nCases <= 4:
        caselles[IDCasellaActual]["nombre cases"] = nCases
        pluralFix = "cases"
        if nCases == 1: pluralFix = "casa"
        AfegirAHistorial(f"  Ara {caselles[IDCasellaActual]["nom"]} té {nCases} {pluralFix}.")
        return ""
    else: return f"El nombre de cases ha de ser entre 1 i 4." 

def TrucFixarHotels(IDCasellaActual, nHotels):
    if caselles[IDCasellaActual]["tipus"] == "especial":
        return "No es poden afegir hotels a una casella especial."
    elif 1 <= nHotels <= 4:
        caselles[IDCasellaActual]["nombre hotels"] = nHotels
        pluralFix = "hotels"
        if nHotels == 1: pluralFix = "hotel"
        AfegirAHistorial(f"  Ara {caselles[IDCasellaActual]["nom"]} té {nHotels} {pluralFix}.")
        return ""
    else: return f"El nombre de hotels ha de ser entre 1 i 4." 

def TrucSeguentJugador(nomJugador):
    if re.fullmatch(r'(b(lau)?)|(g(roc)?)|(t(aronja)?)|(v(ermell)?)',nomJugador.lower()):
        if nomJugador.lower() in ["b","g","t","v"]:
            nomJugador = ["blau","groc","taronja","vermell"][["b","g","t","v"].index(nomJugador.lower())]
        nomJugador = nomJugador.capitalize()

        for jugador, info in jugadors.items():
            if jugador == nomJugador:
                altresDades["torn actual"] = info["torn"] - 1; break

        AfegirAHistorial(f"  \"{nomJugador[0]}\" serà el següent jugador")
        return ""
    else: 
        return f"\"{nomJugador}\" no és un jugador vàlid."

def TrucDinersJugador(nomJugador, nDiners):
    if re.fullmatch(r'(b(lau)?)|(g(roc)?)|(t(aronja)?)|(v(ermell)?)',nomJugador.lower()):
        if nomJugador.lower() in ["b","g","t","v"]:
            nomJugador = ["blau","groc","taronja","vermell"][["b","g","t","v"].index(nomJugador.lower())]
        nomJugador = nomJugador.capitalize()
        if nDiners >= 0:
            jugadors[nomJugador]["diners"] = nDiners
        else:
            return "ERROR: Els diners no poden tenir un valor negatiu."
        AfegirAHistorial(f"  Ara \"{nomJugador[0]}\" té {nDiners}€")
        return ""
    else: 
        return f"\"{nomJugador}\" no és un jugador vàlid."

def TrucDinersBanca(nDiners):
    altresDades["diners banca"] = nDiners
    AfegirAHistorial(f"  Ara hi ha {nDiners}€ a la banca")

def TrucAfegirEspecial(nomJugador):
    AfegirAHistorial(f"  \"{nomJugador[0]}\" podrà sortir de la presó una vegada")
    jugadors[nomJugador]["especial"].append("Sortir de la presó")

def EscollirTrucs(IDCasellaActual, nomJugador):
    lstTrucs = [r'anar a (\w+(.? ?(\w|[àéèíóòú])+)*)', r'fixar cases a (\d+)', r'fixar hotels a (\d+)', r'seguent (\w+)', r'diners (\w+) (\d+)', r'diners (\d+) banca', r'afegir especial', r'acabar']
    AfegirAHistorial(f"  \"{nomJugador[0]}\" fa trampes")

    missatgeError = ""
    while True:
        MostrarInterficie()
        if missatgeError: 
            print(f"ERROR: {missatgeError}")
            missatgeError = ""
        print(f"\"{nomJugador[0]}\" fa trampes, opcions:\n- anar a CASELLA\n- fixar cases a X\n- fixar hotels a X\n- seguent JUGADOR\n- diners JUGADOR DINERS\n- diners DINERS banca\n- afegir especial\n- acabar")
        opcio = input("Escull una opció: ")
        opcioValida = False
        for truc in lstTrucs:
            patroCoincident = re.fullmatch(truc,opcio)
            if patroCoincident:
                IDTruc = lstTrucs.index(truc)
                opcioValida = True; break
        if not(opcioValida): missatgeError = "Opció invàlida."
        else:
            match IDTruc:
                case 0:
                    nomCasellaDesti = patroCoincident.group(1)
                    missatgeError = TrucAnarA(IDCasellaActual, nomJugador, nomCasellaDesti)
                    IDCasellaActual = jugadors[nomJugador]["ID_casella"]
                case 1:
                    nCases = int(patroCoincident.group(1))
                    missatgeError = TrucFixarCases(IDCasellaActual,nCases)
                case 2:
                    nHotels = int(patroCoincident.group(1))
                    missatgeError = TrucFixarHotels(IDCasellaActual,nHotels)
                case 3:
                    nomJugadorSeguent = patroCoincident.group(1)
                    missatgeError = TrucSeguentJugador(nomJugadorSeguent)
                case 4:
                    nomJugadorTruc = patroCoincident.group(1)
                    nDiners = int(patroCoincident.group(2))
                    missatgeError = TrucDinersJugador(nomJugadorTruc,nDiners)
                case 5:
                    nDiners = int(patroCoincident.group(1))
                    TrucDinersBanca(nDiners)
                case 6:
                    TrucAfegirEspecial(nomJugador)
                case 7:
                    MostrarInterficie()
                    break
