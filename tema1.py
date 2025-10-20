#tema 1 laborator algoritmi
text=(" Himalaya este cel mai înalt sistem montan de pe Pământ, întinzându-se pe o lungime de 2400 de kilometri și are o lățime de la 150 la 350 de kilometri. În afară de Nepal, acest lanț trece prin încă șase țări: India, China, Pakistan, Bhutan și Myanmar, iar poalele încep din nordul Bangladeshului. În episodul șase al documentarului MyEverest, realizat cu sprijinul financiar al Uniunii Europene în Republica Moldova, membrii expediției, se întâlnesc cu primi giganți ai Himalayei – cu munți de peste cinci mii de metri si ajungând până la poalele munților de peste opt mii de metri. Îl veți cunoaște pe șerpașul care a colecționat diferite lucruri care fost pe varful Everestului, în mod special, veți vedea cum aratau buteliile de aer care au fost pe vârful Everestului de la Edmund Hillary și șerpașul Tenzing Norgay până în zilele noastre.Toți cunosc cel mai înalt munte al planetei – Everest, de 8848,86 metri. Puțini însă știu că pe planeta Pământ există 14 munți cu o înălțime de peste opt mii de metri și zece din aceste vârfuri se află în Himalaya. Mai mult decât atât, aici se află și 75 de vârfuri cu o înălțime de peste 7000 de mii de metri.Mai multe despre vârfurile Himalayei și oamenii care locuiesc la aceste înălțimi, veți afla din episodul șase al serialului MyEverest.")
#print(text)
mijloc=(len(text)//2)
#print(mijloc)
prima_parte=text[:mijloc:1]
a_doua_parte=text[mijloc::1]
prima_parte2=prima_parte.upper()
prima_parte2=prima_parte2.strip()
#print(prima_parte2)
a_doua_parte2= a_doua_parte[::-1]
a_doua_parte2= a_doua_parte2.capitalize()
#print(a_doua_parte2)
semne_de_punctuatie=("." "," "?" "!")
#print(semne_de_punctuatie)
a_doua_parte2= a_doua_parte2.replace(".", "")
a_doua_parte2= a_doua_parte2.replace(",", "")
a_doua_parte2= a_doua_parte2.replace("?", "")
a_doua_parte2= a_doua_parte2.replace("!", "")
#print(a_doua_parte2)
text_final= prima_parte2 + a_doua_parte2
print(text_final)


