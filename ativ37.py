print("---Cadastro de um livro na biblioteca---")

for tentativa in range(3):
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    genero = input("Gênero: ").strip().upper()
    isbn = input("Número do ISBN: ").strip()
    paginas = input("Quantidade de páginas: ").strip()
    estante = input("Código da estante: ").strip()
    if (
       isbn.isdigit and paginas.isdigit and estante != "000" and genero == "DRAMA"
    ):
        print("Livro cadastrado com sucesso!")
        break

    else:
        print("Tente novamente!")
        print("-" * 30)

else:
    print("Muitas tentativas falhas. Tente novamente mais tarde!.")

print('-' * 42)