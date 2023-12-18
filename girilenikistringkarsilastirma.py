str1 = input("Lütfen birinci kelimeyi giriniz: ")
str2 = input("Lütfen ikinci kelimeyi giriniz: ")
len_str2 = len(str2)
print("uzunluk", len_str2)



# if str1 < str2
if len(str1) < len(str2):
    print("str1 daha kısa")

# if str1 == str2
if str1 == str2:
    print("aynı kelimeler")
else:
    print("farklı kelimeler")