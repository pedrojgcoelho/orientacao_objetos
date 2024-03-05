class Professor(Pessoa):
    def __init__(self, nome, idade, escolaridade, tipoEnsino):
        super().__init__(nome, idade, escolaridade)
        self.tipoEnsino = tipoEnsino

    def get_tipoEnsino(self):
        return self.tipoEnsino

    def set_tipoEnsino(self, tipoEnsino):
        self.tipoEnsino = tipoEnsino