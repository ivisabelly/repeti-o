maior_numero = float('-inf')
for _ in range(5):
    numero = float(input("digita um número aí pae: "))
    if numero > maior_numero:
        maior_numero = numero
print(f"O maior número é {maior_numero}")
