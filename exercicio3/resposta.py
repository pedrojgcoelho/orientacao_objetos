def main():
    aluno1 = Aluno("João", 20, "Ensino Médio", "Curso de Matemática", "Matemática")
    print(aluno1.get_escolaridade())
    professor1 = Professor("Maria", 30, "Ensino Superior", "Curso de Português")
    print(professor1.get_escolaridade())
    escola1 = Escola("Escola Municipal de Ensino Fundamental", "Rio de Janeiro", "Rio de Janeiro")
    print(aluno1.get_estado())
    print(professor1.get_cidade())
    print(escola1.get_estado())
    print(professor1.get_tipoEnsino())
    print(aluno1.get_curso().get_coordenador())
    print(professor1.get_escola().get_diretor())
    if aluno1.get_escola().get_coordenador() != None:
        print(aluno1.get_escola().get_coordenador())
    else:
        print("O aluno não tem coordenador")


if __name__ == "__main__":
    main()
