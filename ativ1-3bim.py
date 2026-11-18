print("--- sistema de ")

for tentativa in range(5):
    # Coletando e tratando os dados naentrada
    missao = input("Nome da Missao: ").strip()
    cod_foguete = input("Codigo do  (Ex: APOLLO11): ").strip().upper()
    data = input("Data do  (DD/MM/AAAA):").strip()
    id_astrona = input("ID Digital do : ").strip()
    email_base = input("E-mail da : ").strip().lower()
    combustivel = input("Nivel de Combustivel (Apenas números): ").strip()
    carga = input("Cargta Espacial: ").strip()
    pressao =  input("Pressão da Cabine: ").strip()
    cidade = input("Cidade de Origem: ").strip()
    status = input("status do Sistema (Digite APROVADO): ").strip().upper()


