print('----Prontuário Médico----')
paciente = input ('nome do paciente ')
medico = input ('nome do médico ')
hospital = input ('hospital ')
crm = input ('CRM ')
ala = input ('Ala médica ')
sintoma = input ('sintoma do paciente ')
if len(paciente) > 4 and len(medico) > 4 and len(hospital) > 4 and len(crm) == 5 and len(ala) == 2 and len(sintoma) > 4:
  print(f'Olá, {paciente} você tem uma consulta com o(a) {medico} no hospital {hospital}, sua CRM é {crm}, ala médica da consulta é {ala} sintôma do paciente é {sintoma}');
  
else:
    print('não foi possível identificar o paciente. ')
print('-'*42)