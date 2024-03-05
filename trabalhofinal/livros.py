class Livro:
    def listar_livros(self):
        listagem_livros: str
        listagem_livros = ''
        arquivo = "livros.txt"
        with open(arquivo, "r") as f:
            linha: str
            for linha in f:
                titulo, autor, codigo = linha.split(",")
                codigo = codigo.strip()
                autor = autor.strip()
                titulo = titulo.strip()
                listagem_livros = listagem_livros + '\nCódigo do Livro: ' + codigo + ' - Título: ' + titulo + ' - Autor: ' + autor + '\n'
        return listagem_livros