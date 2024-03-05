class Veiculo:

    def __init__(self, placa, valor):
        self.placa = placa
        self.valor = valor
        self.alugado = False
        self.historico = []

    def alugar(self, cliente, dias):
        if self.alugado:
            raise ValueError("Veículo já alugado")

        self.alugado = True
        self.historico.append((cliente, dias))

    def devolver(self):
        if not self.alugado:
            raise ValueError("Veículo não alugado")

        self.alugado = False

    def listarHistorico(self):
        for cliente, dias in self.historico:
            print(f"Cliente: {cliente}, Dias: {dias}")