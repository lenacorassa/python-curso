n=int(input("digte:"))
menor=n
maior=n
while n!=-1:
    n=int(input("digite o nr:"))
    if n>maior and n!=-1:
        maior=n
    if n<menor and n!=-1:
        menor=n
print("maior", maior)
print("menor:",menor)
