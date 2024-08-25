def fatorial(n):
    if n < 0 or n >= 16:
        return "o fatorial não é definido para números negativos ou maiores que 15"
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

while True:
    n = int(input("digita ae um número inteiro positivo menor que 16 (ou um número negativo para sair): "))
    if n < 0:
        break
    print("{0}! = {1}".format(n, fatorial(n)))