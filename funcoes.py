from classes import *
from livros import *
from tabulate import tabulate
from getpass import getpass
import os

contas_cliente = []

conta_biblioteca = ["admin", "admin123"]

def limpatela():
    os.system("cls")

def pausar():
    os.system("pause")
    
def menu():
    limpatela()
    while True:
        limpatela()
        print("=" * 42)
        print("          SISTEMA DE BIBLIOTECA           ")
        print("=" * 42)
        print()
        print(" [1]  -  Emprestar Livros")
        print(" [2]  -  Livros disponíveis no catálogo")
        print(" [0]  -  Voltar ao Login")
        print()
        print("=" * 42)
        escolha = int(input("Escolha uma opção: \n--> "))
        if escolha == 1:
            limpatela()
            emprestar()
        elif escolha == 2:
            limpatela()
            mostrar()
        elif escolha == 0:
            limpatela()
            break
        else:
            limpatela()
            print("\nErro: Tente novamente.")
            pausar()

def emprestar():
    while True:
        limpatela()
        print("=" * 42)
        print("          EMPRESTAR LIVROS           ")
        print("=" * 42)
        print()
        print("          LIVROS")
        print("")
        print("          [1] - Romance")
        print("          [2] - História")
        print("          [3] - Terror")
        print()
        print("          HISTÓRIAS EM QUADRINHOS")
        print()
        print("          [4] - Marvel")
        print("          [5] - DC Comics")
        print("          [6] - Turma da Mônica")
        print()
        print("          [0] - Voltar")
        print()
        print("=" * 42)

        escolha = int(input("\nEscolha um gênero\n--> "))

        if escolha == 1:
            limpatela()
            print("=" * 42)
            print("\tLIVROS DE ROMANCE DISPONÍVEIS:\t")
            print("=" * 42)
            cont = 1
            for i in range(0, len(Romance), 2):
                print(f"{cont}. {Romance[i]} - {Romance[i+1]}")
                cont += 1
            
            titulo = input("\nQual livro deseja emprestar? (NOME)\n--> ")

            if titulo in Romance:
                index = Romance.index(titulo)
                livros_emprestados.append(Romance[index])
                livros_emprestados.append(Romance[index + 1])
                del Romance[index:index + 2]
                print(f'\nO livro "{titulo}" foi emprestado com sucesso.')
                pausar()
            else:
                print(f'\nO livro "{titulo}" não está disponível para empréstimo.')
                pausar()
        
        elif escolha == 2:
            limpatela()
            print("=" * 42)
            print("\tLIVROS DE HISTÓRIA DISPONÍVEIS:\t")
            print("=" * 42)
            cont = 1
            for i in range(0, len(História), 2):
                print(f"{cont}. {História[i]} - {História[i+1]}")
                cont += 1
            
            titulo = input("\nQual livro deseja emprestar? (NOME)\n--> ")

            if titulo in História:
                index = História.index(titulo)
                livros_emprestados.append(História[index])
                livros_emprestados.append(História[index + 1])
                del História[index:index + 2]
                print(f'\nO livro "{titulo}" foi emprestado com sucesso.')
                pausar()
            else:
                print(f'\nO livro "{titulo}" não está disponível para empréstimo.')
                pausar()

        elif escolha == 3:
            limpatela()
            print("=" * 42)
            print("\tLIVROS DE TERROR DISPONÍVEIS:\t")
            print("=" * 42)
            cont = 1
            for i in range(0, len(Terror), 2):
                print(f"{cont}. {Terror[i]} - {Terror[i+1]}")
                cont += 1
            
            titulo = input("\nQual livro deseja emprestar? (NOME)\n--> ")

            if titulo in Terror:
                index = Terror.index(titulo)
                livros_emprestados.append(Terror[index])
                livros_emprestados.append(Terror[index + 1])
                del Terror[index:index + 2]
                print(f'\nO livro "{titulo}" foi emprestado com sucesso.')
                pausar()
            else:
                print(f'\nO livro "{titulo}" não está disponível para empréstimo.')
                pausar()

        elif escolha == 4:
            limpatela()
            print("=" * 42)
            print("\tHQS DA MARVEL DISPONÍVEIS:\t")
            print("=" * 42)
            cont = 1
            for i in range(0, len(Marvel), 2):
                print(f"{cont}. {Marvel[i]} - {Marvel[i+1]}")
                cont += 1
            
            titulo = input("\nQual HQ deseja emprestar? (NOME)\n--> ")

            if titulo in Marvel:
                index = Marvel.index(titulo)
                livros_emprestados.append(Marvel[index])
                livros_emprestados.append(Marvel[index + 1])
                del Marvel[index:index + 2]
                print(f'\nA HQ "{titulo}" foi emprestada com sucesso.')
                pausar()
            else:
                print(f'\nA HQ "{titulo}" não está disponível para empréstimo.')
                pausar()

        elif escolha == 5:
            limpatela()
            print("=" * 42)
            print("\tHQS DA DC COMICS DISPONÍVEIS:\t")
            print("=" * 42)
            cont = 1
            for i in range(0, len(DC_Comics), 2):
                print(f"{cont}. {DC_Comics[i]} - {DC_Comics[i+1]}")
                cont += 1
            
            titulo = input("\nQual HQ deseja emprestar? (NOME)\n--> ")

            if titulo in DC_Comics:
                index = DC_Comics.index(titulo)
                livros_emprestados.append(DC_Comics[index])
                livros_emprestados.append(DC_Comics[index + 1])
                del DC_Comics[index:index + 2]
                print(f'\nA HQ "{titulo}" foi emprestada com sucesso.')
                pausar()
            else:
                print(f'\nA HQ "{titulo}" não está disponível para empréstimo.')
                pausar()

        elif escolha == 6:
            limpatela()
            print("=" * 42)
            print("\tHQS DA TURMA DA MÔNICA DISPONÍVEIS:\t")
            print("=" * 42)
            cont = 1
            for i in range(0, len(Turma_da_Mônica), 2):
                print(f"{cont}. {Turma_da_Mônica[i]} - {Turma_da_Mônica[i+1]}")
                cont += 1
            
            titulo = input("\nQual HQ deseja emprestar? (NOME)\n--> ")

            if titulo in Turma_da_Mônica:
                index = Turma_da_Mônica.index(titulo)
                livros_emprestados.append(Turma_da_Mônica[index])
                livros_emprestados.append(Turma_da_Mônica[index + 1])
                del Turma_da_Mônica[index:index + 2]
                print(f'\nA HQ "{titulo}" foi emprestada com sucesso.')
                pausar()
            else:
                print(f'\nA HQ "{titulo}" não está disponível para empréstimo.')
                pausar()

        elif escolha == 0:
            limpatela()
            pausar()
            break

        else:
            limpatela()
            print('Opção Inválida. Tente novamente.')
            pausar()

