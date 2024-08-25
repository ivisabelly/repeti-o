while True:
    usuario = input("digita seu nome de usuário: ")
    senha = input("digita sua senha: ")

    if senha != usuario:
        print("Cadastro concluído com sucesso!")
        break
    else:
        print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")
