# O range(3) faz o codigo repetir 0, 1 e 2(total de 3 vezes ) . 
# Este ' else' pertence ao 'for' . Ele só roda se o laço terminar SEM o break .


senha_correta = "abacate"
for tentativa in range(3):
    chute = input("Digite a senha: ")
    if chute ==senha_correta: 
        print("senha correta! entrando...")
        break # O break interrompe o 'for' imediatamentese ele acertar.
    else:
        print ("senha incorreta!")
else:
    # Este ' else' pertence ao 'for' . Ele só roda se o laço terminar Sem o break.
    print("conta bloqueada após 3 tentativas falhas. ")