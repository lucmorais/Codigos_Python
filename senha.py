"""
Escreva um programa que receba uma senha apenas com caracteres do alfabeto ou espaço.
Utilize o Calumma-12 para transformar os 12 primeiros caracteres do texto da senha para números.

Calumma-12: 0 = a, k, u, G, Q;
            1 = b, l, v, I, S;
            2 = c, m, w, E, O, Y;
            3 = d, n, x, F, P, Z;
            4 = e, o, y, J, T;
            5 = f, p, z, D, N, X;
            6 = g, q, A, K, U;
            7 = h, r, C, M, W;
            8 = i, s, B, L, V;
            9 = j, t, H, R;

Exemplo:
- Entrada:

            3
            ProGRAmador
            IESB nota cinco no MEC
            o nome calumma vem de uma especie de camaleao

- Saída:

            00942098561
            121834902832
            434242010220
"""

n = int(input("Digite a quantidade de senhas: "))

senhas = [input("Digite a senha: ").replace(" ", "") for _ in range(n)]

calumma = [
    (0, ('a', 'k', 'u', 'G', 'Q')),
    (1, ('b', 'l', 'v', 'I', 'S')),
    (2, ('c', 'm', 'w', 'E', 'O', 'Y')),
    (3, ('d', 'n', 'x', 'F', 'P', 'Z')),
    (4, ('e', 'o', 'y', 'J', 'T')),
    (5, ('f', 'p', 'z', 'D', 'N', 'X')),
    (6, ('g', 'q', 'A', 'K', 'U')),
    (7, ('h', 'r', 'C', 'M', 'W')),
    (8, ('i', 's', 'B', 'L', 'V')),
    (9, ('j', 't', 'H', 'R'))
]

def diminuir_string(senhas):
    ch = 12
    temp = []
    for key in senhas:
        if len(key) > ch:
            temp.append(key[:ch])
        else:
            temp.append(key)
    return temp


novas_senhas = diminuir_string(senhas)

for s in novas_senhas:
    for l in s:
        for elem in calumma:
            for chave in elem[1]:
                if l == chave:
                    print(elem[0], end='')
    print(end='\n')