def mostrar():
    limpatela()
    print("=" * 42)
    print("          LIVROS E HQS DISPONIVEIS           ")
    print("=" * 42)
    cont = 1
    print("\nLIVROS\n")
    for i in zip(Romance, História, Terror):
        print(f"  [{cont}]  -  {i}\n")
        cont += 1
    x = 1
    print("\nHISTORIA EM QUADRINHOS\n")
    for y in zip(Marvel, DC_Comics, Turma_da_Mônica):
        print(f"  [{x}]  -  {y}\n")
        x += 1

    pausar()   


def menu_admin():
    limpatela()
    while True:
        limpatela()
        print("=" * 42)
        print("          SISTEMA DE ADMIN           ")
        print("=" * 42)
        print()
        print(" [1]  -  Visualizar Clientes")
        print(" [2]  -  Visualizar Empréstimos")
        print(" [0]  -  Voltar ao Login")
        print()
        print("=" * 42)
        escolha = int(input("Escolha uma opção: \n--> "))

        if escolha == 1:
            limpatela()
            clientes()
        elif escolha == 2:
            limpatela()
            livro_emprestado()
        elif escolha == 0:
            limpatela()
            break
        else:
            limpatela()
            print("\nErro: Tente novamente.")
            pausar()

def clientes():
    limpatela()
    print("=" * 42)
    print("          VISUALIZAR CLIENTES           ")
    print("=" * 42)
    
    headers = ["ID", "USUÁRIO", "EMAIL", "NOME", "SENHA"]
    table = []
    
    for idx, conta in enumerate(contas_cliente, start=1):
        table.append([
            f"[{idx}]",
            conta.getUser(),
            conta.getEmail(),
            conta.getNome(),
            conta.getSenha()
        ])
    
    print()
    print(tabulate(table, headers=headers, tablefmt="plain"))
    pausar()
        
def livro_emprestado():
    limpatela()
    print("=" * 42)
    print("          VISUALIZAR EMPRÉSTIMOS           ")
    print("=" * 42)
    cont = 1
    for i in range(0, len(livros_emprestados), 2):
        print(f"{cont}. {livros_emprestados[i]} - {livros_emprestados[i+1]}")
        cont += 1
        pausar()

def login():
    limpatela()
    print("=" * 42)
    print("          TELA DE LOGIN          ")
    print("=" * 42)
    print()

    nome = input("- Insira seu usuário\n--> ")
    senha = getpass("\n- Insira sua senha\n--> ")
   
    if nome == conta_biblioteca[0] and senha == conta_biblioteca[1]:
        limpatela()
        print("Usuário admin acessado!")
        print()
        pausar()
        menu_admin()
        return

    for conta in contas_cliente:
        if nome == conta.getUser() and senha == conta.getSenha():
            limpatela()
            print("Senha correta!")
            print()
            menu()
            return

    limpatela()
    print("\nConta não identificada, convém rever seus dados ou criar uma conta!")
    pausar()

def cadastro():
    limpatela()
    print("=" * 40)
    print("          TELA DE CADASTRO           ")
    print("=" * 40)
    print()
    usuario = input("- Insira seu usuário\n--> ")
    email = input("\n- Insira seu email\n--> ")
    nome = input("\n- Insira seu nome\n--> ")
    senha = getpass("\n- Insira sua senha\n--> ")
    csenha = getpass("- Insira sua senha novamente\n--> ")
    
    if senha == csenha:
        cadastro = Clientes(nome, email, usuario, senha)
        limpatela()
        contas_cliente.append(cadastro)
        print("Conta cadastrada com sucesso!")
        x = 0 
        pausar() 
    
    else:
        limpatela()
        print("\nErro: As senhas não coincidem.")
        pausar()