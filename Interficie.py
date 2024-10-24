import os
from Dades import *

# Funcions Auxiliars ------------------------------------------------------------------------------
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
        liniaNoms += f"|{casella1["nom curt"].ljust(7)}{MostrarCases(casella1)}"
    
    liniaNoms += "(Historial aquí)"

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
        liniaJugadors += f"|{jugadorsAbreujats.ljust(7)}{MostrarHotels(casella1)}"
    
    liniaJugadors += "(Historial aquí)"

    jugadorsAbreujats = ""
    for jugador in casella2["jugadors"]:
        jugadorsAbreujats += jugador[0]
    if MostrarHotels(casella2) == "": 
        liniaJugadors += f"|{jugadorsAbreujats.ljust(8)}|"
    else: 
        liniaJugadors += f"{MostrarHotels(casella2)}{jugadorsAbreujats.ljust(7)}|"
    
    return liniaJugadors
# -------------------------------------------------------------------------------------------------
def Taulell():
    lstCasellesOrdenades = sorted(caselles, key=lambda casilla: casilla["fil_col_taulell"])
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
            liniaVora = "+--------+(Historial aquí)+--------+"

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
def InfoDreta():
    lstStrInfoDreta = []
    lstStrInfoDreta.extend([f"Banca:", f"Diners: {altresDades["diners banca"]}€",""])

    jugadorsOrdenats = sorted(jugadors.items(), key=lambda jugador: jugador[1]["torn"])

    for jugador, info in jugadorsOrdenats:
        if info['bancarrota']:
            carrers = "BANCARROTA"
            especial = "BANCARROTA"
            diners = "BANCARROTA"
        else:
            if info['carrers'] == []: carrers = "(res)"
            elif len(info['carrers']) >= 8:
                carrersCurts = []
                for carrer in info['carrers']:
                    c = BuscarCasellaSegonsNom(carrer)
                    carrersCurts.append(c['nom curt'])
                carrers = ", ".join(carrersCurts)
            else:
                carrers = ", ".join(info['carrers'])
            if info['especial'] == []: especial = "(res)"
            else: 
                lstEspecialsUnics = []
                lstQuantitats = []
                for esp in info['especial']:
                    if esp not in lstEspecialsUnics:
                        lstEspecialsUnics.append(esp)
                        quantitat = info['especial'].count(esp)
                        lstQuantitats.append(quantitat)
                lstEspsAmbQuantitats = []
                for esp, quantitat in zip(lstEspecialsUnics,lstQuantitats):
                    if quantitat > 1:
                        lstEspsAmbQuantitats.append(f"{esp} ({quantitat})")
                    else:
                        lstEspsAmbQuantitats.append(f"{esp}")
                especial = ", ".join(lstEspsAmbQuantitats)
            diners = f"{info['diners']}€"
        lstStrInfoDreta.extend([f"Jugador {jugador}:", f"Carrers: {carrers}", f"Diners: {diners}", f"Especial: {especial}",""])
    return lstStrInfoDreta
#--------------------------------------------------------------------------------------------------

def InserirHistorialAlTaulell():
    taulell = Taulell()
    taulellAmbHistorial = []
    for i, liniaTaulell in enumerate(taulell):
        liniaAmbHistorial = liniaTaulell
        if 4<=i<=17:
            liniaAmbHistorial = liniaAmbHistorial.replace("(Historial aquí)",historialJoc[i-4])
        taulellAmbHistorial.append(liniaAmbHistorial)
    return taulellAmbHistorial
            
def NetejarPantalla():
    if os.name == 'nt':     # Windows
        os.system('cls')
    else:                   # Linux o macOS
        os.system('clear')

def MostrarInterficie():
    NetejarPantalla()
    taulellAmbHistorial = InserirHistorialAlTaulell()
    infoDreta = InfoDreta()
    for liniaTaulell, liniaDreta in list(zip(taulellAmbHistorial,infoDreta)):
        print(liniaTaulell+"   "+liniaDreta)
