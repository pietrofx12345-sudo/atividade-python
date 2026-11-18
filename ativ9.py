user =["admin", "suporte", "financeiro", "funcionario comunm", "cliente"]
for pessoa in user:

    senha = input (f"qual é a senha de acesso, {pessoa}?:")
    if senha =="admin":
        print(f"acesso liberado, {pessoa}")
    else:
        print(f"senha incorreto , acesso negado, {pessoa}")

        #O for e uma palavra reservada que sinaliza o inicio de um ciclo. ele diz ao ocmputador 
        #"Prepare-se, pois vamos repetir as instruções que vem logo abaixo para um grupo de coisas".

        #usuario (a variavel temporária): Este nome voce inventa, pense nela como uma caixinha vazia que o
        # python vai usar para carregar um nome de cada vez.
        #in funcionarios (A origem): aqui voce indica onde o python deve buscar os dados. funcionarios
        #é o nome da sua lista original que contém os três cargos.

        #O python nao entende o significado  das palavras (ele nao sabe o que é um "usuario" ou um "gerente")]
        #ele apenas segue a regra:
        #"Pegue o proximo item da lista e coloque dentro deste nome que eu inventei".
        #funcionarios (o nome da lista): é o nome que voce deu para esse grupo. è como o rotulo da pasta.