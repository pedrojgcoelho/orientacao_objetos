def main():
 
    aluno1 = Aluno("João", 20, "Ensino Médio", "Curso de Matemática", "Matemática")

    print(aluno1.get_nome())
    print(aluno1.get_idade())
    print(aluno1.get_escolaridade())
    print(aluno1.get_tipoEnsino())
    print(aluno1.get_curso())

    professor1 = Professor("Maria", 30, "Ensino Superior", "Curso de Português")

    print(professor1.get_nome())
    print(professor1.get_idade())
    print(professor1.get_escolaridade())
    print(professor1.get_tipoEnsino())

    escola1 = Escola("Escola Municipal de Ensino Fundamental", "Rio de Janeiro", "Rio de Janeiro")

    print(escola1.get_nome())
    print(escola1.get_estado())
    print(escola1.get_cidade())


if __name__ == "__main__":
    main()
