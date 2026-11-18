#o usuario informa que tipo de cliente ele é:
tipo_cliente = input ("digite seu perfil(1: estudante/ 2: Idoso / 3: Público comum): ")

if tipo_cliente == "1":
    print("Voce tem direito a 50% de desconto (Meia estudante).")
elif tipo_cliente == "2":

    print("Você tem direito a 50% de desconto (meia entrada idoso).")
else:
    print("você pagará o valor de entrada inteira.")

    #o elif é a alternativa específica: não é estudante?
    #Mas é idoso?

    #Se nao caiu nas regras de desconto acima, cai no else automaticamente
    #Dois sinais de igual (==) é uma pergunta. diferente do = que guarda um valor 
    ## 0 == Compara os valores
