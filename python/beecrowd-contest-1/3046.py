def main():
  n = int(input())
  if n < 0 or n > 10000:
    return
  else:
    m = ((n+1)*(n+2))/2
    print(f'{m:.0f}')


main()