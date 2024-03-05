class Venda(Transacao):
    def __init__(self, dataVenda, cliente, produto, quantidade, precoUnitario):
        super().__init__(dataVenda, produto, quantidade)
        self.cliente = cliente
        self.precoUnitario = precoUnitario

    def valorTotal(self):
        return self.quantidade * self.precoUnitario
