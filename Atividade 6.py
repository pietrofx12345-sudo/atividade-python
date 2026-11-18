print("--------------------------------Auditoria Financeira e Custódia de Criptoativos-----------------------------------------")

for tentativas in range(3):

    nome_auditor = input("Digite o nome do auditor: ").strip()
    cargo_empresa = input("Digite o cargo na empresa: ").strip()
    simbolo_token = input("Digite o símbolo do token: ").strip()
    codigo_hash = input("Digite o código Hash do bloco: ").strip()
    chave_publica = input("Digite a chave pública: ").strip()
    taxa_gas = input("Digite a taxa de Gas: ").strip()
    quantidade_transferida = input("Digite a quantidade transferida: ").strip()
    numero_confirmacoes = input("Digite o número de confirmações: ").strip()
    pais_exchange = input("Digite o país da Exchange: ").strip()
    data_operacao = input("Digite a data da operação (DD/MM/AAAA): ").strip()
    email_compliance = input("Digite o e-mail de Compliance: ").strip()
    parecer_auditoria = input("Digite o parecer da auditoria: ").strip().upper()

    if (nome_auditor.isalpha() and
        cargo_empresa.isalpha() and
        pais_exchange.isalpha() and
        simbolo_token.isalnum() and
        codigo_hash.isalnum() and
        chave_publica.isalnum() and
        taxa_gas.isdigit() and
        quantidade_transferida.isdigit() and
        numero_confirmacoes.isdigit() and
        len(chave_publica) >= 12 and
        email_compliance.endswith(".exchange.io") and
        parecer_auditoria == "CONCLUIDO"):

        print(f"\nSUCESSO: auditor {nome_auditor}, auditoria concluída!")
        break

    else:
        print(f"\nERRO: Dados invalidos! {tentativas + 1} de 3")
        print("-" * 40)

else:
    print("\nAcesso negado")
