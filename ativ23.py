print('-------- Entrada de Estacionamento ---------')
for tentativa in range(5):
    placa = input("Digite sua placa: ").strip()
    if len(placa) == 7 and placa != "0000000":
        print("PLaca registrada. Portão abrindo. . .")
        break
    else:
        print("Tente novamente")
else:
    print("Placa inválida ou proibida")
    print('-'*42)