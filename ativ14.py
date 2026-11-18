crianças = ['Carlos', 'Natanael', 'Pietro', 'Kevin', 'Kaique', 'danilows']
for nome in crianças:
 for tentativa in range(6):


  peso = float(input(f'Qual é o peso de {nome}:'))
if peso <= 40:
 print(f'{nome}: Pode balançar')
else:
 print(f'{nome}:Peso acima do limite')