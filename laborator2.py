#structura decizionala if, elif,else
#if conditie conditia returneaza True sau False
#elif alta conditie elif= altfel daca, poate aparea de mai mult ori sau niciodata
#else o singura data sau deloc
numar_1=7
numar_2=7
if numar_1 > numar_2:
    print("Numarul 1 este mai mare decat numarul 2")
elif numar_1< numar_2:
    print("Numarul 1 este mai mic decat numarul 2")
else:
    print("Numarul 1 este egal cu numarul 2")
#verificam daca un numar este par sau impar
numar =11
if numar % 2 ==0:
    print("par")
else:
    print("impar")
#verificam daca un sir de caractere este gol sau nu
print("-------")
sir=""
if len(sir)==0:
    print("sirul este gol")
else:
    print("sirul nu este gol")
#verificam daca sirul de caractere are @
#in operator ce verifica daca un element se afla intr o colectie(sir)
if"@" in sir:
    print("sirul contine @")
else:
    print("sirul nu contine @")
#verificam daca sirul este palindrom(sa se citeasca la fel si de la stanga si de la dreapta)
#inversul unui sir[::-1]
sir="radar"
if sir==sir[::-1]:
    print("sirul este palindrom ")
else:
    print("sirul nu este palindrom")
  #numaram daca apare litera a de numar par de ori intr un sir
sir="Azi este o zi frumoasa"
numar_caractere_a= sir.count("a")
numar_caractere_A= sir.count("A")
if (numar_caractere_a + numar_caractere_A )% 2 == 0:
    print("litera a apare de numar par de ori")
else:
    print("litera a apare de numar impar de ori")
#structuri repetitive for, while
#for parcurge cu numar cunoscut de pasi
#range(start, stop, pas)
for i in range(0,10,1):
    print(i, end=" ")
#2 moduri de pargurgere a caracterelor unui sir for
sir="hello world"
for caracter in sir:
    print(caracter)
    #metoda2
print("-----------")
for i in range(len(sir)):
        print(i, sir[i])
 #numaram cate vocale sunt intr-un sir
sir="Azi vremea este frumoasa"
vocale=("aeiouAEIOU")
numar_vocale=0
for caracter in sir:
    if caracter in vocale:
        numar_vocale +=1
print(numar_vocale)
#pe ce poziti se afla spatiile
sir="Azi vremea este frumoasa"


for pozitie in range(len(sir)):
    if sir[pozitie]==" ":
        print("spatiu gasit pe pozitia:", pozitie)
    #while
    # afisam caracterele din sir pana intalnim un spatiu

sir="Azi vremea este frumoasa"
i=0
while sir[i] !=" ":
    print(sir[i])
    i += 1 #i=i+1

