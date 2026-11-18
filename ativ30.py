print('----matrícula do veículo----')
proprietário = input ('nome do proprietário ')
modelo = input ('modelo do veículo ')
placa = input ('placa do veículo ')
Chassi = input ('Chassi do veículo ')
cor = input ('cor do veículo ')
ano = input ('qual o ano do carro? ')
if len(proprietário) > 2 and len(modelo) > 2 and len(placa) == 7 and len(Chassi) == 10 and len(cor) > 2 and len(ano) == 4:
  print(f'Olá, {proprietário} você quer matricular um veículo do modelo {modelo} com a placa {placa}, com o chassi {Chassi}, a cor do veículo é {cor} do ano {ano}');
  
else:
    print('não foi possível matricular o veículo. ')
print('-'*42)