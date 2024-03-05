class Carro(Veiculo):

    def __init__(self, modelo, placa, valor):
        super().__init__(placa, valor)
        self.modelo = modelo

    def calcularAluguel(self, dias):
        return self.valor * dias

