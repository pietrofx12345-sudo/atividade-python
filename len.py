senha = input("digite sua senha :").strip() # Borracha inteligente

if len(senha) < 8:
    print("sua senha é curta demais")
else:
    print("senha aceita.")