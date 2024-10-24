from Dades import *
from Interficie import MostrarInterficie

def DeclararBancarrota(nomJugador):
    AfegirAHistorial(f"  \"{nomJugador}\" declara bancarrota")
    if jugadors[nomJugador]["carrers"]:
        VendreAlBanc(nomJugador)
    jugadors[nomJugador]["bancarrota"] = True
    ordreTurns.remove(nomJugador)

def CalculPreuBanc(venedor): # Funció auxiliar
    preu = 0
    for carrer in jugadors[venedor]["carrers"]:
        c = BuscarCasellaSegonsNom(carrer)
        preu += (c["comprar terreny"] + c["lloguer casa"] * c["nombre cases"] + c["lloguer hotel"] * c["nombre hotels"]) * 0.5
    if preu * 10 % 10 == 0: #Si la part decimal és 0
        preu = int(preu)
    return preu
def PreuBanc(venedor):
    AfegirAHistorial(f"  Si vens tot al banc guanyaràs {CalculPreuBanc(venedor)}€")
    MostrarInterficie()

def CalculPreuJugador(venedor): # Funció auxiliar
    preu = 0
    for carrer in jugadors[venedor]["carrers"]:
        c = BuscarCasellaSegonsNom(carrer)
        preu += (c["comprar terreny"] + c["lloguer casa"] * c["nombre cases"] + c["lloguer hotel"] * c["nombre hotels"]) * 0.9
    if preu * 10 % 10 == 0: #Si la part decimal és 0
        preu = int(preu)
    return preu
def PreuJugador(venedor):
    for jugador in jugadors:
        if jugador != venedor:
            AfegirAHistorial(f"  Si vens tot a \"{jugador[0]}\" guanyaràs {min(CalculPreuJugador(venedor),jugadors[jugador]["diners"])}€")
    MostrarInterficie()

def VendreAlBanc(venedor):
    for carrer in jugadors[venedor]["carrers"]:
        IDCarrer = BuscarCasellaSegonsNom(carrer,retornarIndex=True)
        caselles[IDCarrer]["propietari"] = "Banca"
        jugadors[venedor]["carrers"].remove(caselles[IDCarrer]["nom"])
        caselles[IDCarrer]["nombre cases"] = 0
        caselles[IDCarrer]["nombre hotels"] = 0

    preuVentaBanc = CalculPreuBanc(venedor)
    Transferencia("Banca",venedor,preuVentaBanc)
    AfegirAHistorial(f"  \"{venedor[0]}\" ven tot al banc per {preuVentaBanc}€")

def VendreAJugador(venedor,comprador):
    for carrer in jugadors[venedor]["carrers"]:
        IDCarrer = BuscarCasellaSegonsNom(carrer,retornarIndex=True)
        jugadors[venedor]["carrers"].remove(caselles[IDCarrer]["nom"])
        jugadors[comprador]["carrers"].append(caselles[IDCarrer]["nom"])
        caselles[IDCarrer]["propietari"] = comprador

    preuVentaJugador = min(CalculPreuJugador(venedor),jugadors[comprador]["diners"])
    Transferencia(comprador,venedor,preuVentaJugador)
    AfegirAHistorial(f"  \"{venedor[0]}\" ven tot a \"{comprador[0]}\" per {preuVentaJugador}€")

def Insolvencia(pagador,cobrador,quantitat):
    if cobrador == "Banca":
        AfegirAHistorial(f"  \"{pagador[0]}\" ha de pagar {quantitat}€ a la banca")
    else:
        AfegirAHistorial(f"  \"{pagador[0]}\" ha de pagar {quantitat}€ a \"{cobrador[0]}\"")
    AfegirAHistorial(f"  \"{pagador[0]}\" no té prou diners")

    lstJugsCompradorsPossibles = []
    for jugadorComprador in jugadors:
            if jugadorComprador != pagador and min(CalculPreuJugador(pagador),jugadors[jugadorComprador]["diners"]) + jugadors[pagador]["diners"] > quantitat:
                lstJugsCompradorsPossibles.append(jugadorComprador)
    lstOpcions.clear()
    if (CalculPreuBanc(pagador) + jugadors[pagador]["diners"]) > quantitat:
        lstOpcions.append("preu banc")
        if lstJugsCompradorsPossibles:
            lstOpcions.append("preu jugador")
        lstOpcions.append("vendre al banc")
        for jugador in lstJugsCompradorsPossibles:
            lstOpcions.append(f"vendre a {jugador}")
    elif lstJugsCompradorsPossibles:
        AfegirAHistorial(f"  Vendre tot al banc no és prou per pagar")
        lstOpcions = ["preu jugador"]
        for jugador in lstJugsCompradorsPossibles:
            lstOpcions.append(f"vendre a {jugador}")
    else:
        dinersMax = 0
        for jugadorComprador in jugadors:
            if jugadorComprador != pagador:
                if dinersMax < jugadors[jugadorComprador]["diners"]:
                    dinersMax = jugadors[jugadorComprador]["diners"]
        if CalculPreuJugador(pagador) > dinersMax:
            AfegirAHistorial("Cap jugador pot comprar-li tot")
        else:
            dif = quantitat - jugadors[pagador]["diners"] - CalculPreuJugador(pagador)
            AfegirAHistorial(f"  Fins i tot venent tot a un altre jugador,")
            AfegirAHistorial(f"  \"{pagador[0]}\" es queda a {dif}€ de poder pagar")
        MostrarInterficie()
        input(f"\"{pagador[0]}\", has de declarar bancarrota. (polsa Intro)")
        DeclararBancarrota(pagador)
        return
    
    MostrarInterficie()
    while True:
        while True:
                print(f"\"{pagador[0]}\", no pots pagar. Opcions: {", ".join(lstOpcions)}")
                opcio = input("Escull una opció: ")
                if opcio in lstOpcions: break
                MostrarInterficie()
                print("Opció invàlida.")
        match opcio:
            case "preu banc": PreuBanc(pagador)
            case "preu jugador": PreuJugador(pagador)
            case "vendre al banc": VendreAlBanc(pagador); break
            case "vendre a Blau": VendreAJugador(pagador,"Blau"); break
            case "vendre a Groc": VendreAJugador(pagador,"Groc"); break
            case "vendre a Taronja": VendreAJugador(pagador,"Taronja"); break
            case "vendre a Vermell": VendreAJugador(pagador,"Vermell"); break
    MostrarInterficie()

def Transferencia(pagador, cobrador, quantitat, especial=False):
    if pagador == "Banca":
        altresDades["diners banca"] -= quantitat
        jugadors[cobrador]["diners"] += quantitat
        if especial: AfegirAHistorial(f"  \"{cobrador[0]}\" guanya {quantitat}€")
    else:
        if jugadors[pagador]["diners"] < quantitat:
            Insolvencia(pagador,cobrador,quantitat)
            if jugadors[pagador]['bancarrota']: 
                quantitat = jugadors[pagador]["diners"]
                if quantitat == 0: return
        if cobrador == "Banca":
            jugadors[pagador]["diners"] -= quantitat
            altresDades["diners banca"] += quantitat
            if especial: AfegirAHistorial(f"  \"{pagador[0]}\" paga {quantitat}€ a la banca")
        else:
            jugadors[pagador]["diners"] -= quantitat
            jugadors[cobrador]["diners"] += quantitat
            if not(especial): AfegirAHistorial(f"  \"{pagador[0]}\" paga {quantitat}€ a \"{cobrador[0]}\"")