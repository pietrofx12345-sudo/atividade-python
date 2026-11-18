
print("--- SISTEMA DE CONTROLE DE IMIGRAÇÃO E PASSAPORTES ---")

for tentativa in range(5):
    nome = input("Nome do Passageiro: ").strip().title()
    sobrenome = input("Sobrenome: ").strip().title()
    pais = input("País de Origem: ").strip().title()
    cidade = input("Cidade de Destino: ").strip().title()
    passaporte = input("Número do Passaporte: ").strip()
    voo = input("Código do Voo: ").strip()
    bagagens = input("Quantidade de Bagagens: ").strip()
    dias = input("Tempo de Estadia em Dias: ").strip()
    data = input("Data de Entrada (DD-MM-AAAA): ").strip()
    email = input("E-mail da Companhia Aérea: ").strip().lower()
    visto = input("Código do Visto: ").strip()
    autorizacao = input("Entrada no País (AUTORIZADO): ").strip().upper()
    data_formatada = data.replace("-", "/")

    if nome.replace(" ", "").isalpha() and \
    sobrenome.replace(" ", "").isalpha() and \
    pais.replace(" ", "").isalpha() and \
    cidade.replace(" ", "").isalpha() and \
    voo.startswith("FLIGHT-") and \
    passaporte.isalnum() and \
    len(passaporte) == 8 and \
    bagagens.isdigit() and \
    dias.isdigit() and \
    data_formatada.count("/") == 2 and \
    email.endswith(".air.com") and \
    autorizacao == "AUTORIZADO":

        visto_oculto = "*" * len(visto)

        print(f"\nSUCESSO: Passageiro {nome} {sobrenome} autorizado!")
        print(f"País: {pais} | Cidade: {cidade}")
        print(f"Passaporte: {passaporte} | Voo: {voo}")
        print(f"Bagagens: {bagagens} | Estadia: {dias} dias")
        print(f"Data Padronizada: {data_formatada}")
        print(f"E-mail: {email} | Visto Protegido: {visto_oculto}")
        print(f"Entrada no País: {autorizacao}")
        break

    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)

else:
    print("\nBLOQUEADO: 5 tentativas esgotadas. Verifique os dados.")
