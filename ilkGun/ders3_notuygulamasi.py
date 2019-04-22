vizeNotu = int(input("vize : "))
finalNotu = int(input("final : "))

ortalama = (vizeNotu*0.3) + (finalNotu*0.7)

print(ortalama)

if vizeNotu <= 100 and finalNotu <= 100:
    if ortalama <= 100 and ortalama > 80:
        print("AA")
    elif ortalama <= 80 and ortalama >40:
        print("CC")
    elif ortalama <= 40 and ortalama >= 0:
        print("FF")
    elif ortalama > 100:
        print("Girdipiniz sayilari kotrol edin")
    else:
        print("hatali sayi girdiniz tekrar deneyin")