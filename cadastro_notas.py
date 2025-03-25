print("----------------------------------------")
print("Bem-vindo ao sistema de cálculo de notas ")
print("1 - cadastrar nota")
print("2 - imprimir média")
print("3 - sair")
opcao = int(input("Qual operação deseja realizar: "))
soma_notas = 0.0
numero_de_notas = 0
nota = 0.0
while(opcao !=3):
    if(opcao == 1):
        nota = float(input("digite uma nota: "))
        soma_notas += nota
        numero_de_notas += 1
    elif(opcao == 2):
        print("média é igual a: ", soma_notas/numero_de_notas)
        soma_notas = 0
        numero_de_notas = 0
    else:
        print("opção inválida!")
    print("----------------------------------------")
    print("Bem-vindo ao sistema de cálculo de notas ")
    print("1 - cadastrar nota")
    print("2 - imprimir média")
    print("3 - sair")
    opcao = int(input("Qual operação deseja realizar: "))
print("Obrigado por utilizar o sistema de notas!")

