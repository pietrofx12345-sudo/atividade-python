nome = input("Digite seu nome:")

# Precisamos converter o input para o float (número decimal)
nota = float(input("Qual é a nota?"))

if nota >= 7:
    print("Parabéns", nome, "você foi Aprovado!")
else:
    print (f"sinto muito, {nome}, você foi Reprovado.")