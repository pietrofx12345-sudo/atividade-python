Temperatura = float(input("Digite a temperatura climática:"))

if Temperatura > 30:
    print("Use roupas leves")
elif Temperatura >= 20:
    print("a temperatura está ambiente, use roupas de tecido normal ou leve mesmo como uma camiseta!")
elif Temperatura >= 10:
    print("leve um casaco leve")
else:
    print("Está muito frio! use roupas pesadas.")