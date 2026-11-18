print('--------Check in aeroporto---------')
for tentativa in range(3):
    voo = input('Qual o codigo de voo? ').strip()
    assento = input('qual seu assento? ').strip()
    if len(voo) == 4 and len(assento) == 3:
        print(f'Seu voo está correto {voo} e assento {assento} aceitos')
        break
    else:
        print('Acesso negado!')
        print('-'*42)