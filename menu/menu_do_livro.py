from livro.livro_repsitorio import livros
from livro.registrar import registrarlivro
from livro.listar_livros import listarLivros
from livro.buscar_livro import buscarLivro
from livro.editar_livro import editarLivro
from livro.deletar_livro import deletarLivro


def menuBiblioteca():
    while True:
        print('---Menu Biblioteca---')
        print('1-Cadastrar livro')
        print('2-Editar Livro')
        print('3-Remover Livro')
        print('4-Buscar Livro')
        print('5- Listar todos os livros')
        print('6-Sair')
        opcao = input('Selecione uma opção:')
        if opcao == '1':
            titulo = input('Digite o titulo do livro:')
            editora = input('Digite a editora:')
            disponivel = input('Qual a disponibilidade?'
                               '1-True /2 - False:')
            if disponivel == '1':
                editarLivro(id, titulo, editora, True)
            else:
                editarLivro(id, titulo, editora, False)

        elif opcao=='3':
            id=int(input('Informe o id do livro:'))
            deletarLivro(id)
        elif opcao=='4':
            id=int(input('Informe o id do livro:'))
            print(buscarLivro(id))
        elif opcao=='5':
            listarLivros()
        elif opcao=='6':
            break
if __name__ == '__main__':
    menuBiblioteca()