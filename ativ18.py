print("----------sistema de sigurança em duas etapas---------")
codigo_de_area= "100"
senha_correta= "1999"
for i in range(3):

    codigo = input ("Qual o seu codigo de area?")
    senha = input ("Qual a sua senha pessoal?")
    if codigo==codigo_de_area and senha==senha_correta:
        print("senha correta! Entrando...")
        break
    else:
        print("tente novamente")
else:
    print("muitas falhas, conta bloqueada")

print('-'*20)



















