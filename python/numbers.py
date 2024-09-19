def euclideanDistance(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

# Kullanıcıdan ilk noktanın x ve y koordinatlarını ayrı ayrı alma
x1 = float(input("1. noktanın x koordinatını giriniz: "))
y1 = float(input("1. noktanın y koordinatını giriniz: "))

# Kullanıcıdan ikinci noktanın x ve y koordinatlarını ayrı ayrı alma
x2 = float(input("2. noktanın x koordinatını giriniz: "))
y2 = float(input("2. noktanın y koordinatını giriniz: "))

# Noktaları tuple olarak tanımlama
p1 = (x1, y1)
p2 = (x2, y2)

# Mesafenin hesaplanması
distance = euclideanDistance(p1, p2)

# Sonucu yazdırma
print(f"1. nokta {p1} ve 2. nokta {p2} arasındaki Öklid mesafesi: {distance}")
