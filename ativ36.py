print("---Cadastro de Produto Químico---")

for tentativa in range(3):
    substancia = input("Substancia: ").strip()
    tipo = input("Tipo: ").strip().upper()
    lote = input("Lote: ").strip()
    responsavel = input("Responsavel: ").strip()
    crm = input("CRM: ").strip()
    validade = input("Validade: ").strip()
    if (
       tipo == "SOLVENTE" and lote != "000" and len(crm) == 5 and len(validade) == 8
    ):
        print("Produto cadastrado com sucesso!")
        break

    else:
        print("Tente novamente!")
        print("-" * 30)

else:
    print("Muitas tentativas falhas. Tente novamente mais tarde!.")

print('-' * 42)