def main():
    entrada = input().split()
    inicio = int(entrada[0])
    fim = int(entrada[1])

    if inicio == fim:
        duracao = 24
    elif inicio < fim:
        duracao = fim - inicio
    else:
        duracao = (24 - inicio) + fim

    print(f"O JOGO DUROU {duracao} HORA(S)")

main()
