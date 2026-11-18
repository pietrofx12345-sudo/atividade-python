print("---Cadastro de Projeto de Engenharia---")
projeto = input("nome do seu projeto: ")
codigo = input("qual o código: ")
engenharia = input("Engenharia: ")
crea = input("CREA: ")
setor = input("Qual o setor: ")
orçamento = input("Qual o orçamento: ")
data_inicio = input("Data de início: ")
data_fim = input("Data de fim: ")
cidade = input("Qual a cidade: ")
uf = input("Qual a uf: ")
email_resp = input("Qual o email do responsável: ")
cliente = input("Nome do cliente: ")
cnpj_c = input("CNPJ: ")
prioridade = input("Prioridade: ")
status = input("Status: ")

if projeto.isalnum() and codigo.isalnum() and engenharia.isalpha() and cidade.isalpha() and crea.isdigit() and\
setor.isalnum() and orçamento.isdigit() and data_inicio.isalpha() != ('dd/mm/aaaa') and data_fim.isalpha() != ('dd/mm/aaaa')  and  uf.isalnum() and email_resp.count("@") == 1 and email_resp.endswith(".com") and cliente.isalpha and\
cnpj_c.isdigit() and cnpj_c == 14 and prioridade.isalpha() and status.isalpha()and status == "Aprovado":
    print("Cadastro valido")
else:
    print("Cadastro inválido")