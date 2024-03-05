class Transacao:
    def __init__(self, dataTransacao, produto, quantidade):
        self.dataTransacao = dataTransacao
        self.produto = produto
        self.quantidade = quantidade

    def __repr__(self):
        return f"{self.dataTransacao} - {self.produto} - {self.quantidade}"
