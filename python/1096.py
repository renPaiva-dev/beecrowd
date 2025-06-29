def main():
  i = 1
  j = 7
  while i <= 9:
    print(f'I={i} J={j}')
    if j == 5:
      i = i + 2
      j = 7
    else:
      j -= 1


main()