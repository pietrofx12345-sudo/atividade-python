print("--------------------------------Sistema Hospitalar de Unidade de Terapia Intensiva (UTI)-----------------------------------------")

for tentativas in range(3):

    nome_paciente = input("Digite o nome do paciente: ").strip()
    especialidade = input("Digite a especialidade médica: ").strip()
    crm_medico = input("Digite o CRM do médico: ").strip()
    codigo_leito = input("Digite o código do leito: ").strip()
    frequencia_cardiaca = input("Digite a frequência cardíaca: ").strip()
    pressao_sistolica = input("Digite a pressão sistólica: ").strip()
    saturacao_oxigenio = input("Digite a saturação de oxigênio: ").strip()
    temperatura_corporal = input("Digite a temperatura corporal: ").strip()
    medicamento_prescrito = input("Digite o medicamento prescrito: ").strip()
    data_admissao = input("Digite a data de admissão (DD/MM/AAAA): ").strip()
    email_hospital = input("Digite o e-mail do hospital: ").strip()
    status_clinico = input("Digite o status clínico: ").strip().upper()

    if (nome_paciente.isalpha() and
        especialidade.isalpha() and
        medicamento_prescrito.isalpha() and
        crm_medico.isalnum() and
        codigo_leito.isalnum() and
        frequencia_cardiaca.isdigit() and
        pressao_sistolica.isdigit() and
        saturacao_oxigenio.isdigit() and
        temperatura_corporal.isdigit() and
        len(crm_medico) == 6 and
        email_hospital.endswith(".med.br") and
        status_clinico == "ESTAVEL"):

        print(f"\nSUCESSO: paciente {nome_paciente}, atendimento autorizado!")
        break

    else:
        print(f"\nERRO: Dados invalidos! {tentativas + 1} de 3")
        print("-" * 40)

else:
    print("\nAcesso negado")