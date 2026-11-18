senha_correta = "12345"
email_correto = "admin@gmail.com"
for tentativa in range(3):
    chute_mail = input("Digite seu email: ")
    chute_senha = input("Digite sua senha: ")
    if chute_mail == email_correto and chute_senha == senha_correta:
        print("Login efetuado")
        break
    else:
        print("Dados incorretos, tente novamente")
else:
    print("Conta bloqueada após 3 tentativas falhas. ")