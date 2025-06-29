def main():
  while True:
    entrada = input().split()
    m = int(entrada[0])
    n = int(entrada[1])

    if m <= 0 or n <= 0:
        break

    if m > n:
        inicio = n
        fim = m
    else:
        inicio = m
        fim = n

    soma = 0
    for i in range(inicio, fim + 1):
        print(i, end=' ')
        soma += i
    print(f'Sum={soma}')




main()
