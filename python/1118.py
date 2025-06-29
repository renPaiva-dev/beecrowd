
def main():
  while True:
    v = 0
    s = 0
    while v < 2:
        n = float(input())
        if 0 <= n <= 10:
            s += n
            v += 1
        else:
            print("nota invalida")
    print("media = %.2f" % (s / 2))
    
    x = 0
    while x != 1 and x != 2:
        print("novo calculo (1-sim 2-nao)")
        x = int(input())
    if x == 2:
        break
main()