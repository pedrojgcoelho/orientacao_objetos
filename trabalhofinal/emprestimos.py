class Emprestimo:
    def listar_emprestimos(self,cod_usuario_parametro):
        lista_emprestimos: str
        lista_emprestimos = ''
        arquivo = "emprestimos.txt"
        with open(arquivo, "r") as f:
            linha: str
            for linha in f:
                codigo, cod_usuario, cod_livro, data = linha.split(",")
                cod_usuario = cod_usuario.strip()
                cod_usuario_parametro = cod_usuario_parametro.strip()
                if cod_usuario == cod_usuario_parametro:
                    lista_emprestimos = lista_emprestimos + '\nCódigo do Livro: ' + cod_livro + ' - Data do Empréstimo: ' + data + '\n'
        return lista_emprestimos          