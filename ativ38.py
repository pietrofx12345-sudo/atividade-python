print("---Registro de Ponto Eletrônico---")

for tentativa in range(3):
    funcionario = input("Funcionario: ").strip()
    unidade = input("unidade: ").strip()
    id = input("ID do crachá: ").strip()
    cargo = input("Cargo: ").strip()
    hora = input("Hora de Entrada: ").strip()
    cdv = input("Código de Verificação: ").strip()
    if (
       len(funcionario) > 3 and \
       unidade == "SUL" and \
       len(id) == 5 and id.isdigit and \
       cargo.isalpha and \
       len(hora) == 4 and hora.isdigit and \
       cdv !=  "123" 
    ):
        print("Registro concluido!")
        break

    else:
        print("Tente novamente!")
        print("-" * 30)

else:
    print("Muitas tentativas falhas. Tente novamente mais tarde!.")

print('-' * 42)