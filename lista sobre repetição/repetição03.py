def validar_nome(nome):
    return len(nome) > 3

def validar_idade(idade):
    return 0 <= idade <= 150

def validar_salario(salario):
    return salario > 0

def validar_sexo(sexo):
    return sexo.lower() in ['f', 'm']

def validar_estado_civil(estado_civil):
    return estado_civil.lower() in ['s', 'c', 'v', 'd']
def main():
    
    nome = input("digita teu nome: ")
    idade = int(input("digita tua idade: "))
    salario = float(input("digita teu salário: "))
    sexo = input("digita teu sexo (f/m): ")
    estado_civil = input("digita teu estado civil (s/c/v/d): ")

    if validar_nome(nome) and validar_idade(idade) and validar_salario(salario) \
            and validar_sexo(sexo) and validar_estado_civil(estado_civil):
        print("blz, informações válidas")
    else:
        print("tem algo errado, alguma informação inválida")

if __name__ == "__main__":
    main()
