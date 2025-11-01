elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]
#Partea A
#cerinta A1
print("Lista eleviilor si notele lor:")
for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")
#cerinta A2
print("---------")
nota_maxima= max(note)
nota_minima= min(note)
#print(nota_minima)
index_of_nota_minima=note.index(nota_minima)
#print(index_of_nota_minima)
index_of_nota_maxima=note.index(nota_maxima)
#print(index_of_nota_maxima)
print(f"{elevi[index_of_nota_minima]} are nota minima {nota_minima}")
print(f"{elevi[index_of_nota_maxima]} are nota maxima {nota_maxima}")
#cerinta A3
print("--------")
media_notelor= sum(note)/len(note)
#print(media_notelor)
print(f"Media clasei este {media_notelor:.2f}")
print("--------")
#cerinta A4
print("Elevii promovati:")
for i in range(len(note)):
    if note[i] >=5:
        print(f"{elevi[i]} este promovat")
#PARTEA B
#cerinta B1
print("--------")
#nota_noua= note[i] + 1
for i in range(len(note)):
    print(f" Nota noua pentru {elevi[i]} devine {note[i]+1}")
print("------")
#cerinta B2
elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elevi.append(elev_nou)
print(elevi)
note.append(nota_elev_nou)
print(note)
#Cerinta B3
print("--------")
elev_de_sters   = "Darius"
pozitia= elevi.index(elev_de_sters)
elevi.pop(pozitia)
note.pop(pozitia)
print(elevi)
print(note)
#Cerinta B4
print("--------")
for i in range(len(elevi)):
    print(f"{elevi[i]} are nota {note[i]}")
print("--------")
#PARTEA C
#Cerinta C1
interogari_nume = ["Ana", "Mara", "Elena", "stop"]
i=0
while interogari_nume[i] != "stop":
    nume= interogari_nume[i]
    if nume in elevi:
        pozitia= elevi.index(nume)
        print(f"{nume} are nota {note[pozitia]}")
    else:
        print(f"{nume} nu exista in lista de interogari nume")
    i += 1




