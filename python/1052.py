def main():
  positivos = 0
  numbers = []
  for i in range (0, 6, +1):
    num = float(input())
    if num > 0:
      positivos += 1
  print(f'{positivos} valores positivos')
  


main()