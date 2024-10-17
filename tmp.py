# Definir las casillas laterales, las casillas inferiores, y el texto en el centro
casillas_superiores = [
    {"nom curt": "Parking"},
    {"nom curt": "Urqinoa"},
    {"nom curt": "Fontan"},
    {"nom curt": "Sort"},
    {"nom curt": "Rambles"},
    {"nom curt": "Pl.Cat"},
    {"nom curt": "Anr pró"}
]

casillas_lateral_izq = [
    {"nom curt": "Aragó"},
    {"nom curt": "S.Joan"},
    {"nom curt": "Caixa"},
    {"nom curt": "Aribau"},
    {"nom curt": "Muntan"}
]

casillas_lateral_der = [
    {"nom curt": "Angel"},
    {"nom curt": "Augusta"},
    {"nom curt": "Caixa"},
    {"nom curt": "Balmes"},
    {"nom curt": "Gracia"}
]

casillas_inferiores = [
    {"nom curt": "Presó"},
    {"nom curt": "Consell"},
    {"nom curt": "Marina"},
    {"nom curt": "Sort"},
    {"nom curt": "Rosell"},
    {"nom curt": "Lauria"},
    {"nom curt": "Sortida"}
]

# Texto en el centro que se mostrará
texto_central = [
    '> Juga "B", ha sortit 4 i 3                 ',
    '  "B" avança fins "Aribau"                  ',
    '  "B" compra el terreny                     ',
    '  Torn del jugador "T"                      ',
    '> Juga "T", ha sortit 2 i 2                 ',
    '  "T" surt de la pressó                     ',
    '  "T" avança fins "S.Joan"                  ',
    '  "T" paga ??€ de lloguer a "V"             ',
    '> Juga "G", ha sortit 1 i 1                 ',
    '  Sort: Anar tres espais enrrera            ',
    '  "G" guanya 200€                           ',
    '> Juga "B", ha sortit 4 i 2                 ',
    '  "B" és a la pressó, 3 torns sense tirar   '
]

#Superiores
print("+--------" * len(casillas_superiores) + "+")
for i in range(len(casillas_superiores)):
    nombre = casillas_superiores[i]["nom curt"].ljust(8)
    print(f"|{nombre}", end="")
print("|")
print("|        " * len(casillas_superiores) + "|")
print("+--------" * len(casillas_superiores) + "+")


# Imprimir las filas laterales con el texto en el centro
for i in range(len(casillas_lateral_izq)):
    print(f"|{casillas_lateral_izq[i]['nom curt'].ljust(8)}|{texto_central[i].ljust(44)}|{casillas_lateral_der[i]['nom curt'].ljust(8)}|")
    print(f"|{' ' * 8}|{texto_central[i+5].ljust(44)}|{' ' * 8}|")
    print(f"+--------+{' ' * 44}+--------+")

#Inferiores
print("+--------" * len(casillas_inferiores) + "+")
for i in range(len(casillas_inferiores)):
    print(f"|{casillas_inferiores[i]['nom curt'].ljust(8)}", end="")
print("|")
print("|        " * len(casillas_inferiores) + "|")
print("+--------" * len(casillas_inferiores) + "+")