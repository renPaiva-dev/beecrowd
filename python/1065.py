def main():
  even = 0
  odd = 0
  positive = 0
  negative = 0
  for i in range (0, 5, +1):
    num = int(input())
    if num == 0:
      positive += 1
      even += 1
      continue
    if num % 2 == 0:
      even += 1
    else:
      odd += 1
    if num > 0:
      positive += 1
    if num < 0:
      negative += 1
  print(f'{even} valores par(es)')
  print(f'{odd} valores impar(es)')
  print(f'{positive} valor(es) positivo(s)')
  print(f'{negative} valor(es) negativo(s)')
  


main()