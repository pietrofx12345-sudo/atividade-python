print("--- registros de criptoativos ---")
# código de foguete e carga espacial devem ser alfanuméricos (.isalnum()). ID do astronauta e combustível devem conter apenas números (.isdigit()).
Nome_Cliente = input("Nome do cliente: ").strip()
Nome_da_criptomoeda = input("Nome da criptomoeda: ").strip()
codigo_hash = input("Código hash: ").strip()
data_de_transacao = input("Data de transação (dd/mm/aaaa): ").strip()
id_bloco = input("ID do bloco: ").strip()
quantidade_moedas= input("Quantidade de moedas: ").strip()
Confirmacao_autenticacao= input("confirmacao e autentificacao: ").strip()
email_suporte = input("Email da base de controle: ").strip()

if (Nome_Cliente.isalpha() and Nome_da_criptomoeda.isalnum() and codigo_hash.isalnum() and
        data_de_transacao != "dd/mm/aaaa" and id_bloco.isdigit() and quantidade_moedas.isdigit() and
        Confirmacao_autenticacao.isalpha() and email_suporte.count("@") == 1 and email_suporte.endswith(".com")):
    print("Cadastro válido")
else:    
    print("Cadastro inválido, tente novamente")