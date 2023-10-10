idade=0
contador=0
while idade !=-1:
    idade = int (input("digite uma idade:"))
    if idade >=18:
        contador = contador+1

print (f"quantidade de pessoas maiores de 18:{contador}")