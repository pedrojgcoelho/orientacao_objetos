class Produto:
    def __init__(self, nome, quantidadeEstoque, precoUnitario, estoqueMinimo, estoqueMaximo):
        self.nome = nome
        self.quantidadeEstoque = quantidadeEstoque
        self.precoUnitario = precoUnitario
        self.estoqueMinimo = estoqueMinimo
        self.estoqueMaximo = estoqueMaximo

    def debitarEstoque(self, quantidade):
        self.quantidadeEstoque -= quantidade

    def creditarEstoque(self, quantidade):
        self.quantidadeEstoque += quantidade

    def verificarEstoqueBaixo(self):
        return self.quantidadeEstoque <= self.estoqueMinimo

    def verificarEstoqueInsuficiente(self, quantidade):
        return self.quantidadeEstoque < quantidade

    def verificarEstoqueExcedente(self, quantidade):
        return self.quantidadeEstoque > quantidade

    def calcularValorVenda(self, quantidade):
        return self.quantidade * self.precoUnitario
