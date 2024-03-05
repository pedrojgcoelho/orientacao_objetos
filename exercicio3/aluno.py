class Aluno(Pessoa):
    def __init__(self, nome, idade, escolaridade, tipoEnsino, curso):
        super().__init__(nome, idade, escolaridade)
        self.tipoEnsino = tipoEnsino
        self.curso = curso

    def get_tipoEnsino(self):
        return self.tipoEnsino

    def get_curso(self):
        return self.curso

    def set_tipoEnsino(self, tipoEnsino):
        self.tipoEnsino = tipoEnsino

    def set_curso(self, curso):
        self.curso = curso
