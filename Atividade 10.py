print("--------------------------------Desafio Integrador: Centro Espacial e Telemetria de Satélites-----------------------------------------")

for tentativas in range(3):

    nome_diretor = input("Digite o nome do diretor: ").strip()
    agencia_espacial = input("Digite o nome da agência espacial: ").strip()
    nome_satelite = input("Digite o nome do satélite: ").strip()
    codigo_transponder = input("Digite o código do transponder: ").strip()
    altitude_orbital = input("Digite a altitude orbital: ").strip()
    velocidade_orbital = input("Digite a velocidade orbital: ").strip()
    frequencia_uplink = input("Digite a frequência de Uplink: ").strip()
    potencia_paioneis = input("Digite a potência dos painéis: ").strip()
    pais_operador = input("Digite o país operador: ").strip()
    data_rastreio = input("Digite a data do rastreio (DD/MM/AAAA): ").strip()
    email_centro = input("Digite o e-mail do centro de controle: ").strip()
    sinal_telemetria = input("Digite o sinal de telemetria: ").strip().upper()

    if (nome_diretor.isalpha() and
        agencia_espacial.isalpha() and
        nome_satelite.isalnum() and
        codigo_transponder.isalnum() and
        altitude_orbital.isdigit() and
        velocidade_orbital.isdigit() and
        frequencia_uplink.isdigit() and
        potencia_paioneis.isdigit() and
        pais_operador.isalpha() and
        len(codigo_transponder) == 8 and
        len(data_rastreio) == 10 and
        email_centro.endswith(".space.org") and
        sinal_telemetria == "SINCRONIZADO"):

        print(f"\nSUCESSO: satélite {nome_satelite}, telemetria sincronizada!")
        break

    else:
        print(f"\nERRO: Dados invalidos! {tentativas + 1} de 3")
        print("-" * 40)

else:
    print("\nAcesso negado")
