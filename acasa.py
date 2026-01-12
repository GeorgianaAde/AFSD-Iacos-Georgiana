numar_1=input("Scrie o nota un numar intreg de la 1 la 100")
nota=int(numar_1)
if nota >= 90:
    print("Excelent")
elif nota >=50 and nota <=89 :
    print("Admis")
else:
    print("Picat")
for i in range(1,11):
    print(i)
contor = 1
while contor <= 5: # Condiția de start (cu :)
    print(contor)
    contor += 1      # Avansul corect (fără buclă infinită)
zile_saptamana = ["Luni" , "Marti" , "Miercuri", "Joi",  "Vineri"]
print(zile_saptamana[3])
print(zile_saptamana[0])
# Se va executa de 3 ori
for i in range(3):
    print("Repetarea numarul:", i)
# Atenție: i va fi 0, apoi 1, apoi 2.
numar_introdus=0
while numar_introdus !=7:
 numar_introdus= int(input("Introdu aici un numar:   "))
print("Felicitari! Ai ghicit!")
def calculeaza_medie_student(nume_student, note):
 media_aritmetica= sum(note)/ len(note)
 media_aritmetica_finala= round(media_aritmetica, 2)
 return (nume_student, media_aritmetica_finala)
nume = ("ADELA")
note_elev = [8, 9.5, 7, 10]
rezultat = calculeaza_medie_student(nume, note_elev)
print(rezultat)
print("----------------------")
def cifre(numar):
    lista_cifre=[]
    while numar > 0:
        cifra= numar % 10
        numar = numar // 10
        lista_cifre.append(cifra)
    return lista_cifre
print(cifre(2345))