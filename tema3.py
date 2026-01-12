tabla= [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "],
]
def afiseaza(tabla):
    for i in range(3):
        for j in range(3):
            print(tabla[i][j],end=" ")
    print()
print(tabla)
def citeste_mutares(tabla,jucator):
    while True:
        linia= int(input(f"Jucator {jucator},alege linia(0-2):"))
        coloana= int(input(f"Jucator {jucator},alege coloana(0-2):"))
        if 0 <= linia <= 2 and 0 <= coloana <= 2:
            if tabla[linia][coloana] == " ":
                return linia,coloana
            else:
                print("Casuta este deja ocupata!Mai incearca.")
        else:
            print("Numar invalid! Alege 0, 1 sau 2.")
def stare_joc(tabla):
    for i in range(3):
        if tabla[i][0] == tabla[i][1] == tabla[i][2] != " ":return tabla[i][0]
        if tabla[0][i] == tabla[1][i] == tabla[2][i] != " ":return tabla[0][i]
    if tabla[0][0] == tabla[1][1] == tabla[2][2] != " ":return tabla[0][0]
    if tabla[0][2] == tabla[1][1] == tabla[2][0] != " ":return tabla[0][2]
    for linie in tabla:
        if " " in linie:return "CONTINUA"
    return "EGAL"
#iNCEPEREA JOCULUI
jucator_curent="X"
stare= ("CONTINUA")
while stare == "CONTINUA":
    afiseaza(tabla)
    linie, coloana = citeste_mutares(tabla,jucator_curent)
    tabla[linie][coloana]= jucator_curent
    stare= stare_joc(tabla)
    if stare == "CONTINUA":
        if jucator_curent == "X":
            jucator_curent= "O"
        else:
            jucator_curent= "X"
afiseaza(tabla)
if stare=="EGAL":
    print("REMIZA")
else:
    print(f"Felicitari! Jucatorul {stare} a castigat!")