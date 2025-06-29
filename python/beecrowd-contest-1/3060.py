def main():
  v = int(input())
  p = int(input())

  base = v // p
  resto = v % p

  for i in range(p):
    if i < resto:
      print(base + 1)
    else:
      print(base)

main()
