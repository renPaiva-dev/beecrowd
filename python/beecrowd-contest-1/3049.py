def main():
    b = int(input())
    t = int(input())
    altura = 70
    area_felix = (b + t) * altura // 2
    metade = 160 * 70 // 2 
    if area_felix > metade:
        print(1) 
    elif area_felix < metade:
        print(2) 
    else:
        print(0) 

main()
