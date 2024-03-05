class Aluno:
  def __init__(self, nome, matricula, notas):
    self.nome = nome
    self.matricula = matricula
    self.notas = notas

  def media(self):
    return sum(self.notas) / len(self.notas)

  def aprovado(self):
    if self.media() >= 6:
      return True
    else:
      return False

  def get_dados(self):
    return (self.nome, self.matricula, self.aprovado())
