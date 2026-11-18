print("---Validação de embarque internacional---")

for tentativa in range(3):
    passageiro = input("Nome do passageiro: ").strip()
    destino = input("Destino: ").strip()
    passaporte = input("Número do passaporte: ").strip()
    voo = input("Voo: ").strip()
    portão = input("Portão: ").strip()
    assento = input("Assento: ").strip()
    if (
        len(passageiro) > 3 and passageiro.isalpha() and \
        destino.isalpha() and \
        len(passaporte) == 8 and passaporte.isdigit() and \
        len(voo) == 4 and voo.isdigit() and \
        portão == "A1" and \
        len(assento) > 1 \
    ):
        print("Cartão de Embarque Emitido!")
        break

    else:
        print("Tente novamente!")
        print("-" * 30)

else:
    print("Muitas tentativas falhas. Tente novamente mais tarde!.")

print('-' * 42)