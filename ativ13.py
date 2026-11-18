passageiros  = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Juliana']

for nome in passageiros:
    peso = float(input(f'Qual é o peso da mala de {nome}:'))

    if peso <= 23:
        print(f'{nome}: Bagagem liberada')
    else:
        print(f'{nome}: Deve pagar taxa extra')