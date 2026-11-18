print('---------- Cadastro de Perfil de Usuário ----------')
for tentativa in range(3):
    nome = input('Qual seu nome? ').strip()
    cidade = input('Qual sua cidade? ').strip()
    sigla = input('Qual a sigla do estado? ').strip()
    if len(nome) > 3 and len(cidade) > 4 and len(sigla) == 2:
        print(f'Seu nome é {nome}, você mora em {cidade} no Estado de {sigla}')
        break
    else:
        print('Acesso Negado!')
print('-'*42)