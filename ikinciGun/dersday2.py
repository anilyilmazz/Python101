isim = input("İsim Giriniz : ")
soyisim = input("Soyisim Giriniz : ")
yas = int(input("Yas Giriniz : "))
kilo = float(input("Kilo Giriniz : "))
boy = float(input("Boy Giriniz : "))

bki = kilo / boy ** 2

kisi = [isim, soyisim, yas, kilo, boy, bki]

print(kisi)

if 25 > bki >= 0:
    print(kisi[0], kisi[1], "\nYas : ", kisi[2], "\nBKİ : ", kisi[5], "\nZayıfsınız")
elif 30 >= bki >= 25:
    print(kisi[0], kisi[1], "\nYas : ", kisi[2],
          "\nBKİ : ", kisi[5], "\nKilonuz Orta")
elif 30 < bki:
    print(kisi[0], kisi[1], "\nYas : ", kisi[2],
          "\nBKİ : ", kisi[5], "\nKilolusunuz")
