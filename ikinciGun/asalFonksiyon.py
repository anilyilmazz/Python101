def asalMi(sayi):
    for i in range(2, sayi):
        if sayi % i == 0:
            return False
    return True


if (asalMi(11)):
    print("Sayı Asal")
else:
    print("Sayı Asal değil.")

