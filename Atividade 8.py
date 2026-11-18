print("--------------------------------Terminal Portuário e Controle de Atracação Marítima-----------------------------------------")

for tentativas in range(3):

    nome_pratico = input("Digite o nome do prático: ").strip()
    pais_embarcacao = input("Digite o país da embarcação: ").strip()
    nome_navio = input("Digite o nome do navio: ").strip()
    codigo_imo = input("Digite o código IMO: ").strip()
    calado_navio = input("Digite o calado do navio: ").strip()
    numero_berco = input("Digite o número do berço: ").strip()
    tonelagem_carga = input("Digite a tonelagem de carga: ").strip()
    codigo_rebocador = input("Digite o código do rebocador: ").strip()
    canal_atracacao = input("Digite o canal de atracação: ").strip()
    data_atracacao = input("Digite a data da atracação (DD/MM/AAAA): ").strip()
    email_capitania = input("Digite o e-mail da Capitania: ").strip()
    autorizacao_portuaria = input("Digite a autorização portuária: ").strip().upper()

    if (nome_pratico.isalpha() and
        pais_embarcacao.isalpha() and
        nome_navio.isalpha() and
        codigo_imo.isalnum() and
        codigo_rebocador.isalnum() and
        canal_atracacao.isalnum() and
        calado_navio.isdigit() and
        numero_berco.isdigit() and
        tonelagem_carga.isdigit() and
        len(codigo_imo) == 7 and
        email_capitania.endswith(".marinha.mil.br") and
        autorizacao_portuaria == "CONFIRMADO"):

        print(f"\nSUCESSO: prático {nome_pratico}, atracação confirmada!")
        break

    else:
        print(f"\nERRO: Dados invalidos! {tentativas + 1} de 3")
        print("-" * 40)

else:
    print("\nAcesso negado")
