print("--- Painel de controle de foguete espacial ---")
# código de foguete e carga espacial devem ser alfanuméricos (.isalnum()). ID do astronauta e combustível devem conter apenas números (.isdigit()).
codigo_foguete = input("Código do foguete: ").strip()
carga_espacial = input("Carga espacial: ").strip()
nome_missao = input("Nome da missão: ").strip()
data_lancamento = input("Data de lançamento (dd/mm/aaaa): ").strip()
id_astronauta = input("ID do astronauta: ").strip()
combustivel = input("Quantidade de combustível (litros): ").strip()
status_sistema = input("Status do sistema: ").strip()
email_base = input("Email da base de controle: ").strip()

if (codigo_foguete.isalnum() and carga_espacial.isalnum() and nome_missao.isalnum() and
        data_lancamento != "dd/mm/aaaa" and id_astronauta.isdigit() and combustivel.isdigit() and
        status_sistema.isalpha() and email_base.count("@") == 1 and email_base.endswith(".com")):
    print("Cadastro válido")
else:    
    print("Cadastro inválido, tente novamente")