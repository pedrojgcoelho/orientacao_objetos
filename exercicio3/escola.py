class Escola:
    def __init__(self, nome, estado, cidade):
        self.nome = nome
        self.estado = estado
        self.cidade = cidade

    def get_nome(self):
        return self.nome

    def get_estado(self):
        return self.estado

    def get_cidade(self):
        return self.cidade

    def set_nome(self, nome):
        self.nome = nome

    def set_estado(self, estado):
        self.estado = estado

    def set_cidade(self, cidade):
        self.cidade = cidade