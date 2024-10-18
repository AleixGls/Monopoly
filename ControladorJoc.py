import random
from Dades import *
from Interficie import MostrarInterficie
#--------------------------------------------------------------------------------------------------

# Funcions Caselles Carrer ------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------

# Funcions Caselles Especials ---------------------------------------------------------------------
def Sortida(jugador):
    jugadors[jugador]["diner"] += 200

#--------------------------------------------------------------------------------------------------

# Randomitzar turn jugadors -----------------------------------------------------------------------
def AleatoritzarOrdreTurns():
    lstJugadors = ["Groc","Taronja","Vermell","Blau"]
    random.shuffle(lstJugadors)

    for i,jug in enumerate(lstJugadors):
        jugadors[jug]["torn"] = i+1
    
    caselles["especials"][0]["jugadors"] = lstJugadors

def IniciarJoc():
    AleatoritzarOrdreTurns()
    MostrarInterficie()

IniciarJoc()
