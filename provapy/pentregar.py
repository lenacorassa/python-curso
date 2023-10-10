lista = [5, 1, 3, 4, 6, 7, 0]
lista.sort(reverse=True)
print(lista)
lista.append(2)
lista.append(4)
print(lista)

tamanho_lista = len(lista)
print(tamanho_lista)

posicao_5 = lista.index(5)
print(posicao_5)

quantidade_4 = lista.count(4)
print(quantidade_4)

lista.insert(2, 10)
print(lista)
