from livro_repsitorio import livros
from livro.buscar_livro import buscarLivro
def emprestarLivro(id: int):
    livro = buscarLivro(id)

    if not livro:
        print('Erro: Livro não encontrado')
        return

    if not livro['disponivel']:
        print('Erro: O livro nao está disponivel')
        return
    livro['disponivel']=False
    print('Emprestimo Realizado Com Sucesso')

if __name__=="__main__":
    emprestarLivro(1)
    print(livros)

def devolverLivro(id: int):
    livro=buscarLivro(id)

    if not livro:
        print('Erro: Livro nâo encontrado')
        return

    if livro['disponivel']:
        print('Erro: O livro ja está disponivel')
        return

    livro['disponivel'] = True
    print('Livro devolvido com sucesso!')

if __name__ == "__main__":
    emprestarLivro(1)
    print(livros)