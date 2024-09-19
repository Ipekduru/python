altdeger = int(input("istenilen alt degeri giriniz: "))
ustdeger = int(input("istenilen ust degeri giriniz: "))

for i in range(altdeger, ustdeger + 1):
    print(f"{i} Sayisinin Bolenleri :")

    for j in range(1, i + 1):
        if i % j == 0:
            print(j)

print()