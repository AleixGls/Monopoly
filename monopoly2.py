def imprimir_tablero(tablero):
    for fila in tablero:
        print("+--------" * len(fila) + "+")
        for propiedad in fila:
            # Ajustar el texto para que ocupe un espacio de 8 caracteres
            if propiedad:
                print(f"| {propiedad.ljust(8)} ", end="")
            else:
                print("|        ", end="")
        print("|")  # Cierra la fila
    print("+--------" * len(fila) + "+")

propiedades = [
    "Parking", "Urquinaona", "Fontan", "Sort", "Rambles", "Pl. Catalunya", "Anr Pró",
    "Angel"  , ""          , ""      , ""    , ""       , ""             , "Aragó"  , 
    "S. Joan", ""          , ""      , ""    , ""       , ""             , "Augusta",            
    "Caixa"  , ""          , ""      , ""    , ""       , ""             , "Caixa"  ,
    "Aribau" , ""          , ""      , ""    , ""       , ""             , "Balmes" ,
    "Muntan" , ""          , ""      , ""    , ""       , ""             , "Gracia" ,
    "Presó"  , "Consell"   , "Marina", "Sort", "Rosell" , "Lauria"       , "Sortida"
]

tablero = [
    propiedades[0:7],  # Fila 1
    propiedades[7:14], # Fila 2
    propiedades[14:21],# Fila 3
    propiedades[21:28],# Fila 4
    propiedades[3:44],# Fila 5
    propiedades[45:51],# Fila 6
    propiedades[52:58]# Fila 7
]

imprimir_tablero(tablero)
