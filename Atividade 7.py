print("--------------------------------Sistema de Defesa Cibernética e Monitoramento de SOC-----------------------------------------")

for tentativas in range(3):

    nome_analista = input("Digite o nome do analista: ").strip()
    equipe_resposta = input("Digite a equipe de resposta: ").strip()
    codigo_incidente = input("Digite o código do incidente: ").strip()
    ip_origem = input("Digite o IP de origem: ").strip()
    ip_destino = input("Digite o IP de destino: ").strip()
    porta_protocolo = input("Digite a porta do protocolo: ").strip()
    tipo_ameaca = input("Digite o tipo de ameaça: ").strip()
    severidade_numerica = input("Digite a severidade numérica: ").strip()
    codigo_patch = input("Digite o código do patch: ").strip()
    data_alerta = input("Digite a data do alerta (DD/MM/AAAA): ").strip()
    email_soc = input("Digite o e-mail do SOC: ").strip()
    resposta_incidente = input("Digite a resposta ao incidente: ").strip().upper()

    if (nome_analista.isalpha() and
        equipe_resposta.isalpha() and
        tipo_ameaca.isalpha() and
        codigo_incidente.isalnum() and
        codigo_patch.isalnum() and
        ip_origem.isalnum() and
        ip_destino.isalnum() and
        porta_protocolo.isdigit() and
        severidade_numerica.isdigit() and
        len(codigo_incidente) == 8 and
        email_soc.endswith(".soc.sec") and
        resposta_incidente == "MITIGADO"):

        print(f"\nSUCESSO: analista {nome_analista}, incidente mitigado!")
        break

    else:
        print(f"\nERRO: Dados invalidos! {tentativas + 1} de 3")
        print("-" * 40)

else:
    print("\nAcesso negado")
