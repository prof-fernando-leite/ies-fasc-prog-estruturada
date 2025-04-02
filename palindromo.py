# Funcionamento do [::-1]:
# word[start:end:step] é a sintaxe geral de slicing em Python.
# Quando usamos [::-1], estamos dizendo:
# start: Não especificado (pega toda a string).
# end: Não especificado (vai até o final).
# step: -1 (passo negativo, percorre a string de trás para frente).

def is_palindrome(word):
    return word == word[::-1]

s = input("Digite uma palavra ou frase: ")
if is_palindrome(s):
    print("A frase ou palavra digitada é um palíndromo")
else:
    print("A frase ou palavra digitada não é um palíndromo")