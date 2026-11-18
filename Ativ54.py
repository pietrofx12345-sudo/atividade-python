print("---Controle de estoque industrial---")
maquina = input("nome da máquina: ")
serie = input("qual a serie: ")
operador = input("qual o operador: ")
turno = input("qual o turno: ")
pecas_dia = input("peças do dia: ")
defeito = input("defeito: ")
email_t = input("email do técnico: ")
fabrica = input("fabrica: ")
setor = input("setor: ")
corredor = input("corredor: ")
gaveta = input("gaveta: ")
fornecedor = input("fornecedor: ")
cnpj_f = input("CNPJ do fornecedor: ")
data_manut = input("Data de manutenção: ")
status = input("Status: ")

if (maquina.upper() and serie.isalnum() and turno.upper()
        and pecas_dia.isdigit() and defeito
        and email_t.count("@") == 1 and email_t.endswith(".com")
        and fabrica.upper() and setor.isalpha() and gaveta.isdigit()
        and fornecedor.isalpha() and cnpj_f.isdigit()
        and data_manut != "dd/mm/aaaa"
        and status.isalpha() and status.upper() == "OPERACIONAL"):
    print("Cadastro valido")
else:
    print("Cadastro inválido")