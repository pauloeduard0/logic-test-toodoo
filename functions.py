from datetime import datetime


def media_idades(i, j, k, x, y):
    x = ((i + j + k + x + y) / 5)
    return x


def distancia_e_gasto(a, b):
    return b / a


def menor_numero(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c


def conversao_c_f(c):
    return 32 + (c / (5 / 9))


def multiplo(x, y):
    if x % y == 0 or y % x == 0:
        print(f'{x} e {y} são múltiplos')
    else:
        print(f'{x} e {y} NÂO são múltiplos')


def partida_fut(a, b):
    hms = '%H:%M:%S'
    duracao = datetime.strptime(b, hms) - datetime.strptime(a, hms)
    print(f'Duração da partida: {duracao}')


def lista_pares(a):
    result = []
    for i in a:
        if i % 2 == 0:
            result.append(f'{i}')
    return result


def primo(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        return True


def tabuada(n):
    i = 0
    while i < 11:
        print(f'{n} * {i} = {n * i}')
        i += 1


def fatorial(n):
    if n <= 1:
        return 1
    else:
        return n * fatorial(n - 1)


def intersecao(a, b):
    result = [n for n in range(1, 9) if n in a and n in b]
    return result


def concatenacao(a, b):
    return a + b


def matriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f'[{m[i][j]}]', end='')
        print()


def palindromo(p):
    tamanho = len(p)
    p = p.lower()
    if tamanho == 0:
        return False
    for i in range(0, tamanho // 2):
        if p[i] != p[tamanho - i - 1]:
            return False
    return True
