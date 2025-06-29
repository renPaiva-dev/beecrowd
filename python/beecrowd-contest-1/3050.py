def main():
    N = int(input())
    andares = input().split()
    
    valor = int(andares[0])
    esquerda = valor
    direita = valor
    distancia = 0

    i = 1
    while i < N:
        valor = int(andares[i])
        
        d1 = valor + i + esquerda
        d2 = valor - i + direita

        if d1 > distancia:
            distancia = d1
        if d2 > distancia:
            distancia = d2

        if valor - i > esquerda:
            esquerda = valor - i
        if valor + i > direita:
            direita = valor + i

        i += 1

    print(distancia)

main()
