n=int(input("insira um nr:"))
lista=[]
for i in range (0,n):
    nr=int(input("inisra um nr:"))
    lista.append(nr)
for i in range (0,n):
    if lista [i] <=0:
            lista [i]=1
    print("novo numero:", lista [i])