print("---manifesto de carga de navio cargueiro---")

navio = input("Navio: ")
capitao = input("Capitão: ")
origem = input("Origem: ")
destino = input("Destino: ")
carga = input("Carga: ")
peso = input("Peso em toneladas: ")
containers = input("Containers: ")
valor = input("Valor: ")
seguro = input("Seguro: ")
porto = input("Porto: ")
empresa = input("Empresa: ")
licenca = input("Licença: ")
rota = input("Rota: ")
combustivel = input("Combustível: ")
chegada = input("Chegada: ")

if capitao.isalpha() and origem.isalpha() and licenca.isdigit() and len(licenca) == 8 and peso.isdigit() and destino.upper() == "EUROPA" and empresa != "FANTASMA" and rota.upper() == "SUL":
    print("Manifesto válido")
else:
    print("Manifesto inválido")