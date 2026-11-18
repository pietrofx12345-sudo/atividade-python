print('-----Cadastro de Funcionário Completo-----')
for tentativa in range(1):
    nome = input ('Qual seu nome? ')
    cargo = input ('Qual seu cargo? ')
    cpf = input ('Qual seu cpf? ')
    email = input('Qual sua email? ')
    senha = input('Qual sua senha? ')
    turno = input('Qual seu turno? ')
    if len(nome) > 3 and len(cargo) > 3 and len(cpf) == 11 and len(email) > 10 and len(senha) == 8 and len(turno) == 5:
        print(f'Olá, {nome} você é um(a) {cargo} e possui o CPF {cpf}, seu email é {email}, sua senha é {senha} e você trabalha no turno {turno}');
        break
else:
    print('Tu foi demitido, seu betinha. ')
print('-'*42)