print("---------Nome de Usuario-------")
nome = input("qual seu nome?" ) . strip()

for tentativas in range(3):
    if len(nome) > 4:
        print("usuario aceito")
        break
else:
    print("nome muito curto!")
        
print("-"*30)