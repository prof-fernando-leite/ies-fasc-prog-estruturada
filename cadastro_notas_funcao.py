import os

soma_notas = 0.0
numero_de_notas = 0

def boas_vindas():
    print("----------------------------------------")
    print("Bem-vindo ao sistema de cálculo de notas ")

def menu() -> int:
    print("1 - cadastrar nota")
    print("2 - imprimir média")
    print("3 - sair")
    opcao = int(input("Qual operação deseja realizar: "))
    return opcao

def adiciona_nota():
    global soma_notas, numero_de_notas    
    os.system('clear')
    nota = float(input("digite uma nota: "))
    soma_notas += nota
    numero_de_notas += 1

def calcula_media():
    global soma_notas, numero_de_notas
    os.system('clear')
    print("média é igual a: ", soma_notas/numero_de_notas)
    soma_notas = 0
    numero_de_notas = 0

def seleciona_funcao(seletor):
    if(seletor == 1):
        adiciona_nota() 
    elif(seletor == 2):
        calcula_media()
    else:
        print("opção inválida!")

def controla_menu():
    boas_vindas()
    opcao = menu()
    while(opcao !=3):
        seleciona_funcao(opcao)
        opcao = menu()

def main():
    os.system('clear')
    controla_menu()
    print("Obrigado por utilizar o sistema de notas!")


main()