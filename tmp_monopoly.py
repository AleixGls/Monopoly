# Importacions ------------------------------------------------------------------------------------
import random
#--------------------------------------------------------------------------------------------------

# Diccionari jugadors -----------------------------------------------------------------------------
jugadors = {
    "Banca" : {
        "diner" : 1000000,
        "torn" : 0,
        "carrers" : None,
        "especial" : None,
    },

    "Groc" : {
        "diner" : 2000,
        "torn" : None,
        "carrers" : "(res)",
        "especial" : "(res)",
    },
    "Taronja" : {
        "diner" : 2000,
        "torn" : None,
        "carrers" : "(res)",
        "especial" : "(res)",
    },
    "Vermell" : {
        "diner" : 2000,
        "torn" : None,
        "carrers" : "(res)",
        "especial" : "(res)",
    },
    "Blau" : {
        "diner" : 2000,
        "torn" : None,
        "carrers" : "(res)",
        "especial" : "(res)",
    },
}
#--------------------------------------------------------------------------------------------------

# Definicions -------------------------------------------------------------------------------------
def Sortida(jugador):
    jugadors[jugador]["diner"] += 200

#--------------------------------------------------------------------------------------------------

# Randomitzar turn jugadors -----------------------------------------------------------------------
lstJugadors = ["Groc","Taronja","Vermell","Blau"]
random.shuffle(lstJugadors)

for i,jug in enumerate(lstJugadors):
    jugadors[jug]["torn"] = i+1

#--------------------------------------------------------------------------------------------------

