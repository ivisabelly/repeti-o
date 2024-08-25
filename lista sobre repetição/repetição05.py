def calcular_populacao_final(populacao_inicial_A, taxa_crescimento_A, populacao_inicial_B, taxa_crescimento_B):
    anos = 0
    populacao_A = populacao_inicial_A
    populacao_B = populacao_inicial_B

    while populacao_A < populacao_B:
        populacao_A = populacao_A * (1 + taxa_crescimento_A)
        populacao_B = populacao_B * (1 + taxa_crescimento_B)
        anos += 1

    return anos, populacao_A, populacao_B
def obter_valor_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("insira um valor numérico válido")

while True:
    print("informa as populações iniciais e as taxas de crescimento:")
    populacao_inicial_A = obter_valor_float("população inicial do país A: ")
    taxa_crescimento_A = obter_valor_float("taxa de crescimento do país A (em decimal): ")
    populacao_inicial_B = obter_valor_float("população inicial do país B: ")
    taxa_crescimento_B = obter_valor_float("taxa de crescimento do país B (em decimal): ")
    anos, populacao_A_final, populacao_B_final = calcular_populacao_final(
        populacao_inicial_A, taxa_crescimento_A, populacao_inicial_B, taxa_crescimento_B
    )
    print(f"\nvai levar{anos} anos para que a população do país A ultrapasse ou se iguale a população do país B.")
    print(f"população final do país A: {populacao_A_final:.2f}")
    print(f"população final do país B: {populacao_B_final:.2f}\n")
    repetir = input("quer realizar outra operação? (s/n): ").lower()
    if repetir != 's':
        break
