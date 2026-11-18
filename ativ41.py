print("--- CADASTRO DE TRIPULAÇAO ESPACIAL---")

for tentativa in range(3):

   nome = input("digite seu nome:  ").strip()
   planeta = input("digite o planeta: ").strip()
   email = input("digite o seu email: ").strip().lower()
   cargo = input("digite o seu cargo: ").strip().upper()
   ID = input("digite o seu ID: ").strip()
   peso= input("digite o seu peso: ").strip()
   codigo_de_missao= input("digite o seu codigo: ").strip()
   nave= input("digite a sua nave: ").strip()


   if nome.isalpha() and planeta.isalpha() and \
      cargo =="PILOTO" and \
      ID.isdigit() and \
      peso.isdigit() and \
      codigo_de_missao =="MARTE2026" and \
      nave != "TESTE" :
    

        print(f"Acesso liberado! Bem-vindo ao sistema, {nome}.")
        break

   else:
        print(f"Erro nos dados! Tentativa {tentativa + 1} de 3.") 

else:
    print("SISTEMA BLOQUEADO. Alerta de intrusão enviado à segurança.")