# Taulell -----------------------------------------------------------------------------------------
lista_caselles = {
    "normals" : [
        {
            "nom": "Lauria",
            "nom curt": "Lauria",
            "lloguer casa": 10,
            "lloguer hotel": 15,
            "coprar terreny": 50,
            "comprar casa": 200,
            "comprar hotel": 250,
            "nombre casas": 0,
            "nombre hotels": 0,
            "jugadors": [],
            "ID_moviment": 2,
            "fil_col_taulell": [6,5]
        },
        {
            "nom": "Rosselló",
            "nom curt": "Rosell",
            "lloguer casa": 10,
            "lloguer hotel": 15,
            "coprar terreny": 50,
            "comprar casa": 225,
            "comprar hotel": 255,
            "nombre casas": 0,
            "nombre hotels": 0,
            "jugadors": [],
            "ID_moviment": 3,
            "fil_col_taulell": [6,4]
        },
        {
            "nom": "Marina",
            "nom curt": "Marina",
            "lloguer casa": 15,
            "lloguer hotel": 15,
            "coprar terreny": 50,
            "comprar casa": 250,
            "comprar hotel": 260,
            "nombre casas": 0,
            "nombre hotels": 0,
            "jugadors": [],
            "ID_moviment": 5,
            "fil_col_taulell": [6,2]
        },
        {
            "nom": "C. de cent",
            "nom curt": "Consell",
            "lloguer casa": 15,
            "lloguer hotel": 20,
            "coprar terreny": 50,
            "comprar casa": 275,
            "comprar hotel": 265,
            "nombre casas": 0,
            "nombre hotels": 0,
            "jugadors": [],
            "ID_moviment": 6,
            "fil_col_taulell": [6,1]
        },
        {
            "nom": "Muntaner",
            "nom curt": "Muntan",
            "lloguer casa": 20,
            "lloguer hotel": 20,
            "coprar terreny": 60,
            "comprar casa": 300,
            "comprar hotel": 270,
            "nombre casas": 0,
            "nombre hotels": 0,
            "jugadors": [],
            "ID_moviment": 8,
            "fil_col_taulell": [5,0]
        },
        {
            "nom": "Aribau",
            "nom curt": "Aribau",
            "lloguer casa": 20,
            "lloguer hotel": 20,
            "coprar terreny": 60,
            "comprar casa": 325,
            "comprar hotel": 275,
            "nombre casas": 0,
            "nombre hotels": 0,
            "jugadors": [],
            "ID_moviment": 9,
            "fil_col_taulell": [4,0]
        },
        {
            "nom": "Sant Joan",
            "nom curt": "St.Joan",
            "lloguer casa": 25,
            "lloguer hotel": 25,
            "coprar terreny": 60,
            "comprar casa": 350,
            "comprar hotel": 280,
            "nombre casas": 0,
            "nombre hotels": 0,
            "jugadors": [],
            "ID_moviment": 11,
            "fil_col_taulell": [2,0]
        },
        {
            "nom": "Aragó",
            "nom curt": "Aragó",
            "lloguer casa": 25,
            "lloguer hotel": 25,
            "coprar terreny": 60,
            "comprar casa": 375,
            "comprar hotel": 285,
            "nombre casas": 0,
            "nombre hotels": 0,
            "jugadors": [],
            "ID_moviment": 12,
            "fil_col_taulell": [1,0]
        },
        {
            "nom": "Urquinaona",
            "nom curt": "Urqinoa",
            "lloguer casa": 30,
            "lloguer hotel": 25,
            "coprar terreny": 70,
            "comprar casa": 400,
            "comprar hotel": 290,
            "nombre casas": 0,
            "nombre hotels": 0,
            "jugadors": [],
            "ID_moviment": 14,
            "fil_col_taulell": [0,1]
        },
        {
            "nom": "Fontana",
            "nom curt": "Fontan",
            "lloguer casa": 30,
            "lloguer hotel": 30,
            "coprar terreny": 70,
            "comprar casa": 425,
            "comprar hotel": 300,
            "nombre casas": 0,
            "nombre hotels": 0,
            "jugadors": [],
            "ID_moviment": 15,
            "fil_col_taulell": [0,2]
        },
        {
            "nom": "Les Rambles",
            "nom curt": "Rambles",
            "lloguer casa": 35,
            "lloguer hotel": 30,
            "coprar terreny": 70,
            "comprar casa": 450,
            "comprar hotel": 310,
            "nombre casas": 0,
            "nombre hotels": 0,
            "jugadors": [],
            "ID_moviment": 17,
            "fil_col_taulell": [0,4]
        },
        {
            "nom": "Pl. Catalunya",
            "nom curt": "Pl.Cat",
            "lloguer casa": 35,
            "lloguer hotel": 30,
            "coprar terreny": 70,
            "comprar casa": 475,
            "comprar hotel": 320,
            "nombre casas": 0,
            "nombre hotels": 0,
            "jugadors": [],
            "ID_moviment": 18,
            "fil_col_taulell": [0,5]
        },
        {
            "nom": "P. Àngel",
            "nom curt": "Angel",
            "lloguer casa": 40,
            "lloguer hotel": 35,
            "coprar terreny": 80,
            "comprar casa": 500,
            "comprar hotel": 330,
            "nombre casas": 0,
            "nombre hotels": 0,
            "jugadors": [],
            "ID_moviment": 20,
            "fil_col_taulell": [1,6]
        },
        {
            "nom": "Via Augusta",
            "nom curt": "Augusta",
            "lloguer casa": 40,
            "lloguer hotel": 35,
            "coprar terreny": 80,
            "comprar casa": 525,
            "comprar hotel": 340,
            "nombre casas": 0,
            "nombre hotels": 0,
            "jugadors": [],
            "ID_moviment": 21,
            "fil_col_taulell": [2,6]
        },
        {
            "nom": "Balmes",
            "nom curt": "Balmes",
            "lloguer casa": 50,
            "lloguer hotel": 40,
            "coprar terreny": 80,
            "comprar casa": 550,
            "comprar hotel": 350,
            "nombre casas": 0,
            "nombre hotels": 0,
            "jugadors": [],
            "ID_moviment": 23,
            "fil_col_taulell": [4,6]
        },
        {
            "nom": "Pg. de Gracia",
            "nom curt": "Gracia",
            "lloguer casa": 50,
            "lloguer hotel": 50,
            "coprar terreny": 80,
            "comprar casa": 525,
            "comprar hotel": 360,
            "nombre casas": 0,
            "nombre hotels": 0,
            "jugadors": [],
            "ID_moviment": 24,
            "fil_col_taulell": [5,6]
        },
    ],
    "especials" : [
        {
            "nom": "Sortida",
            "nom curt":"Sortida",
            "funcio": "Sortida",
            "jugadors": [],
            "ID_moviment": 1,
            "fil_col_taulell": [6,6]
        },
        {
            "nom": "Sort",
            "nom curt": "Sort",
            "funcio": "print()",
            "jugadors": [],
            "ID_moviment": 4,
            "fil_col_taulell": [6,3]
        },
        {
            "nom": "Presó",
            "nom curt": "Presó", 
            "funcio": "print()",
            "jugadors": [],
            "ID_moviment": 7,
            "fil_col_taulell": [6,0]
        },
        {
            "nom": "Caixa",
            "nom curt": "Caixa",
            "funcio": "print()",
            "jugadors": [],
            "ID_moviment": 10,
            "fil_col_taulell": [3,0]
        },
        {
            "nom": "Parking",
            "nom curt": "Parking", 
            "funcio": "print()",
            "jugadors": [],
            "ID_moviment": 13,
            "fil_col_taulell": [0,0]
        },
        {
            "nom":"Sort",
            "nom curt":"Sort",
            "funcio": "print()",
            "jugadors": [],
            "ID_moviment": 16,
            "fil_col_taulell": [0,3]
        },
        {
            "nom":"Anar preso",
            "nom curt":"Anr pró",
            "funcio": "print()",
            "jugadors": [],
            "ID_moviment": 19,
            "fil_col_taulell": [0,6]
        },
        {
            "nom":"Caixa",
            "nom curt":"Caixa",
            "funcio": "print()",
            "jugadors": [],
            "ID_moviment": 22,
            "fil_col_taulell": [3,6]
        },
    ]
}

def MostrarCases(casella):
    if casella.get("nombre cases",0) != 0:
        return f"{casella["nombre cases"]}C"
    else: return ""
def MostrarHotels(casella):
    if casella.get("nombre hotels",0) != 0:
        return f"{casella["nombre hotels"]}H"
    else: return ""
