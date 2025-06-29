def main():
  n = int(input())
  melhor_preco = 0
  for i in range(n):
    entrada = input().split()
    preco = float(entrada[0])
    gramas = int(entrada[1])
    preco_real = (1000 / gramas) * preco
    if preco_real < melhor_preco or melhor_preco == 0:
      melhor_preco = preco_real
  print(f'{melhor_preco:.2f}')



main()