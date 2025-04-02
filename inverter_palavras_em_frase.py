# Dada uma frase, inverta cada palavra individualmente, mas mantenha a ordem das palavras na frase.
def inverter_palavras(frase):
    return ' '.join(palavra[::-1] for palavra in frase.split())

s = input("Digite uma frase: ")
print(inverter_palavras(s))