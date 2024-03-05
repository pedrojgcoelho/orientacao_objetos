class Compra(Transacao):
    def __init__(self, dataCompra, produto, fornecedor, quantidade, precoUnitario):
        super().__init__(dataCompra, produto, quantidade)
        self.fornecedor = fornecedor
        self.precoUnitario = precoUnitario

    def valorTotal(self):
        return self.quantidade * self.precoUnitario
