class Pessoa:
  def __init__(self, nome, peso, altura):
    self.nome = nome
    self.peso = peso
    self.altura = altura

  def calcular_imc(self):
    return self.peso / (self.altura ** 2)

  def obter_classificacao_imc(self):
    imc = self.calcular_imc()

    if imc < 18.5:
      return "Abaixo do peso"
    elif imc < 25:
      return "Dentro do peso ideal"
    elif imc < 30:
      return "Sobrepeso"
    else:
      return "Obeso"

pessoa = Pessoa("João", 70, 1.75)

imc = pessoa.calcular_imc()

classificacao_imc = pessoa.obter_classificacao_imc()

print("Nome:", pessoa.nome)
print("IMC:", imc)
print("Classificação do IMC:", classificacao_imc)
