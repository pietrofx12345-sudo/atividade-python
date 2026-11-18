print("--------------------------------Gestão de Frota e Telemetria Veicular Pesada-----------------------------------------")

for tentativas in range(3):

    nome_motorista = input("Digite o nome do motorista: ").strip()
    sobrenome = input("Digite o sobrenome: ").strip()
    cidade_saida = input("Digite a cidade de saída: ").strip()
    cidade_chegada = input("Digite a cidade de chegada: ").strip()
    placa_caminhao = input("Digite a placa do caminhão: ").strip()
    chassi_veiculo = input("Digite o chassi do veículo: ").strip()
    quilometragem_atual = input("Digite a quilometragem atual: ").strip()
    capacidade_tanque = input("Digite a capacidade do tanque: ").strip()
    codigo_carga = input("Digite o código da carga: ").strip()
    data_viagem = input("Digite a data da viagem (DD/MM/AAAA): ").strip()
    email_central = input("Digite o e-mail da central: ").strip()
    autorizacao_viagem = input("Digite a autorização da viagem: ").strip().upper()

    if (nome_motorista.isalpha() and
        sobrenome.isalpha() and
        cidade_saida.isalpha() and
        cidade_chegada.isalpha() and
        placa_caminhao.isalnum() and
        chassi_veiculo.isalnum() and
        codigo_carga.isalnum() and
        quilometragem_atual.isdigit() and
        capacidade_tanque.isdigit() and
        len(placa_caminhao) == 7 and
        email_central.endswith(".transporte.com") and
        autorizacao_viagem == "AUTORIZADO"):

        print(f"\nSUCESSO: motorista {nome_motorista}, viagem autorizada!")
        break

    else:
        print(f"\nERRO: Dados invalidos! {tentativas + 1} de 3")
        print("-" * 40)

else:
    print("\nAcesso negado")
