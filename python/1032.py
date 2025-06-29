def eh_primo(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def gera_primos(qtd):
    primos = []
    n = 2
    while len(primos) < qtd:
        if eh_primo(n):
            primos.append(n)
        n += 1
    return primos

def josephus_dinamico(n):
    primos = gera_primos(n)  # gerar n primos (pra garantir)
    pessoas = list(range(1, n+1))  # lista das pessoas
    pos = 0
    for i in range(n-1):
        passo = primos[i]
        pos = (pos + passo - 1) % len(pessoas)
        pessoas.pop(pos)
    return pessoas[0]

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        print(josephus_dinamico(n))

main()
