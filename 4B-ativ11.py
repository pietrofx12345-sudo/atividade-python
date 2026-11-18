print("--- Controle de Aceso ao Datacenter de Segurança Nacional ---")

for tentativa in range(5):
    especialista = input("Nome do especialista: ").strip().title()
    area = input("Área de Atuação: ").strip().title()
    empresa = input("Empresa Contratada: ").strip().upper()
    cidade = input("Cidade da Sede: ").strip().title()
    rack = input("Código do Rack: ").strip().upper()
    id = input("ID do Gabinete: ").strip()
    temperatura = input("Temperatura do Corredor Frio: ").strip()
    umidade = input("Umidade Relativa do Ar: ").strip()
    data = input("Data do Acesso (DD-MM-AAAA): ").strip()
    email = input("E-mail Corporativo: ").strip().lower()
    senha = input("Senha Biométrica: ").strip()
    liberação = input("Liberação da Porta (ABERTO): ").strip().upper()
    data_formatada = data.replace("-", "/")

    if especialista.isalpha and \
       area.isalpha and \
       cidade.isalpha and \
       rack.startswith("RACK-") and \
       id.isalnum() and \
       temperatura.isdigit() and \
       umidade.isdigit() and \
       data_formatada.count("/") == 2 and \
       len(data_formatada) == 10 and \
       email.endswith(".datacenter.com") and \
       liberação == "ABERTO":

        senha = "*" * len(senha)

        print(f"\nSUCESSO")
        break
    else:
        print(f"\nERRO: Dados inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nACESSO NEGADO: 5 tentativas esgotadas.")