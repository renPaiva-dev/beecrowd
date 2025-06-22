def main():
  valores = input().split()

  a = float(valores[0])
  b = float(valores[1])
  c = float(valores[2])

  baskara(a,b,c)

def baskara(a,b,c):
  if a <= 0 or b <= 0 or c <= 0:
    return print("Impossivel calcular")
  delta = (b*b) - 4*a*c
  if delta <= 0:
    return print("Impossivel calcular")
  r1 = (-b + delta**0.5) / (2*a)
  r2 = (-b - delta**0.5) / (2*a)
  print(f"R1 = {r1:.5f}")
  print(f"R2 = {r2:.5f}")

main()
