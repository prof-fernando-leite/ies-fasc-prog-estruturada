import os

def boas_vindas():
    print("----------------------------------------")
    print("Bem-vindo ao sistema de cálculo de notas ")

def menu() -> int:
    print("1 - cadastrar nota")
    print("2 - imprimir média")
    print("3 - sair")
    return int(input("Qual operação deseja realizar: "))


def adiciona_nota(soma_notas, numero_de_notas):
    os.system('clear')
    nota = float(input("digite uma nota: "))
    soma_notas += nota
    numero_de_notas += 1
    return soma_notas, numero_de_notas

def calcula_media(soma_notas, numero_de_notas):
    os.system('clear')
    print("média é igual a: ", soma_notas/numero_de_notas)
    soma_notas = 0.0
    numero_de_notas = 0
    return soma_notas, numero_de_notas

def main():
    soma_notas = 0.0
    numero_de_notas = 0
    boas_vindas()
    opcao = menu()
    while opcao != 3:
        if opcao == 1:
            soma_notas, numero_de_notas = adiciona_nota(soma_notas, numero_de_notas)
        if opcao == 2:
            soma_notas, numero_de_notas = calcula_media(soma_notas, numero_de_notas)
        if opcao > 3:
            print("Opção inválida!")
        opcao = menu()
    print("Obrigado por utilizar o sistema de notas!")

if __name__ == "__main__":
    main()