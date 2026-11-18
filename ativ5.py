semáforo = input ("digite a cor que está o semáforo: ")

if semáforo == "Verde":
    print("pode passar a segunda marcha e passar o semáforo.")
elif semáforo == "Amarelo":

    print("Passe a marcha, reduza a velocidade e aguarde o sinal verde.")
elif semáforo == "Vermelho":
    print("Freie o carro e aguarde até o sinal ficar verde.")
else:
    print("Cor inválida.")