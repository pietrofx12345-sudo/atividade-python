print('----Cadastro de Aluno em Universidade----')

for tentativa in range(3):
    nome = input('Qual seu nome? ').strip()
    curso = input('Qual seu curso? ').strip()
    matricula = input('Qual o número de matrícula? ').strip()
    ano = input('Qual seu ano? ').strip()
    campus = input('Qual seu Campus? ').strip()
    senha = input('Qual sua senha? ').strip()

    if len(nome) > 0 and nome.isalpha() and \
       len(curso) > 0 and curso.isalpha() and \
       len(matricula) == 6 and matricula.isdigit() and \
       len(ano) == 4 and ano.isdigit() and \
       campus == "CENTRAL" and \
       senha != "123456": 
         
        print(f'{nome}, você foi cadastrado(a) com sucesso!')
        print(f'Curso: {curso} | Ano: {ano} | Campus: {campus} | Matrícula: {matricula}')
        break
    else:
        print("\nErro no cadastro! Tente novamente!")
        print("-" * 42)
else:
    print('Muitas tentativas falhas. Tente novamente mais tarde!')

print('-' * 42)