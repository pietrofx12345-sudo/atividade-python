print("--- sistema de lançamento espacial")

for tentativa in range(5):
    # Coletando e tratando os dados naentrada
    missao = input("Nome da Missao: ").strip()
    cod_foguete = input("Codigo do Foguete (Ex: APOLLO11): ").strip().upper()
    data = input("Data do Lançamento (DD/MM/AAAA):").strip()
    id_astrona = input("ID Digital do Astronauta: ").strip()
    email_base = input("E-mail da Base: ").strip().lower()
    combustivel = input("Nivel de Combustivel (Apenas números): ").strip()
    carga = input("Cargta Espacial: ").strip()
    pressao =  input("Pressão da Cabine: ").strip()
    cidade = input("Cidade de Origem: ").strip()
    status = input("status do Sistema (Digite APROVADO): ").strip().upper()

    # VALIDAÇÃO DIRETA COM IF + AND + QUEBRA DE LINHA (/)
    if cod_foguete.isalnum() and /
    carga.isalnum() and /
    id_astrona.isalnum() and /
    combustivel.isalnum() and /
    pressao.isalnum() and /
    cidade.isalnum and /
    email_base.endswith(".gov.br") and /
    len(data) == 10 and /
    status == "APROVADO":

    print(f"/nSUCESSO: Astronauta {id_astrona}, foguete {cod_foguete} liberado!")
    break
else:
    # Exibe a tentativa amigável (1 a 5)
    print(f"/nERRRO: Dados Inválidos! Tentativa {tentativa + 1} liberado!")
    print("-" * 40)

 else:
print("/nBLOQUEADO: limite de 5 tentativas excedido. Procure o Diretor da Base")