print ("--------------------------------Plataforma de Comércio Exterior & Importação Aduaneira-----------------------------------------")

for tentativas in range(3):
 nome_importador = input("Digite o nome do importador: ").strip()
 razão_social = input("Digite o razão_social: ").strip()
 porto = input("Digite o porto: ").strip()
 destino = input("Digite o salrio base: ").strip()
 container = input("Digite as container trabalhadas: ").strip()
 declaraçao = input("Digite o declaraçao do banco: ").strip()
 quantidade = input("Digite a quantidade funcional do porto ocupado: ").strip()
 peso = input("Digite o E-mail da transportadora: ").strip()
 codigo = input("Digite o status do envio: ").strip().upper()
 data = input("Digite o status do envio: ").strip().upper()
 email = input("Digite o status do envio: ").strip().upper()
 parecer = input("Digite o status do envio: ").strip().upper()

 if nome_importador.isalpha() and \
     razão_social.isalpha() and \
     porto.isalpha() and \
     destino.isalpha() and \
     container.isalnum() and \
     codigo.isalnum() and \
     declaraçao.isdigit() and \
     quantidade.isdigit() and \
     peso.isdigit() and \
     data.count("/") == 2 and\
     len(data) == 10 and\
     email.count("@") == 1 and\
     email.endswith(".gov.br") and\
     parecer == "VALIDADO":

      print(f"\nSUCESSO: importador {nome_importador}, sistema {razão_social} liberado!")
      break

 else:

  print(f"\nERRO: Dados invalidos! {tentativas + 1} de 3")
  print("-" * 40)
  
 
else:
    print("Acesso negado")