def CasesIHotels(casella): 
    return MostrarCases(casella)+MostrarHotels(casella)
def LiniaNomsFilesCentrals(casella1,casella2):
    liniaNoms = ""
    
    if MostrarCases(casella1) == "": 
        liniaNoms += f"|{casella1["nom curt"].ljust(8)}|"
    else: 
        liniaNoms += f"|{casella2["nom curt"].ljust(7)}{MostrarCases(casella1)}"
    
    liniaNoms += "".ljust(44)

    if MostrarCases(casella2) == "": 
        liniaNoms += f"|{casella2["nom curt"].ljust(8)}|"
    else: 
        liniaNoms += f"{MostrarCases(casella2)}{casella2["nom curt"].ljust(7)}|"
    
    return liniaNoms
def LiniaJugadorsFilesCentrals(casella1,casella2):
    liniaJugadors = ""

    jugadorsAbreujats = ""
    for jugador in casella1["jugadors"]:
        jugadorsAbreujats += jugador[0]
    if MostrarHotels(casella1) == "": 
        liniaJugadors += f"|{jugadorsAbreujats.ljust(8)}|"
    else: 
        liniaJugadors += f"{MostrarHotels(casella1)}{jugadorsAbreujats.ljust(7)}|"
    
    liniaJugadors += "".ljust(44)

    jugadorsAbreujats = ""
    for jugador in casella2["jugadors"]:
        jugadorsAbreujats += jugador[0]
    if MostrarHotels(casella2) == "": 
        liniaJugadors += f"|{jugadorsAbreujats.ljust(8)}|"
    else: 
        liniaJugadors += f"{MostrarHotels(casella2)}{jugadorsAbreujats.ljust(7)}|"
    
    return liniaJugadors

def Taulell():
    lstCasellesOrdenades = sorted(lista_caselles["normals"]+lista_caselles["especials"], key=lambda casilla: casilla["fil_col_taulell"])
    matriuCasellesOrdenades = [
        lstCasellesOrdenades[:7],
        lstCasellesOrdenades[7:9],
        lstCasellesOrdenades[9:11],
        lstCasellesOrdenades[11:13],
        lstCasellesOrdenades[13:15],
        lstCasellesOrdenades[15:17],
        lstCasellesOrdenades[17:]
    ]

    lstStrTaulell = []
    lstStrTaulell.append("--------".join("++++++++"))
    for fila in range(7):
        if fila == 0 or fila == 6:
            lst = [""]
            for columna in range(7):
                lst.append(CasesIHotels(matriuCasellesOrdenades[fila][columna]).rjust(8,"-"))
            lst.append("")
            liniaVora = "+".join(lst)

            lst = [""]
            for columna in range(7):
                lst.append(matriuCasellesOrdenades[fila][columna]["nom curt"].ljust(8))
            lst.append("")
            liniaNoms = "|".join(lst)

            lst = [""]
            for columna in range(7):
                jugadorsAbreujats = ""
                for jugador in matriuCasellesOrdenades[fila][columna]["jugadors"]:
                    jugadorsAbreujats += jugador[0]
                lst.append(jugadorsAbreujats.ljust(8))
            lst.append("")
            liniaJugadors = "|".join(lst)
        else:
            liniaVora = "+--------+"+"".ljust(44)+"+--------+"

            casella1 = matriuCasellesOrdenades[fila][0]
            casella2 = matriuCasellesOrdenades[fila][1]
            liniaNoms = LiniaNomsFilesCentrals(casella1,casella2)
            liniaJugadors = LiniaJugadorsFilesCentrals(casella1,casella2)

        if fila == 6:
            lstStrTaulell.append(liniaVora)
            lstStrTaulell.append(liniaJugadors)
            lstStrTaulell.append(liniaNoms)
        else:
            if 2<=fila<=5: lstStrTaulell.append(liniaVora)
            lstStrTaulell.append(liniaNoms)
            lstStrTaulell.append(liniaJugadors)
            if fila == 0: lstStrTaulell.append(liniaVora)
    lstStrTaulell.append("--------".join("++++++++"))

    return lstStrTaulell

#--------------------------------------------------------------------------------------------------


# Info dreta --------------------------------------------------------------------------------------
def InfoDreta():
    lstStrInfoDreta = []
    jugadorsOrdenats = sorted(jugadors.items(), key=lambda jugador: jugador[1]["torn"])

    for jugador, info in jugadorsOrdenats:
        if jugador == "Banca":
            lstStrInfoDreta.extend([f"{jugador}:", f"Diners: {info['diner']}€",""])
        else:
            lstStrInfoDreta.extend([f"Jugador {jugador}:", f"Carrers: {info['carrers']}", f"Diners: {info['diner']}€", f"Especial: {info['especial']}",""])
    return lstStrInfoDreta
#--------------------------------------------------------------------------------------------------

def MostrarInterficie():
    taulell = Taulell()
    infoDreta = InfoDreta()
    for liniaTaulell, liniaDreta in list(zip(taulell,infoDreta)):
        print(liniaTaulell+"   "+liniaDreta)

MostrarInterficie()