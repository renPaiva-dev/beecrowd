def main():
  entrada = input().split()
  x = int(entrada[0])
  y = int(entrada[1])
  if x == 1:
    z = y * 4
    print(f"Total: R$ {z:.2f}")
  if x == 2:
    z = y * 4.5
    print(f"Total: R$ {z:.2f}")
  if x == 3:
    z = y * 5
    print(f"Total: R$ {z:.2f}")
  if x == 4:
    z = y * 2
    print(f"Total: R$ {z:.2f}")
  if x == 5:
    z = y * 1.5
    print(f"Total: R$ {z:.2f}")



main()
