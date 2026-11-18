print('----Reserva de hotel internacional----')
hospede = input ('Qual o nome do hospede? ')
país = input (' Qual país deseja se hospedar? ')
passaporte = input ('Número do passaporte ')
quarto = input (' número do quarto ')
data = input ('Data ')
reserva = input ('Código de reserva ')
if len(hospede) > 3 and len(país) > 3 and len(passaporte) == 6 and len(quarto) == 3 and len(data) == 8 and len(reserva) == 4:
  print(f'Olá, {hospede} você tem reserva no(a) {país} e possui o passaporte {passaporte}, seu quarto é o número {quarto}, data de reserva: {data} seu código é {reserva}');
  
else:
    print('não foi possível identificar sua reserva. ')
print('-'*42)