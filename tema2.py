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


