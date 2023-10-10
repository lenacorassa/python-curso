soma=0
contador=0
N=int(input("defina a quantidade de numeros:"))
for i in range(0,N):
    n=int(input("Digite um numero:"))
    soma=soma+n
    media=soma/N
    if n%2==0:
        contador=contador+1
        
        
porcentagem=((contador/N)*100)
print("temos",porcentagem ,"porcento de numeros pares")
print(soma)
print(media)
