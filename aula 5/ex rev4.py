n=int(input("insira um nr:"))
maior=n
menor=n
 
while n!=-1:
    n=int(input("digte um nr:"))

    if n>maior:
        maior=n
    if n<menor:
        menor=n

print("o maior nr 'e e o menor 'e:", maior, menor)