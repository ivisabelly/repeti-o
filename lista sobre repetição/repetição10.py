n=int(input("digita um numero ae pae: "))
lista=[1,1]
for i in range(n-2):
    lista.append(lista[i]+ lista[i+1])
print(lista)