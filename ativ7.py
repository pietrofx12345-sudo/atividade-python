Aparelho = input ("qual o status do seu aparelho: quebrado/travado/ligado ")

if Aparelho == "Ligado":
    print("Acesse o menu de configurações para atualizar o sistema ")
elif Aparelho == "Travado":

    print("Pressione os 'botões ligar' e 'volume' por 10 segundos para reiniciar.")
elif Aparelho == "Quebrado":
    print("Encaminhando para o setor de assistência física para reparo de hardware.")
else:
    print("Opção nao reconhecida. Deseja falar com um atendente humano?")