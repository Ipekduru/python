sayi1=int (input("Lütfen birinci sayiyi giriniz"))
sayi2=int (input("lütfen ikinci sayiyi giriniz"))
sayi3=int (input("lütfen üçüncü sayiyi giriniz"))

enB =0
if (sayi1>=sayi2) and (sayi1>sayi3):
    enB = sayi1
elif (sayi2>=sayi1) and (sayi2>sayi3):
    enB =sayi2
else:
    enB=sayi3
    print(enB)