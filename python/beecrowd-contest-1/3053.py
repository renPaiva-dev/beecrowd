def main():
    n = int(input())
    posicao = input().lower()

    if posicao == 'a':
        posicao_bolinha = 0
    elif posicao == 'b':
        posicao_bolinha = 1
    else:
        posicao_bolinha = 2

    for i in range(n):
        movimento = int(input())

        if movimento == 1:
            if posicao_bolinha == 0:
                posicao_bolinha = 1
            elif posicao_bolinha == 1:
                posicao_bolinha = 0
        elif movimento == 2:
            if posicao_bolinha == 1:
                posicao_bolinha = 2
            elif posicao_bolinha == 2:
                posicao_bolinha = 1
        elif movimento == 3:
            if posicao_bolinha == 2:
                posicao_bolinha = 0
            elif posicao_bolinha == 0:
                posicao_bolinha = 2

    print(['A', 'B', 'C'][posicao_bolinha])

main()
