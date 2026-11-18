print("--- PLATAFORMA DE E-COMMERCE E DESPACHO DE PEDIDOS ---")

for tentativa in range(5):
    comprador = input("Nome do Comprador: ").strip().title()
    sobrenome = input("Sobrenome: ").strip().title()
    cidade = input("Cidade de Entrega: ").strip().title()
    estado = input("Estado Federativo: ").strip().upper()
    rastreamento = input("Código de Rastreamento: ").strip().upper()
    sku = input("SKU do Produto: ").strip()
    quantidade = input("Quantidade Comprada: ").strip()
    valor = input("Valor Total em Reais: ").strip()
    data = input("Data da Postagem (DD-MM-AAAA): ").strip()
    email = input("E-mail do Cliente: ").strip().lower()
    cvv = input("Código de Validação do Cartão: ").strip()
    status = input("Status da Entrega (DESPACHADO): ").strip().upper()

    data_formatada = data.replace("-", "/")

    if comprador.replace(" ", "").isalpha() and \
       sobrenome.replace(" ", "").isalpha() and \
       cidade.replace(" ", "").isalpha() and \
       estado.isalpha() and \
       rastreamento.startswith("LOG-") and \
       sku.isalnum() and \
       quantidade.isdigit() and \
       valor.isdigit() and \
       data_formatada.count("/") == 2 and \
       len(data_formatada) == 10 and \
       email.endswith(".com.br") and \
       status == "DESPACHADO":

        cvv_oculto = "*" * len(cvv)

        print(f"\nSUCESSO: Pedido de {comprador} despachado para {cidade}, {estado}!")
        print(f"Rastreamento: {rastreamento} | Data: {data_formatada} | Código Protegido: {cvv_oculto}")
        break
    else:
        print(f"\nERRO: Dados inválidos! Tentativa {tentativa + 1} de 5.")
        print("-" * 40)
else:
    print("\nACESSO NEGADO: 5 tentativas esgotadas.")