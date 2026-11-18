print('-----Criação de Conta Bancária Completa-----')
for tentativa in range (3):
    nome = input ('Qual seu nome? ')
    senha = input('Qual sua senha? ')
    frase = input('Qual sua frase de segurança? ')
    if len(nome) > 3 and len(senha) == 4 and senha != '0000' and len(frase) >10:
        print(f'{nome} sua conta foi criada com a senha: {senha} e a frase de segurança é {frase} ')
        break
    else:
        print('falha ao criar conta. ')
        print('-'*42)