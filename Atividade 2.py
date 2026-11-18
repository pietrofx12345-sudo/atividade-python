# 02. Plataforma de Comércio Exterior & Importação Aduaneira
# Enunciado (12 Entradas): Noma do Importador, Razão Social, Porto de Origem, Perts de Destino, Código de Container, Mimaro da Declaragan Quaritada de tens, Peso Bruto, Código Taritário, Data do Despacho (DD/MM/AAAA) E-mail da Allandega, Perecer Fiscal (LIBERADO) Regras Nome do krportador, Razão Social, Porto de Origem e Porto de Destino devem conter apenas letras (isalpha() Código do Contamer Código Taritário devem ser alfanuméricos (isalnus()). Número da Declaração, Cuantidade a Peso Brute devem corter apenas digito (indigit()). OE-mail deve canter "" e termenar comgov.br" (endswith()). A Dasa deve pennur 10 caracteres lem() Paracer deve BLIBERADO
# 03. Sistema Hospitalar de Unidade do Terapia intensiva (UTI)
# Enunciado (12 Entradas): Nome do Pacients, Especialdade Médica, CRM do Médico, Código de Leila Frequência Cardiaca, Pranado Slanética, Saturação de Cogério, Temperatura Corporal, Medicamento Prescrits, Data da Advisão (DD/BAAAA, E mal do Hoepts, Glatus Climaco (RSTAVEL)
# Ragras Noria do Pacients, Especialidade e Medicamaran devem ser spenas lesbian (Analpha()) CRM Lado devem ser απάνες (Δ)) Frequência, Pressão, Baturação e Temperatura devem ser unicamente rúmeras (Andigit() deve corter & caracteres (en) E-mail deve terminar com med br" (andwith() Stamun deve ser "ESTAVEL

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