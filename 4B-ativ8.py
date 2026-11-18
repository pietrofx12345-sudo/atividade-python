
print("--- SISTEMA DE LEILÕES E RASTREAMENTO DE GADO BOVINO ---")

for tentativa in range(5):
    pecuarista = input("Nome do Pecuarista: ").strip().title()
    fazenda = input("Nome da Fazenda: ").strip().title()
    raca = input("Raça do Animal: ").strip().title()
    municipio = input("Município do Registro: ").strip().title()
    brinco = input("Código do Brinco Eletrônico: ").strip()
    registro = input("Registro Genealógico: ").strip()
    peso = input("Peso em Arrobas: ").strip()
    idade = input("Idade em Meses: ").strip()
    data = input("Data da Pesagem (DD-MM-AAAA): ").strip()
    email = input("E-mail da Associação Agropecuária: ").strip().lower()
    pin = input("PIN do Produtor: ").strip()
    certificacao = input("Certificação Sanitária (APROVADO): ").strip().upper()
  
    data_formatada = data.replace("-", "/")

    if pecuarista.replace(" ", "").isalpha() and \
    fazenda.replace(" ", "").isalpha() and \
    raca.replace(" ", "").isalpha() and \
    municipio.replace(" ", "").isalpha() and \
    brinco.startswith("BOV-") and \
    registro.isalnum() and \
    peso.isdigit() and \
    idade.isdigit() and \
    data_formatada.count("/") == 2 and \
    email.endswith(".agro.org.br") and \
    certificacao == "APROVADO":

        pin_oculto = "*" * len(pin)

        print(f"\nSUCESSO: Animal registrado para o pecuarista {pecuarista}!")
        print(f"Fazenda: {fazenda} | Raça: {raca}")
        print(f"Município: {municipio}")
        print(f"Brinco Eletrônico: {brinco}")
        print(f"Registro Genealógico: {registro}")
        print(f"Peso: {peso} arrobas | Idade: {idade} meses")
        print(f"Data da Pesagem: {data_formatada}")
        print(f"E-mail: {email}")
        print(f"PIN Protegido: {pin_oculto}")
        print(f"Certificação Sanitária: {certificacao}")
        break

    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)

else:
    print("\nBLOQUEADO: 5 tentativas esgotadas. Verifique os dados.")
