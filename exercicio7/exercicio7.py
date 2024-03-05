class Funcionário:

    def __init__(self, nome, salário_bruto, total_acréscimo, total_desconto):
        self.nome = nome
        self.salário_bruto = salário_bruto
        self.total_acréscimo = total_acréscimo
        self.total_desconto = total_desconto

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def salário_bruto(self):
        return self.__salário_bruto

    @salário_bruto.setter
    def salário_bruto(self, salário_bruto):
        self.__salário_bruto = salário_bruto

    @property
    def total_acréscimo(self):
        return self.__total_acréscimo

    @total_acréscimo.setter
    def total_acréscimo(self, total_acréscimo):
        self.__total_acréscimo = total_acréscimo

    @property
    def total_desconto(self):
        return self.__total_desconto

    @total_desconto.setter
    def total_desconto(self, total_desconto):
        self.__total_desconto = total_desconto

    def calcular_salário_líquido(self):
        return self.salário_bruto + self.total_acréscimo - self.total_desconto
def teste():
    funcionário = Funcionário("João da Silva", 1000.0, 100.0, 50.0)

    print("Nome:", funcionário.nome)
    print("Salário bruto:", funcionário.salário_bruto)
    print("Total de acréscimos:", funcionário.total_acréscimo)
    print("Total de descontos:", funcionário.total_desconto)
    print("Salário líquido:", funcionário.calcular_salário_líquido())


if __name__ == "__main__":
    teste()
