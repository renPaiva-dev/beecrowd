def main():
  m = int(input())
  if m < 40 or m > 110:
    return
  a = int(input())
  if a < 1 or a > m:
    return
  b = int(input())
  if b < 1 or b > m or b == a:
    return
  c = m - (a + b)
  if c > b and c > a:
    print(c)
  elif b > a:
    print(b)
  else:
    print(a)
main()