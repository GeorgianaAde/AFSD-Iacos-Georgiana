#Bubble sort
lista=[1,5,7,3,9,4,3]
def bubble_sort(lista):
    interschimbare= True
    while interschimbare:
        interschimbare= False
        i=0
        while i< len(lista)-1:
            #i este pozitia curenta
            #i+1 e pozitia urmatoare
            #val curenta lista[i]
            if lista[i] > lista[i+1]:
                interschimbare= True
                lista[i], lista[i+1]= lista[i+1], lista[i]
            i+=1
print(lista)
bubble_sort(lista)
print(lista)