print("--- CADASTRO DE COFRE ELETRONICO---")

for tentativa in range(3):

    usuário = input("digite seu usuário:  ").strip().upper()
    senha_master = input("digite sua senha: ").strip()
    palavras_de_segurança = input("digite sua palavra de segurança: ").strip().upper()
    código_de_cofre = input("digite o código de cofre: ").strip()
    cidade_de_origem = input("digite sua cidade de origem: ").strip()
    email_de_recuperação = input("digite o email de recuperação: ").strip().lower()

    if len(usuário) > 3 and \
       senha_master.isdigit() and len(senha_master) ==6 and \
       palavras_de_segurança == "FALCAO" and \
       len(código_de_cofre) ==4 and \
       cidade_de_origem.isalpha() and \
       len (email_de_recuperação) > 10 :
    

        print(f"Acesso liberado! Bem-vindo ao sistema, {usuário}.")
        break

    else:
        print(f"Erro nos dados! Tentativa {tentativa + 1} de 3.")

else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")