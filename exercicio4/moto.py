class Moto(Veiculo):

    def __init__(self, cilindrada, placa, valor):
        super().__init__(placa, valor)
        self.cilindrada = cilindrada

    def calcularAluguel(self, dias):
        return self.valor * dias * self.cilindrada / 1000

