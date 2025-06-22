def main():
    a, b, c, d = map(int, input().split())
    calculo(a,b,c,d)

def calculo(a,b,c,d):
    if b > c and d > a and (c+b > a+b) and c > 0 and d > 0:
        return print("Valores aceitos")
    else:
        return print("Valores nao aceitos")



main()
