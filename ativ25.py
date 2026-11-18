print('-------- Sistema de logística---------')
for tentativa in range (3):
    produto = input('Qual seu produto? ')
    codigo = input('Qual seu código? ')
    destino = input('Qual seu destino? ')
    if len(codigo) == 6 and len(destino) > 3 and produto != 'PROIBIDO':
        print(f'Seu produto é {produto}, seu código é {codigo}, e seu destino é {destino}. ')
        break
    else:
        print('Falha ao resgistrar entrega. ')
print('-'*42)