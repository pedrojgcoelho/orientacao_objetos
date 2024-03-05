from empresa import Empresa
from aluno import Aluno
from professor import Professor
from turma import Turma
from curso import Curso

if __name__ == "__main__":
    empresa = Empresa()
    empresa.set_id(1)
    empresa.set_codigo(123456)
    empresa.set_razaoSocial("Empresa Exemplo")
    empresa.set_endereco("Rua Exemplo, 123")
    empresa.set_cnpj("12.345.678/9001-23")
    empresa.set_nome("Empresa Exemplo")

    curso = Curso()
    curso.set_nome("Engenharia de software")
    curso.set_descricao("4 anos e 6 meses")

    aluno = Aluno()
    aluno.set_id(1)
    aluno.set_nome("Cliente Exemplo")
    aluno.set_endereco("Rua Cliente, 456")
    aluno.set_email("cliente@example.com")
    aluno.set_matricula("1234567890")

    turma = Turma()
    turma.set_id(101)
    turma.set_descricao(110)
    turma.set_ano("2023")
    turma.set_semestre(2)

    professor = Professor()
    professor.set_nome("Professor exemplo")
    professor.set_matricula("0987654321")
    professor.set_email("professor@gmail.com")
    professor.set_endereco("Juiz de Fora")


    print("Informações da Empresa:")
    print(empresa.gerar_relatorio())

    print("\nInformações do curso:")
    print(f"Curso: {curso.get_nome()}")
    print(f"Curso: {curso.get_descricao()}")

    print("\nInformações do aluno:")
    print(f"Nome do aluno: {aluno.get_nome()}")
    print(f"Endereço do aluno: {aluno.get_endereco()}")
    print(f"Email do aluno: {aluno.get_email()}")
    print(f"Matrícula do aluno: {aluno.get_matricula()}")

    print("\nInformações da Turma:")
    print(f"Descricao da turma: {turma.get_descricao()}")
    print(f"Ano da turma: {turma.get_ano()}")
    print(f"Semestre da turma: {turma.get_semestre()}")

    print("\nInformações do Professor:")
    print(f"Nome do Professor: {professor.get_nome()}")
    print(f"Matrícula do Professor: {professor.get_matricula()}")
    print(f"E-mail do Professor: {professor.get_email()}")
    print(f"Endereço do Professor: {professor.get_endereco()}")
