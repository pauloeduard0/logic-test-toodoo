import functions as f


class Exercice:
    print('1 - Entre com as idades')
    i = float(input("I = "))
    j = float(input("J = "))
    k = float(input("K = "))
    x = float(input("X = "))
    y = float(input("Y = "))
    result_1 = f.media_idades(i, j, k, x, y)
    print(f'Média das idades: {round(result_1, 3)}')
    print("--------------------------")

    print("2 - Entre com distância e combustível gasto")
    a = float(input("A = "))
    b = float(input("B = "))
    result_2 = f.distancia_e_gasto(a, b)
    print(f'Consumo médio: {result_2}')
    print("--------------------------")

    print("3 - Entre com três números ")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    result_3 = f.menor_numero(a, b, c)
    print(f'Menor número: {result_3}')
    print("--------------------------")

    print("4 - Entre com graus celsius")
    c = float(input("ºC = "))
    result_4 = f.conversao_c_f(c)
    print(f'{result_4}°F')
    print("--------------------------")

    print("5 - Entre com dois números")
    x = float(input("X = "))
    y = float(input("Y = "))
    f.multiplo(x, y)
    print("--------------------------")

    print("6 - Entre com horario de inicio e fim no formato 00:00:00")
    a = str(input())
    b = str(input())
    f.partida_fut(a, b)
    print("--------------------------")

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f'7 - lista = {lista}')
    result_7 = f.lista_pares(lista)
    print(f'Lista com pares {result_7}')
    print("--------------------------")

    print("8 - Entre com um número")
    n = float(input("Número: "))
    result_8 = f.primo(n)
    print(f'É Primo? {result_8}')
    print("--------------------------")

    print("9 - Entre com um número")
    n = int(input("Número: "))
    result_9 = f.tabuada(n)
    print("--------------------------")

    print("10 - Entre com um número")
    n = float(input("Número: "))
    result_10 = f.fatorial(n)
    print(f'Fatorial de {n} é {result_10}')
    print("--------------------------")

    A = [1, 2, 3, 4]
    B = [1, 2, 5, 8]
    print(f'11 - Dada listas A = {A} e B = {B}')
    result_11 = f.intersecao(A, B)
    print(f'Intersecção nas listas: {result_11}')
    print("--------------------------")

    A = [1, 2, 3, 4]
    B = [1, 2, 5, 8]
    print(f'12 - Dada listas A = {A} e B = {B}')
    result_12 = f.concatenacao(A, B)
    print(f'Concatenação das listas: {result_12}')
    print("--------------------------")

    print("13 - Entre com valores para matriz 3x3")
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(0, 3):
        for j in range(0, 3):
            m[i][j] = int(input(f'Valores para [{i}, {j}]: '))
    f.matriz(m)
    print("--------------------------")

    print("14 - Entre com uma palavra")
    poli = str(input("Palavra: "))
    result_14 = f.palindromo(poli)
    print(f'É Políndromo: {result_14}')
    print("--------------------------")

