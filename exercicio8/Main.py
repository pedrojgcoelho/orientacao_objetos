class Grupo:
    def __init__(self, sede, pais):
        self.sede = sede
        self.pais = pais
class Empresa:
    def __init__(self, estado, diretor):
        self.estado = estado
        self.diretor = diretor
class Funcionario:
    def __init__(self, alocacao, departamento, cidade, chefia, coordenacao):
        self.alocacao = alocacao
        self.departamento = departamento
        self.cidade = cidade
        self.chefia = chefia
        self.coordenacao = coordenacao

from class import Grupo, Empresa, Funcionario
grupo = Grupo(sede="São Paulo", pais="Brasil")
presidente = grupo.presidente
escolaridade = presidente.escolaridade
print(escolaridade)
from class import Grupo, Empresa, Funcionario
grupo = Grupo(sede="São Paulo", pais="Brasil")
empresa = Empresa(estado="São Paulo", diretor="João da Silva")
funcionario = Funcionario(alocacao=empresa, departamento="Desenvolvimento", cidade="São Paulo", chefia=None, coordenacao=None)
pais = funcionario.empresa.pais
print(pais)
from class import Grupo, Empresa, Funcionario
grupo = Grupo(sede="São Paulo", pais="Brasil")
empresa1 = Empresa(estado="São Paulo", diretor="João da Silva")
empresa2 = Empresa(estado="Rio de Janeiro", diretor="Maria da Silva")
funcionario = Funcionario(alocacao=empresa1, departamento="Desenvolvimento", cidade="São Paulo", chefia=None, coordenacao=empresa2)
estado = funcionario.coordenacao.estado
print(estado)
from class import Grupo, Empresa, Funcionario
grupo = Grupo(sede="São Paulo", pais="Brasil")
empresa = Empresa(estado="São Paulo", diretor="João da Silva")
funcionario1 = Funcionario(alocacao=empresa, departamento="Desenvolvimento", cidade="São Paulo", chefia=None, coordenacao=None)
funcionario2 = Funcionario(alocacao=empresa, departamento="Desenvolvimento", cidade="São Paulo", chefia=funcionario1, coordenacao=None)
escolaridade = funcionario1.escolaridade
print(escolaridade)
from class import Grupo, Empresa, Funcionario
grupo = Grupo(sede="São Paulo", pais="Brasil")
empresa1 = Empresa(estado="São Paulo", diretor="João da Silva")
empresa2 = Empresa(estado="Rio de Janeiro", diretor="Maria da Silva")
funcionario = Funcionario(alocacao=empresa2, departamento="Desenvolvimento", cidade="Rio de Janeiro", chefia=None, coordenacao=None)
nome = funcionario.empresa.diretor.nome
print(nome)
