nome = ['Dudu', 'Bia', 'Léo']

for criança in nome:
    altura = int(input(f'Qual a altura de {criança} em centímetros: '))

    if altura >= 140:
        print(f'{criança}: Pode subir!')
    else:
        print(f'{criança}: Não pode subir.')