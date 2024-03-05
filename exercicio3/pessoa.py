class Pessoa:
    def __init__(self, nome, idade, escolaridade):
        self.nome = nome
        self.idade = idade
        self.escolaridade = escolaridade

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_escolaridade(self):
        return self.escolaridade

    def set_nome(self, nome):
        self.nome = nome

    def set_idade(self, idade):
        self.idade = idade

    def set_escolaridade(self, escolaridade):
        self.escolaridade = escolaridade
