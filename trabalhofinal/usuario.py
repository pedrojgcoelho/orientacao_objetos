class Usuario:
    #def __init__(self, login, senha):
    #    self.login = login
    #    self.senha = senha

    def verificar_login(self, login):
        login_ok = False
        arquivo = "usuarios.txt"
        with open(arquivo, "r") as f:
            linha: str
            for linha in f:
                codigo, nome, tipo, login_usuario, senha_usuario = linha.split(",")
                login_usuario = login_usuario.strip()
                if login == login_usuario:
                    login_ok = True
                    break
            if login_ok:
                return True
            else:
                return False

    def verificar_senha(self, login, senha):
        senha_ok = False
        arquivo = "usuarios.txt"
        with open(arquivo, "r") as f:
            linha: str
            for linha in f:
                codigo, nome, tipo, login_usuario, senha_usuario = linha.split(",")
                login_usuario = login_usuario.strip()
                senha_usuario = senha_usuario.strip()
                if login == login_usuario and senha == senha_usuario:
                    senha_ok = True
                    break
            if senha_ok:
                return True
            else:
                return False

    def retorna_codigo_usuario(self,login):
        usuario_ok = False
        arquivo = "usuarios.txt"
        with open(arquivo, "r") as f:
            linha: str
            for linha in f:
                codigo, nome, tipo, login_usuario, senha_usuario = linha.split(",")
                codigo = codigo.strip()
                login_usuario = login_usuario.strip()
                if login == login_usuario: 
                    usuario_ok = True
                    codigo_usuario = codigo
                    break
        if usuario_ok:
            return codigo_usuario
        else:
            return 'Usuário não encontrado'

    def retorna_nome_usuario(self,login):
        usuario_ok = False
        arquivo = "usuarios.txt"
        with open(arquivo, "r") as f:
            linha: str
            for linha in f:
                codigo, nome, tipo, login_usuario, senha_usuario = linha.split(",")
                nome = nome.strip()
                login_usuario = login_usuario.strip()
                if login == login_usuario: 
                    usuario_ok = True
                    nome_usuario = nome
                    break
        if usuario_ok:
            return nome_usuario
        else:
            return 'Usuário não encontrado'