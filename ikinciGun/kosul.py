# girilen 2 sayıdan büyüğünü bulma

sayi1 = int(input())
sayi2 = int(input())

if(sayi1 > sayi2):
    print(sayi1, " Büyüktür ", sayi2)
if(sayi1 < sayi2):
    print(sayi2, " Büyüktür ", sayi1)
else:
    print("Sayılar Eşittir")

# ders notunun harf karşılığını bulma

print("Ders Notunu giriniz:")
dersNotu = int(input())
if(dersNotu <= 100 & dersNotu >=90 ):
    print("AA")
elif(dersNotu <= 99 & dersNotu >= 70):
    print("BB")
elif(dersNotu <= 69 & dersNotu >= 40):
    print("CC")
elif(dersNotu <= 39 & dersNotu >= 0):
    print("FF")
