def main():
  entrada = input().split()
  l = int(entrada[0])
  c = int(entrada[1])
  vect = []
  for i in range(c):
    vect[i] = int(input())
    for j in range(l):
