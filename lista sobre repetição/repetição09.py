quantidade_de_pares = 0
quantidade_de_impares = 0
for _ in range(10):
    numero = int(input("digita um número inteiro ae pae: "))
    if numero % 2 == 0:
        quantidade_de_pares += 1
    else:
        quantidade_de_impares += 1
print(f"\nquantidade de números pares {quantidade_de_pares}")
print(f"quantidade de números ímpares {quantidade_de_impares}")
