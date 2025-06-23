def main():
  entrada = input().split()

  a = float(entrada[0])
  b = float(entrada[1])

  if b % a == 0 or a % b == 0:
    print('Sao Multiplos')
  else:
    print('Nao sao Multiplos')



main()