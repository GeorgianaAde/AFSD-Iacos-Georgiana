#LISTE
lista_de_numere= [10, 20,30,40, 50]
lista_diversa= [1, "text", 3.14, True, [1,2,3]]
#indexarea elementelor din lista
#incepe de la zero
print(lista_diversa[0])
print(lista_diversa[-1])
print(lista_diversa[1][0])
#segmentare
lista_de_numere=[10, 20, 30, 40, 50]
sublista= lista_de_numere[1:4:2]
print(sublista)
#operatorii + si*
lista_1=[1,2,3,4]
lista_2=[5,6,7]
print(lista_1 + lista_2)
#functii utile
#len
print(len(lista_1))
#max returneaza maximul din lista
print(max(lista_1))
print(min(lista_1))
#adaugam elemente in lista avem 2 metode
#met 1 append-adauga elementul la finalul listei
lista=[1,2,3]
lista.append(10)
#met 2 cu insert( index(pozitia), element)
lista.insert(1, 44)
#stergere elemente din lista #pop (index)
element_sters= lista.pop(1)
print("-------------------")
#remove(element)
#sterge prima apartie a numarului dat
lista=[1,2,3,4,3]
lista.remove(3)
print(lista)
print("-------------------")
#sortare lista
#sort
lista=[1,2,4,6,3,5]
print(lista)
print(lista)
#lista.sort(reverse:True)
print(lista)
#sorted(lista)
#returneaza o lista noua sortata
print("-------------------")
#cautarea elementelor in lista
#index(element)
#returneaza indexul primei aparitii a elementelot dat
lista=[5,"8", 8,9]
index_element=lista.index(8)
print(index_element)
#count numara elementele
# for element in lista, parcurge cu element pe valori
lista=[101,102,220,301,405]
for element in lista:
    print(element )
    #afisati nr pare
print("Elemente pare")
for element in lista:
    if element % 2==0:
        print(element)
#parcurgere cu index
#for index in range(len(lista))
#pozitia elementului la care suntem:index
#valoarea elementului: lista[index]
print("-------------------")
lista= [101,202,301,405,50,66,772,88,99]
for index in range(len(lista)):
    print(index, lista[index])
    #pozitioa e index
    #valoarea e lista[index]
if lista[index] % 2 ==0 and index % 3==0:
    print(lista[index])
#parcurgere cu while
#parcurgem cat timp avem elemente in lista sau e indeplinita o conditie
#parcurgere tot pe index, cresterea indexului la finalul fiecarui pas
print("-------------------")
lista=[10,20,30,"stop", 40]
index==0
while index<len(lista) and lista[index] != "stop" :
    print(lista[index])
    index+=1
print(lista)