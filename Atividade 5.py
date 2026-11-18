print("--------------------------------Automação Industrial e Supervisório de Usina Hidrelétrica-----------------------------------------")

for tentativas in range(3):

    nome_operador = input("Digite o nome do operador: ").strip()
    turno_trabalho = input("Digite o turno de trabalho: ").strip()
    sigla_turbina = input("Digite a sigla da turbina: ").strip()
    codigo_gerador = input("Digite o código do gerador: ").strip()
    rotacao_rpm = input("Digite a rotação (RPM): ").strip()
    nivel_represa = input("Digite o nível da represa: ").strip()
    vazao_agua = input("Digite a vazão da água: ").strip()
    temperatura_mancais = input("Digite a temperatura dos mancais: ").strip()
    sala_comando = input("Digite a sala de comando: ").strip()
    data_leitura = input("Digite a data da leitura (DD/MM/AAAA): ").strip()
    email_usina = input("Digite o e-mail da usina: ").strip()
    alarme_geral = input("Digite o alarme geral: ").strip().upper()

    if (nome_operador.isalpha() and
        turno_trabalho.isalpha() and
        sala_comando.isalpha() and
        sigla_turbina.isalnum() and
        codigo_gerador.isalnum() and
        rotacao_rpm.isdigit() and
        nivel_represa.isdigit() and
        vazao_agua.isdigit() and
        temperatura_mancais.isdigit() and
        len(data_leitura) == 10 and
        email_usina.endswith(".energia.ind.br") and
        alarme_geral == "NORMAL"):

        print(f"\nSUCESSO: operador {nome_operador}, sistema da usina liberado!")
        break

    else:
        print(f"\nERRO: Dados invalidos! {tentativas + 1} de 3")
        print("-" * 40)

else:
    print("\nAcesso negado")
