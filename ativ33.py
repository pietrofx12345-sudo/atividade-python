print('---- Sistema de agendamento da oficina ----')

for tentativa in range(3):  # 3 tentativas
    cliente = input("Cliente: ").strip()
    veiculo = input("Veículo: ").strip()
    placa = input("Placa: ").strip().upper()
    km = input("KM: ").strip()
    servico = input("Serviço: ").strip()
    codigo = input("Código: ").strip()

    if (
        len(cliente) > 3 and cliente.isalpha() and
        len(veiculo) > 3 and
        len(placa) == 7 and
        km.isdigit() and
        servico != "teste" and
        codigo == "T100"
    ):
        print("Seu agendamento foi concluído!")
        break

    else:
        print("Erro: verifique se o agendamento está correto, consulte o secretário ou tente novamente.")
        print("-" * 30)

else:
    print("Muitas tentativas falhas. Procure uma agência física.")