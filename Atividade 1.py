print("--- Controle de acesso ao centro de pesquisa nuclear ---")

for tentativa in range(5):
    
    nome = input("Nome do pesquisador: ").strip()
    sobrenome = input("sobrenome do pesquisador: ").strip().upper()
    data_inspeção = input("Data de inspeção (DD/MM/AAAA):").strip()
    codigo_reator = input("codigo do reator : ").strip()
    email_instituição = input("E-mail da instituição : ").strip().lower()
    nivel_radiação = input("Nivel de radiação: ").strip()
    setor_acesso = input("setor de acesso: ").strip()
    cartão_acesso =  input("cartão de acesso: ").strip()
    id_crachá = input("id do crachá: ").strip()
    temperatura_nucleo = input("temperatura do nucleo: ").strip()
    cidade_laboratorio = input("Cidade do laboratorio: ").strip()
    status_segurança = input("status do Sistema (Digite APROVADO): ").strip().upper()

    if (nome.upper() and sobrenome.isalpha() and data_inspeção.upper()
        and codigo_reator.isdigit() and email_instituição
        and email_instituição.count("@") == 1 and email_instituição.endswith(".com")
        and nivel_radiação.upper() and setor_acesso.isalpha() and cartão_acesso.isdigit()
        and id_crachá.isalpha() and temperatura_nucleo.isdigit()
        and cidade_laboratorio != "dd/mm/aaaa"
        and status_segurança.isalpha() and status_segurança.upper() == "OPERACIONAL"):
     print ("Cadastro valido")
else:
    print("Cadastro inválido")

