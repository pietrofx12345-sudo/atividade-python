print("---Entrega por aplicativo---")

entregador = input("nome do entregador: ").strip()
veiculo = input("veículo: ").strip()
codigo = input("código de entrega: ").strip()
distancia = input("distancia calculada: ").strip()
cidade = input("Cidade: ").strip()
observação = input("Observações: ").strip()

if len(entregador) and entregador.isalpha and \
   len(veiculo) > 3 and veiculo.isalpha and \
   codigo == 6 and codigo.isdigit and \
   distancia > 2 and distancia.isdigit and \
   cidade != "BRASILIA" and cidade.isalpha and \
   observação != "nenhuma" and observação.isalpha:

    print("Entrega registrada com sucesso!")
else:
    print("erro: não foi possivel registrar sua entrega")
    print("-" * 30)