"""
retiro o ultimo elemento da lista com o método 'pop', e faço uma verificação com cada elemento que restou da lista e
adicionei um contador para saber a quantidade de vezes que essa verificação for verdadeira
"""

n, menor, maior = input().split()
numeros = input().split()
numeros = [int(valor) for valor in numeros]
cont = 0

while len(numeros) != 0:
    ret = numeros.pop()
    for num in numeros:
        if (ret + num) >= int(menor) and (ret + num) <= int(maior):
            cont += 1

print(cont)