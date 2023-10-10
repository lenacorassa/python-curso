def abc (x):
    for i in x:
        if i<33 and i>7:
             listanova.append(i)
    # print(listanova)
    return listanova

listanova=[]
lista=[1,6,3,5,6,66,77,33,22,9,46]
print(lista)
listan=sorted(lista)
print(listan)
print(abc(listan))


