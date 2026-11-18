print("--- CADASTRO AVANÇADO COM PROTEÇÃO DE SENHA ---")

for tentativa in range(5):
    # 1.Entrada de dados e tratamento inicial
    nome = input("Nome do usuário: ").strip().title()
    "Kamilla Silva"
    chave_acesso = input("Chave de Acesso (Ex: SEC-889): ").strip()
    data_acesso = input("Data de acesso (DD-MM-AAAA): ").strip()
    senha = input("senha provisória (Minimo 6 caractéres): ").strip()

    # 2. Tratamento com .replace(): troca traço ' - ' por barra "/"
    data_formatada = data_acesso.replace("-", "/")

    # 3. Validação combinada com .startswith(), .count() e len()
    if chave_acesso.startswith("SEC.")and \
    len(data_formatada) == 10 and \
    len(senha) >= 6:

        # 4. Criação da máscara de proteção para esconder a senha no terminal
        senha_oculta = "*" * len(senha)

        print(f"\nSUCESSO: Usuário {nome} autenticado!")
        print(f"Data registrada: {data_formatada}")
        print(f"Senha protegida: {senha_oculta} {len(senha)} dígitos protegidos)")
        break
    else:
        print(f"\nERRO: Dados invalidos! tentativa {tentativa + 1} de 5. ")
        print("-" * 40)
else:
    print("\nBLOQUEADO: Limite de 5 tentativas atingido. Contate o suporte técnico.")