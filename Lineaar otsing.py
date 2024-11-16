def lineaar_otsing(jada, otsitav_arv):
 
    for index in range(len(jada)):
 
        if jada[index] == otsitav_arv:
            return index
        
    return -1


jada = [10, 23, 45, 11, 70, 15]
otsitav_arv = 10

otsing = lineaar_otsing(jada, otsitav_arv)

if otsing != -1:
    print(f"Arv on järjekorras {otsing+1}-s")
else:
    print("Arvu pole järjekorras")
