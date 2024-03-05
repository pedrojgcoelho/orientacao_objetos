# empresa.py

class Empresa:
    def set_id(self, id):
        self.__id = id

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_razaoSocial(self, razaoSocial):
        self.__razaoSocial = razaoSocial

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def set_cnpj(self, cnpj):
        self.__cnpj = cnpj

    def set_nome(self, nome):
        self.__nome = nome

    def get_id(self):
        return self.__id

    def get_codigo(self):
        return self.__codigo

    def get_razaoSocial(self):
        return self.__razaoSocial

    def get_endereco(self):
        return self.__endereco

    def get_cnpj(self):
        return self.__cnpj

    def get_nome(self):
        return self.__nome

    def gerar_relatorio(self):
        relatorio = f"Empresa: {self.get_razaoSocial()}"
        relatorio += f"\nID: {self.get_id()}"
        relatorio += f"\nCódigo: {self.get_codigo()}"
        relatorio += f"\nCNPJ: {self.get_cnpj()}"
        relatorio += f"\nEndereço: {self.get_endereco()}"
        relatorio += f"\nNome: {self.get_nome()}"
        return relatorio

    def adicionar_produto(self, produto):
        self.__produtos.append(produto)

    def remover_produto(self, produto):
        self.__produtos.remove(produto)

    def listar_produtos(self):
        return self.__produtos