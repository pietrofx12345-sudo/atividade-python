print("---controle de reator de fusao nuclear---")
Reator = input("Reator: ")
Elemento = input("Elemento: ")
Massa = input("Massa: ")
Calor = input("Calor: ")
Pressao = input("Pressao: ")
Fluxo = input("Fluxo: ")
Tecnico = input("Tecnico: ")
ID_tec = input("ID_tec: ")
Turno = input("Turno: ")
Estacao = input("Estacao: ")
Resfriamento = input("Resfriamento: ")
Energia = input("Energia: ")
Stastus = input("Stastus: ")
Emergencia = input("Emergencia: ")
Chave = input("Chave: ")

if Reator.isalpha() and Elemento.isalpha() and Massa.isdigit() and Calor.isdigit()  and\
Pressao.isdigit() and len.Fluxo > 1 and Tecnico.isalpha()  and  ID_tec.isdigit and Turno.isalpha() and Estacao.isalpha() and\
Resfriamento.isalpha() and Energia.isdigit() and Stastus.isalpha()== "ESTAVEL" and Emergencia.isalpha()and  Emergencia!="DESATIVADA" and Chave.isalpha()and Chave!="REATOR_ON":
    print("Cadastro válido")
else:
    print("Cadastro inválido")