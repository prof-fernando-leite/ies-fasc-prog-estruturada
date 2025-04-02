def conta_vogais(s) -> int:
    vogais = 0
    for letra in s:
        if letra in 'aeiou':
            vogais += 1
    return vogais

s = input("insira uma string qualquer:")

numero_de_vogais = conta_vogais(s)

print(f"a palavra ou frase contém {numero_de_vogais} vogais.")
