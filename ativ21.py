print("----------senha segura---------")

for tentativas in range(3):
    senha = input('Digite sua senha( 8 caracteries )? '). strip()
    if len(senha) == 8:
        print('senha definida com sucesso')
        break
    else:
        print('tente novamente ')
else:
    print('senha invalida: ela deve ter exatamente 8 caracteres. ')

print('-'* 30)










