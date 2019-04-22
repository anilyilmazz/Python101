def ebob(sayi1,sayi2):
    kucuk = sayi1
    if sayi2 < sayi1:
        kucuk = sayi2
    bolen = 1
    for i in range(1, kucuk+1):
        if sayi1 % i == 0 and sayi2 % i == 0:
            bolen = i
    print(bolen)


ebob(10, 20)
