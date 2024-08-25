def calcular_anos_populacao(a_populacao, b_populacao, taxa_crescimento_a, taxa_crescimento_b):
    anos = 0
    while a_populacao <= b_populacao:
        a_populacao *= 1 + taxa_crescimento_a / 100
        b_populacao *= 1 + taxa_crescimento_b / 100
        anos += 1
    return anos

populacao_a = 80000
taxa_crescimento_a = 3

populacao_b = 200000
taxa_crescimento_b = 1.5
anos_necessarios = calcular_anos_populacao(populacao_a, populacao_b, taxa_crescimento_a, taxa_crescimento_b)

print(f"vai ser necessário {anos_necessarios} anos para que a população do país A ultrapasse ou se iguale a população do país B")
