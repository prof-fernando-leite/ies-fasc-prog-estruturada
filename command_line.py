from sys import argv as a
from sys import platform as p

if len (a) > 1:
    print(a)
else:
    print("Nenhum argumento encontrado!")

if p == 'darwin':
    print("MAC OS detectado!")
elif p == 'win32':
    print("Windows detectado! Mude urgentemente de OS!")
elif p == 'linux':
    print("Linux detectado!")