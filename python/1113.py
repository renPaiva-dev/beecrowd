def main():
  while True:
    entrada = input().split()
    a, b = int(entrada[0]), int(entrada[1])
    if a > b:
      print('Decrescente')
    elif a < b:
      print('Crescente')
    else:
      break


main()