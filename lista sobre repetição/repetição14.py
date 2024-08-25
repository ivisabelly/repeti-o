idades = []
while True:
    idade = input("digita ae a idade da pessoa (ou 'fim' para sair né): ")
    if idade == "fim":
        break
    idades.append(int(idade))

if len(idades) == 0:
    print("não houve alunos digitados")
else:
    media = sum(idades) / len(idades)
    print("a média de idade da turma é de {0:.1f} anos.".format(media))
    if media >= 0 and media <= 25:
        print("a turma é jovem")
    elif media >= 26 and media <= 60:
        print("a turma é adulta")
    else:
        print("a turma é idosa")