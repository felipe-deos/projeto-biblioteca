from livro.livro_repsitorio import livros
def listarLivros():
    print('---Lista de livros---')
    for livro in livros:
        print(f"ID: {livro['id']}")
        print(f"Titulo:{livro['tilulo']}")
        print(f"Editora:{livro['editora']}")
        print(f"Disponivel:{livro['disponivel']}")
        print("*"*50)

    if __name__=="__main__":
        listarLivros()