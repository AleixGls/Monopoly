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
def sortida(jugador):
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
            "ID": 2
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
            "ID": 3
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
            "ID": 5
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
            "ID": 6
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
            "ID": 8
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
            "ID": 9
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
            "ID": 11
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
            "ID": 12
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
            "ID": 14
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
            "ID": 15
        },
        {
            "nom": "Les rambles",
            "nom curt": "Rambles",
            "lloguer casa": 35,
            "lloguer hotel": 30,
            "coprar terreny": 70,
            "comprar casa": 450,
            "comprar hotel": 310,
            "nombre casas": 0,
            "nombre hotels": 0,
            "jugadors": [],
            "ID": 17
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
            "ID": 18
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
            "ID": 20
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
            "ID": 21
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
            "ID": 23
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
            "ID": 24
        },
    ],
    "especials" : [
        {
            "nom": "Sortida",
            "nom curt":"Sortida",
            "funcio": sortida,
            "jugadors": [],
            "ID":1
        },
        {
            "nom": "Sort",
            "nom curt": "Sort",
            "funcio": print(),
            "jugadors": [],
            "ID": 4
        },
        {
            "nom": "Presó",
            "nom curt": "Presó", 
            "funcio": print(),
            "jugadors": [],
            "ID": 7
        },
        {
            "nom": "Caixa",
            "nom curt": "Caixa",
            "funcio": print(),
            "jugadors": [],
            "ID": 10
        },
        {
            "nom": "Parking",
            "nom curt": "Parking", 
            "funcio": print(),
            "jugadors": [],
            "ID": 13
        },
        {
            "nom":"Sort",
            "nom curt":"Sort",
            "funcio": print(),
            "jugadors": [],
            "ID": 16
        },
        {
            "nom":"Anar preso",
            "nom curt":"Anr pró",
            "funcio": print(),
            "jugadors": [],
            "ID": 19
        },
        {
            "nom":"Caixa",
            "nom curt":"Caixa",
            "funcio": print(),
            "jugadors": [],
            "ID": 22
        },
    ]
}
# Info dreta --------------------------------------------------------------------------------------
def infoDreta():
    jugadores_ordenados = sorted(jugadors.items(), key=lambda jugador: jugador[1]["torn"])

    for jugador, info in jugadores_ordenados:
        if jugador == "Banca":
            print(f"""{jugador}:
    Diners: {info['diner']}€
        """)
        else:
            print(f"""Jugador {jugador}:
    Carrers: {info['carrers']}
    Diners: {info['diner']}€
    Especial: {info['especial']}
            """)
#--------------------------------------------------------------------------------------------------
jugadores_ordenados = sorted(jugadors.items(), key=lambda jugador: jugador[1]["torn"])
casillas_ordenados = sorted(lista_caselles["normals"]+lista_caselles["especials"], key=lambda casilla: casilla["ID"])

print(f"""
+--------+--------+--------+--------+--------+--------+--------+ Banca:
|{casillas_ordenados[12]["nom curt"].ljust(8," ")}|{casillas_ordenados[13]["nom curt"].ljust(8," ")}|{casillas_ordenados[14]["nom curt"].ljust(8," ")}|{casillas_ordenados[15]["nom curt"].ljust(8," ")}|{casillas_ordenados[16]["nom curt"].ljust(8," ")}|{casillas_ordenados[17]["nom curt"].ljust(8," ")}|{casillas_ordenados[18]["nom curt"].ljust(8," ")}| Diners: {jugadores_ordenados[0][1]["diner"]}
|{"".ljust(8," ")}|{"".ljust(8," ")}|{"".ljust(8," ")}|{"".ljust(8," ")}|{"".ljust(8," ")}|{"".ljust(8," ")}|{"".ljust(8," ")}|
+--------+--------+--------+--------+--------+--------+--------+ Jugador {jugadores_ordenados[1][0]}:
|{casillas_ordenados[11]["nom curt"].ljust(8," ")}|{"".center(44," ")}|{casillas_ordenados[19]["nom curt"].ljust(8," ")}| Carrers: {jugadores_ordenados[1][1]["carrers"]}
|{"".ljust(8," ")}|{"".center(44," ")}|{"".ljust(8," ")}| Diners: {jugadores_ordenados[1][1]["diner"]}
+--------+{"".center(44," ")}+--------+ Especial: {jugadores_ordenados[1][1]["especial"]}
|{casillas_ordenados[10]["nom curt"].ljust(8," ")}|{"".center(44," ")}|{casillas_ordenados[20]["nom curt"].ljust(8," ")}|
|{"".ljust(8," ")}|{"".center(44," ")}|{"".ljust(8," ")}| Jugador {jugadores_ordenados[2][0]}:
+--------+{"".center(44," ")}+--------+ Carrers: {jugadores_ordenados[2][1]["carrers"]}
|{casillas_ordenados[9]["nom curt"].ljust(8," ")}|{"".center(44," ")}|{casillas_ordenados[21]["nom curt"].ljust(8," ")}| Diners: {jugadores_ordenados[2][1]["diner"]}
|{"".ljust(8," ")}|{"".center(44," ")}|{"".ljust(8," ")}| Especial: {jugadores_ordenados[2][1]["especial"]}
+--------+{"".center(44," ")}+--------+
|{casillas_ordenados[8]["nom curt"].ljust(8," ")}|{"".center(44," ")}|{casillas_ordenados[22]["nom curt"].ljust(8," ")}| Jugador {jugadores_ordenados[3][0]}:
|{"".ljust(8," ")}|{"".center(44," ")}|{"".ljust(8," ")}| Carrers: {jugadores_ordenados[3][1]["carrers"]}
+--------+{"".center(44," ")}+--------+ Diners: {jugadores_ordenados[3][1]["diner"]}
|{casillas_ordenados[7]["nom curt"].ljust(8," ")}|{"".center(44," ")}|{casillas_ordenados[23]["nom curt"].ljust(8," ")}| Especial: {jugadores_ordenados[3][1]["especial"]}
|{"".ljust(8," ")}|{"".center(44," ")}|{"".ljust(8," ")}| 
+--------+--------+--------+--------+--------+--------+--------+ Jugador {jugadores_ordenados[4][0]}:
|{"".ljust(8," ")}|{"".ljust(8," ")}|{"".ljust(8," ")}|{"".ljust(8," ")}|{"".ljust(8," ")}|{"".ljust(8," ")}|{"".ljust(8," ")}| Carrers: {jugadores_ordenados[4][1]["carrers"]}
|{casillas_ordenados[6]["nom curt"].ljust(8," ")}|{casillas_ordenados[5]["nom curt"].ljust(8," ")}|{casillas_ordenados[4]["nom curt"].ljust(8," ")}|{casillas_ordenados[3]["nom curt"].ljust(8," ")}|{casillas_ordenados[2]["nom curt"].ljust(8," ")}|{casillas_ordenados[1]["nom curt"].ljust(8," ")}|{casillas_ordenados[0]["nom curt"].ljust(8," ")}| Diners: {jugadores_ordenados[4][1]["diner"]}
+--------+--------+--------+--------+--------+--------+--------+ Especial: {jugadores_ordenados[4][1]["especial"]}
""")


#--------------------------------------------------------------------------------------------------


