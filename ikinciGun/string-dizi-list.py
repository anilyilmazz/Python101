deneme = "Hello World!"

print(deneme)

print(deneme[1])

print(deneme[2:5])

print(deneme[2:])

print(deneme * 2)


print("Isim giriniz:", end="")

#isim = input()

#print("Hos Geldin ", isim)




# strip()

deneme = " Hello World! "
print(deneme.strip())

# strip()

deneme = "Hello World!"
print(len(deneme))

# lower() upper()

deneme = "Hello World!"

print(deneme.lower())

print(deneme.upper())

# replace()

deneme = "Hello World!"

print(deneme.replace("H", "J"))

# split()

deneme = "Hello-World!"

print(deneme.split("-"))


#****** LİSTE *********

liste = ["elma", "muz", "armut"]
print(liste)

print(liste[0])
print(liste[1])
print(liste[2])
#print(liste[3])

liste[0] = "Kırmızı Elma"

print(liste[0])


for i in liste:
    print(i)



if "muz" in liste:
    print("listenizde muz vardır")



print(len(liste))


liste.append("çilek")

print(liste)

liste.insert(1,"portakal")

print(liste)


liste.remove("portakal")

print(liste)


del liste[0]

print(liste)


liste.clear()

print(liste)


liste = ["elma", "muz", "armut"]

yeniListe = liste.copy()

print(yeniListe)



# Dictionary -------------


sozluk ={
  "marka": "Ford",
  "model": "Mustang",
  "yil": 1964
}
print(sozluk)

print(sozluk["model"])




