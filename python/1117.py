def main():
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

main()