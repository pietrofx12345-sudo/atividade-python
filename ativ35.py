print("---Reserva de veiculo de luxo---")

for tentativa in range(3):
    cliente = input("Nome do cliente: ").strip()
    veiculo = input("Modelo do carro: ").strip()
    cor = input("Cor do carro: ").strip()
    cnh = input("CNH: ").strip()
    dias = input("Quantidade de dias da reserva: ").strip()
    seguro = input("NUMERO DO SEGURO: ").strip()
    if (
       veiculo == "SEDAN" and cor.isalpha and len(cnh) == 9 \
    ):
        print("Carro reservado com sucesso!")
        break

    else:
        print("Tente novamente!")
        print("-" * 30)

else:
    print("Muitas tentativas falhas. Tente novamente mais tarde!.")

print('-' * 42)