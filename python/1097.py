def main():
  i = 1
  j = 7
  b = 7
  cont = 0
  while i <= 9:
    print(f'I={i} J={j}')
    if cont == 2:
      i += 2
      j = b + 2
      b = b + 2
      cont = 0
    else: 
      cont += 1
      j -= 1
   




main()