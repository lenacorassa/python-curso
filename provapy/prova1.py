lista=[1,2,5,6,7]
lista.extend([3,4])
novalista=sorted(lista)
novalista.sort(reverse=True)
print(novalista)
print(len(novalista))
novalista.pop(0)
novalista.insert(0,35)
print(novalista)