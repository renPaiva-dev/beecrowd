def main():
    n = int(input())
    anterior = 0  
    contar = 0

    for i in range(n):
        atual = int(input())
        if atual != anterior:
            contar += 1
            anterior = atual

    print(contar)

main()
