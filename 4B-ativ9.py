print("--- CENTRO DE COMANDO E TELEMETRIA DE DRONES DE RESGATE ---")

for tentativa in range(5):
    piloto = input("Nome do Piloto Remoto: ").strip().title()
    regiao = input("Região de Busca: ").strip().title()
    cidade = input("Cidade Base: ").strip().title()
    missao = input("Tipo de Missão: ").strip().title()
    prefixo = input("Prefixo do Drone: ").strip().upper()
    canal = input("Canal do Transmissor: ").strip()
    altitude = input("Altitude de Voo: ").strip()
    bateria = input("Nível da Bateria em Porcentagem: ").strip()
    data = input("Data da Decolagem (DD-MM-AAAA): ").strip()
    email = input("E-mail do Corpo de Bombeiros: ").strip().lower()
    chave = input("Chave de Arme dos Motores: ").strip()
    status = input("Status do Link (CONECTADO): ").strip().upper()

    data_formatada = data.replace("-", "/")

    if piloto.replace(" ", "").isalpha() and \
       regiao.replace(" ", "").isalpha() and \
       cidade.replace(" ", "").isalpha() and \
       missao.replace(" ", "").isalpha() and \
       prefixo.startswith("DRONE-") and \
       canal.isalnum() and \
       altitude.isdigit() and \
       bateria.isdigit() and \
       data_formatada.count("/") == 2 and \
       len(data_formatada) == 10 and \
       email.endswith(".bombeiros.gov.br") and \
       status == "CONECTADO":

        chave_oculta = "*" * len(chave)

        print(f"\nSUCESSO: Drone {prefixo} conectado! Piloto: {piloto} | Cidade: {cidade}.")
        print(f"Data Padronizada: {data_formatada} | Chave Protegida: {chave_oculta}")
        break
    else:
        print(f"\nERRO: Dados inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nACESSO NEGADO: 5 tentativas esgotadas.")