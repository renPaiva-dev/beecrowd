def main():
    entrada = input().split()
    a = float(entrada[0])
    b = float(entrada[1])
    c = float(entrada[2])

    # Ordenação manual em ordem decrescente
    if a >= b and a >= c:
        A = a
        if b >= c:
            B = b
            C = c
        else:
            B = c
            C = b
    elif b >= a and b >= c:
        A = b
        if a >= c:
            B = a
            C = c
        else:
            B = c
            C = a
    else:
        A = c
        if a >= b:
            B = a
            C = b
        else:
            B = b
            C = a

    if A >= B + C:
        print("NAO FORMA TRIANGULO")
    else:
        A2 = A ** 2
        B2_C2 = B ** 2 + C ** 2

        if A2 == B2_C2:
            print("TRIANGULO RETANGULO")
        elif A2 > B2_C2:
            print("TRIANGULO OBTUSANGULO")
        else:
            print("TRIANGULO ACUTANGULO")

        if A == B == C:
            print("TRIANGULO EQUILATERO")
        elif A == B or A == C or B == C:
            print("TRIANGULO ISOSCELES")

main()
