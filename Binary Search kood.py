def binary(arvud, x, low, high):

    # kordab kuni mõlemad pooled kohtuvad
    while low <= high:

        kesk = low + (high - low)//2
        if x == arvud[kesk]:
            return kesk
        elif x > arvud[kesk]:
            low = kesk + 1
        else:
            high = kesk - 1
    return -1


arvud = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = int(input("Sisesta otsitav arv: "))

vastus = binary(arvud, x, 0, len(arvud)-1)
if vastus != -1:
    print("Arvu koht reas on " + str(vastus+1))
else:
    print("Ei ole arvude seas")