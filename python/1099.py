def main():
  n = int(input())
  sum = 0
  for i in range(n):
    entrada = input().split()
    a = int(entrada[0])
    b = int(entrada[1])
    if b > a:
      a, b = b, a
    if b == a:
      sum = 0
      print(sum)
    if a == b+1:
      sum = 0
      print(sum)
    for j in range(b+1, a, 1):
      if j % 2 != 0:
        sum += j
      if j == a-1:
        print(sum)
        sum = 0
      else:
        continue





main()