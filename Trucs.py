import random
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

def TrucAfegirCases(IDCasellaActual, nCases):
    if caselles[IDCasellaActual]["tipus"] == "especial":
        return "No es poden afegir cases a una casella especial."
    else:
        nCasesMax = 4 - caselles[IDCasellaActual]["nombre cases"]
        if 1 <= nCases <= nCasesMax:
            caselles[IDCasellaActual]["nombre cases"] += nCases
            return ""
        elif nCases == 0: return f"El nombre de cases per afegir ha de ser entre 1 i {nCasesMax}." 
        else:
            match nCasesMax:
                case 0: return "No es poden afegir més cases."
                case 1: return f"Només es pot afegir 1 casa més, no pas {nCases} cases."
                case _: return f"El nombre de cases per afegir ha de ser entre 1 i {nCasesMax}." 

def TrucAfegirHotels(IDCasellaActual, nHotels):
    if caselles[IDCasellaActual]["tipus"] == "especial":
        return "No es poden afegir hotels a una casella especial."
    else:
        nHotelsMax = 2 - caselles[IDCasellaActual]["nombre hotels"]
        if 1 <= nHotels <= nHotelsMax:
            caselles[IDCasellaActual]["nombre hotels"] += nHotels
            return ""
        elif nHotels == 0: return f"El nombre d'hotels per afegir ha de ser entre 1 i {nHotelsMax}." 
        else:
            match nHotelsMax:
                case 0: return "No es poden afegir més hotels."
                case 1: return f"Només es pot afegir 1 hotel més, no pas {nHotels} hotels."
                case _: return f"El nombre d'hotels per afegir ha de ser o bé 1 o bé 2." 

def TrucSeguentJugador(nomJugador):
    if re.fullmatch(r'(b(lau)?)|(g(roc)?)|(t(aronja)?)|(v(ermell)?)',nomJugador.lower()):
        if nomJugador.lower() in ["b","g","t","v"]:
            nomJugador = ["blau","groc","taronja","vermell"][["b","g","t","v"].index(nomJugador.lower())]
        nomJugador = nomJugador.capitalize()

        pass

        AfegirAHistorial(f"  El següent jugador serà {nomJugador}.")
        return ""
    else: 
        return f"\"{nomJugador}\" no és un jugador vàlid."

def TrucDinersJugador(nomJugador, nDiners):
    if re.fullmatch(r'(b(lau)?)|(g(roc)?)|(t(aronja)?)|(v(ermell)?)',nomJugador.lower()):
        if nomJugador.lower() in ["b","g","t","v"]:
            nomJugador = ["blau","groc","taronja","vermell"][["b","g","t","v"].index(nomJugador.lower())]
        nomJugador = nomJugador.capitalize()
        jugadors[nomJugador]["diners"] = nDiners
        AfegirAHistorial(f"  Ara \"{nomJugador[0]}\" té {nDiners}€")
        return ""
    else: 
        return f"\"{nomJugador}\" no és un jugador vàlid."

def TrucDinersBanca(nDiners):
    banca["diners"] = nDiners
    AfegirAHistorial(f"  Ara hi ha {nDiners}€ a la banca")

def EscollirTrucs(IDCasellaActual, nomJugador):
    lstTrucs = [r'anar a (\w+( \w+)*)', r'afegir (\d+) cases', r'afegir (\d+) hotels', r'seguent (\w+)', r'diners (\w+) (\d+)', r'diners (\d+) banca', r'acabar']
    AfegirAHistorial(f"  \"{nomJugador[0]}\" fa trampes")

    missatgeError = ""
    while True:
        MostrarInterficie()
        if missatgeError: 
            print(f"ERROR: {missatgeError}")
            missatgeError = ""
        print(f"\"{nomJugador[0]}\" fa trampes, opcions:\n- anar a CASELLA\n- afegir X cases\n- afegir X hotels\n- seguent JUGADOR\n- diners JUGADOR DINERS\n- diners DINERS banca\n- acabar")
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
                    TrucAnarA(IDCasellaActual, nomJugador, nomCasellaDesti)
                    IDCasellaActual = jugadors[nomJugador]["ID_casella"]
                case 1:
                    nCases = int(patroCoincident.group(1))
                    missatgeError = TrucAfegirCases(IDCasellaActual,nCases)
                case 2:
                    nHotels = int(patroCoincident.group(1))
                    missatgeError = TrucAfegirHotels(IDCasellaActual,nHotels)
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
                    MostrarInterficie()
                    break
