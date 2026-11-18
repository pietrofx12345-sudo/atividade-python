#Criamos uma lista de nomes para o programa percorrer
convidados = ["ana", "bruno", "carla"]

#O FOR funciona como um laço que pega um nome por vez da lista
for pessoa in convidados:
    #O INPUT para o programa e espera o usuario digitar a idade
    #O INT transforma o que foi digitado em um numero inteiro
    idade = int (input("qual a idade de " + pessoa + "? " ))
    #O IF faz a pergunta: a idade é maior ou igual a 18?
    if idade >= 18:
        #Se for verdade, o python executa essa linha:
        print(pessoa, "é maior de idade, acesso liberado!")

        #O ELSE é o "caso contrário" (se a pergunta do if for falsa)
    else:
        #Se for menor de 18, o python executa ess linha:
        print(pessoa, "é menor de idade, acesso negado!")