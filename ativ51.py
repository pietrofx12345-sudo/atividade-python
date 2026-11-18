print("---prontuario de clinica veterinaria---")
pet = input("nome do seu pet: ")
especie = input("qual a Especie: ")
Raça = input("qual o raça: ")
Idade = input("Idade: ")
Peso = input("Qual o Peso: ")
Tutor = input("Nome do tutor: ")
Cpf = input("Cpf do Tutor: ")
Email = input("E-mail do Tutor: ")
Fone = input("Fone: ")
Vacina = input("qual a vacina: ")
Clinica = input("Qual a Clinica: ")
Veterinario = input("Nome do Veterinario: ")
crmv = input("CRMV: ")
data = input("Data: ")
status = input("Status: ")

if pet.isalpha() and especie.isalpha() and Raça.isalpha() and Idade.isdigit()  and\
Peso.isdigit() and len.Tutor and Cpf.isalpha() == 11  and  Email.isdigit() and Fone.isalpha() and Vacina.isalpha() and\
Clinica.isalpha() and Veterinario.isdigit() and crmv.isalpha()> 3 and data.isalpha() != ('dd/mm/aaaa') and  status.isalpha()and status!="OK":
    print("protuario valido")
else:
    print("Prontuarioc inválido")