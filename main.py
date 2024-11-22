from funcoes import *
import os

x = 0
while x == 0:
    limpatela()
    print("=" * 45)
    print("          VOCÊ JA POSSUI UM CADASTRO           ")
    print()
    print("          [1]  -  SIM                             ")
    print("          [2]  -  NÃO                             ")
    print("          [0]  -  SAIR                             ")
    print()
    print("=" * 45)
    escolha = int(input("Qual opção desejar selecionar\n--->  "))

    if escolha == 1:
        limpatela()
        login()

    elif escolha == 2:
        limpatela()
        cadastro()    

    elif escolha == 0:
        print()
        limpatela()
        pausar()
        break

    else:
        print("Opção Inválida!!")
        pausar()
        limpatela()

