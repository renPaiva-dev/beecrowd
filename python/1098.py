def main():
    i = 0
    j = 1
    cont = 0
    while i <= 2:
        if i == int(i):
            if j == int(j):
                print(f'I={int(i)} J={int(j)}')
            else:
                print(f'I={int(i)} J={j:.1f}')
        else:
            if j == int(j):
                print(f'I={i:.1f} J={int(j)}')
            else:
                print(f'I={i:.1f} J={j:.1f}')

        if cont == 2:
            i += 0.2
            i = round(i, 1)
            j = 1 + i
            cont = 0
        else:
            j += 1
            cont += 1

main()
