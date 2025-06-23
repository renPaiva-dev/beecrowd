def main():
  positivos = 0
  pos_soma = 0
  for i in range (0, 6, +1):
    num = float(input())
    if num > 0:
      positivos += 1
      pos_soma += num
  print(f'{positivos} valores positivos')
  avg = pos_soma / positivos
  print(f'{avg:.1f}')
  


main()