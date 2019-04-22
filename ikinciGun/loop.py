i = 1
while i < 6:
    print(i)
    i += 1

#break continue

i = 1
while i < 9:
    if i == 3:
        i += 1
        continue

    if i == 5:
        break

    print(i)
    i += 1
# for loop
for i in range(10):
    print(i)


#break continue for

for i in range(0,10,2):
    if i == 3:
        break
    print(i)


#-------
for i in range(0, 10, 3):
    if i == 3:
        break
    print(i)


#-------------
print("*****")
print("*****")
print("*****")
print("*****")
print("*****")


for i in range(5):
    for j in range(5):
        print("*", end="")
    print("")

#----------


print("*****")
print("****")
print("***")
print("**")
print("*")
print("------------")



for i in range(5):
    for j in range(5-i,0,-1):
        print("*", end = "")
    print("")


print("*")
print("**")
print("***")
print("****")
print("*****")



for i in range(5):
    for j in range(i+1):
        print("*", end = "")
    print("")










