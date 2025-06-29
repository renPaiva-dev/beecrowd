def fib_mod(n, m):
    if n == 0:
        return (0, 1)
    a, b = fib_mod(n // 2, m)
    c = (a * ((2 * b - a) % m)) % m
    d = (a * a + b * b) % m
    if n % 2 == 0:
        return (c, d)
    else:
        return (d, (c + d) % m)

def main():
    case_num = 1
    while True:
        entrada = input().strip()
        if entrada == '':
            break
        n_str, b_str = entrada.split()
        n = int(n_str)
        b = int(b_str)
        if n == 0 and b == 0:
            break

        fib_n1_mod = fib_mod(n+1, b)[0]
        resultado = (2 * fib_n1_mod - 1) % b

        print(f"Case {case_num}: {n} {b} {resultado}")
        case_num += 1


main()
