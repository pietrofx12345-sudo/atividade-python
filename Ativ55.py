print("---Sistema de Matricula Universitario---")
aluno = input("nome do aluno: ").strip()
cpf = input("CPF do aluno: ").strip()
rg = input("RG do aluno: ").strip()
idade = input("idade: ").strip()
curso = input("curso: ").strip()
semestre = input("semestre: ").strip()
turno = input("turno: ").strip()
campus = input("campus: ").strip()
email_a = input("email do aluno: ").strip()
ra = input("RA do aluno: ").strip()
bolsista = input("bolsista (sim/não): ").strip()
coordenador = input("coordenador: ").strip()
telefone = input("telefone: ").strip()
data_matricula = input("data de matrícula: ").strip()
status = input("status: ").strip()

if aluno.isalpha() and cpf.isdigit() == 11 and rg.isdigit() and \
     idade.isdigit() and curso.isalpha\
    and semestre.isdigit() and \
         campus.isalpha() and email_a.count("@") == 1 and email_a.endswith(".com") and \
           ra.isdigit() and bolsista.lower() in ("sim", "não") and \
            coordenador.isalpha() and telefone.isdigit() and \
             data_matricula != "dd/mm/aaaa" and \
              status.isalpha() and status.upper() == "MATRICULADO":
    print("Cadastro valido")
else:
    print("Cadastro inválido") 