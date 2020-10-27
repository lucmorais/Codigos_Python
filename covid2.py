"""
O arquivo em anexo contem as datas da pandemia de covid no distrito federal e o valor acumulado de casos a cada dia.
Você deve ler o arquivo em anexo utilizando a função open do python e criar um programa que receba uma entrada (apenas um input) de duas formas distintas:
A primeira forma é somente um número, representando o mês, o retorno deve ser a quantidade de casos de covid naquele mês (Ex: 05)
A segunda forma é informar mês e dia separados por espaço, o retorno deve ser a quantidade de casos de covid naquele dia. (Ex: 05 28)
"""

arquivo = list(open('covid-bsb.txt', 'r'))

def corrigir_arq(arquivo):
    arquivo = [espaco.strip() for espaco in arquivo]
    arquivo = [valor.replace('-',' ') for valor in arquivo]
    arquivo = [data.split("\t") for data in arquivo]
    novoarq = list(map(lambda dado: ((int(dado[0][0:4]), int(dado[0][6:7]), int(dado[0][8:10])), int(dado[1])), arquivo))
    novoarq = [list(lista) for lista in novoarq]
    return novoarq


novoarq = corrigir_arq(arquivo)

n = int(input('Digite um mes entre 3 e 5: '))

def dados_mes(novoarq):
    global n
    novo = lambda dado: (dado[0][1] == n,dado[1])
    mes = list(map(novo, novoarq))
    percorrer = tuple(valor[1] for valor in mes if valor[0]==True)
    return f'Numero de casos no mês {n}: {sum(percorrer)}\n'


print(dados_mes(novoarq))

n1, n2 = input('Digite um mes e um dia: ').split()
n1, n2 = int(n1), int(n2)

for valor in novoarq:
    if n1 in valor[0] and n2 in valor[0]:
        print(f'Numero de casos na data ({n1}/{n2}): {valor[1]}')