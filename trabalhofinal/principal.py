print('\nSistema de Biblioteca\n')

from usuario import Usuario
from emprestimos import Emprestimo
from livros import Livro
from empresa import Empresa

login = input('Digite o Login (email): ')
senha = input("Digite a Senha: ")

novo_usuario = Usuario()

if novo_usuario.verificar_login(login) == False:
    print('Login inválido!')
    quit()
    
if novo_usuario.verificar_senha(login,senha) == False:
    print ('Senha inválida!')
    quit()

codigo_usuario = novo_usuario.retorna_codigo_usuario(login)
nome_usuario = novo_usuario.retorna_nome_usuario(login)
print (' ')
print (' ')
print('Bem-vindo ', nome_usuario)
print (' ')
print ('Escolha um item do menu de opções:')
print (' ')

menu = 0
while menu != 4:
    menu = int(input(f"DIGITE: 1–Visualizar Empréstimos. 2–Visualizar Livros. 3–Sobre. 4–Sair. : "))
    if menu == 1:
        emprestimos = Emprestimo()
        print (emprestimos.listar_emprestimos(codigo_usuario))
    if menu == 2:
        livros = Livro()
        print (livros.listar_livros())    
    if menu == 3:
        empresa = Empresa()
        print (empresa.exibir_info())
print('')
print('Obrigado. Volte sempre!\n')             