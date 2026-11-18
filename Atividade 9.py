print("--------------------------------Cadastro Geral de Propriedade e Registro Imobiliário-----------------------------------------")

for tentativas in range(3):

    nome_titular = input("Digite o nome do titular: ").strip()
    sobrenome = input("Digite o sobrenome: ").strip()
    bairro_imovel = input("Digite o bairro do imóvel: ").strip()
    cidade_registro = input("Digite a cidade do registro: ").strip()
    numero_matricula = input("Digite o número da matrícula: ").strip()
    codigo_iptu = input("Digite o código do IPTU: ").strip()
    area_metros = input("Digite a área em metros: ").strip()
    valor_venal = input("Digite o valor venal: ").strip()
    numero_cartorio = input("Digite o número do cartório: ").strip()
    data_escritura = input("Digite a data da escritura (DD/MM/AAAA): ").strip()
    email_cartorio = input("Digite o e-mail do cartório: ").strip()
    situacao_registro = input("Digite a situação do registro: ").strip().upper()

    if (nome_titular.isalpha() and
        sobrenome.isalpha() and
        bairro_imovel.isalpha() and
        cidade_registro.isalpha() and
        numero_matricula.isalnum() and
        codigo_iptu.isalnum() and
        area_metros.isdigit() and
        valor_venal.isdigit() and
        numero_cartorio.isdigit() and
        len(data_escritura) == 10 and
        email_cartorio.endswith(".cartorio.not.br") and
        situacao_registro == "REGISTRADO"):

        print(f"\nSUCESSO: imóvel de {nome_titular}, registro imobiliário realizado!")
        break

    else:
        print(f"\nERRO: Dados invalidos! {tentativas + 1} de 3")
        print("-" * 40)

else:
    print("\nAcesso negado")
