def main():
    entrada = input().split()
    tamanho = int(entrada[0])
    limite_min = int(entrada[1])
    limite_max = int(entrada[2])
    contador = 0

    numeros_str = input().split()
    numeros = [0] * tamanho 
    for i in range(tamanho):
        
        numeros[i] = int(numeros_str[i]) 

    for i in range(tamanho):
        for j in range(i + 1, tamanho):
            soma = numeros[i] + numeros[j]
            if limite_min <= soma and soma <= limite_max:
                contador += 1

    print(contador)

main()
