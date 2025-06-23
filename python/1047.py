def main():
    entrada = input().split()
    hi = int(entrada[0])
    mi = int(entrada[1])
    hf = int(entrada[2])
    mf = int(entrada[3])

   
    inicio = hi * 60 + mi
    fim = hf * 60 + mf

    if inicio == fim:
        duracao = 24 * 60 
    elif fim > inicio:
        duracao = fim - inicio
    else:
        duracao = (24 * 60 - inicio) + fim

    horas = duracao // 60
    minutos = duracao % 60

    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

main()
