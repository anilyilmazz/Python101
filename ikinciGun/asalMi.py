sayi = int(input("Sayı giriniz : "))

asalKontrol = True
for i in range(2,sayi):
    if sayi%i == 0:
        asalKontrol = False

if (asalKontrol):
    print("Sayı Asal")
else:
    print("Asal Değil")




