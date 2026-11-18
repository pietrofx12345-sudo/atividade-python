
print("--- SISTEMA DE GESTÃO DE CARGAS E TRÁFEGO FERROVIÁRIO ---")

for tentativa in range(5):
    maquinista = input("Nome do Maquinista: ").strip().title()
    partida = input("Terminal de Partida: ").strip().title()
    chegada = input("Terminal de Chegada: ").strip().title()
    minerio = input("Tipo de Minério: ").strip().title()
    vagao = input("Código do Vagão: ").strip()
    trem = input("Número do Trem: ").strip()
    peso = input("Peso em Toneladas: ").strip()
    km = input("Quilômetros a Percorrer: ").strip()
    data = input("Data da Viagem (DD-MM-AAAA): ").strip()
    email = input("E-mail da Ferrovia: ").strip().lower()
    chave = input("Chave do Bloqueio de Freio: ").strip()
    sinalizacao = input("Sinalização da Linha (VERDE): ").strip().upper()

    data_formatada = data.replace("-", "/")

    if maquinista.replace(" ", "").isalpha() and \
    partida.replace(" ", "").isalpha() and \
    chegada.replace(" ", "").isalpha() and \
    minerio.replace(" ", "").isalpha() and \
    vagao.startswith("CARGA-") and \
    trem.isalnum() and \
    peso.isdigit() and \
    km.isdigit() and \
    data_formatada.count("/") == 2 and \
    len(data_formatada) == 10 and \
    email.endswith(".ferrovia.log.br") and \
    sinalizacao == "VERDE":

        chave_oculta = "*" * len(chave)

        print(f"\nSUCESSO: Carga ferroviária registrada!")
        print(f"Maquinista: {maquinista}")
        print(f"Partida: {partida} | Chegada: {chegada}")
        print(f"Tipo de Minério: {minerio}")
        print(f"Vagão: {vagao} | Trem: {trem}")
        print(f"Peso: {peso} toneladas | Distância: {km} km")
        print(f"Data da Viagem: {data_formatada}")
        print(f"E-mail: {email}")
        print(f"Chave Protegida: {chave_oculta}")
        print(f"Sinalização da Linha: {sinalizacao}")
        break

    else:
        print(f"\nERRO: Dados Inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)

else:
    print("\nBLOQUEADO: 5 tentativas esgotadas. Verifique os dados.")
