# liste işlemleri
# ogrenciler = [."Burak"."Necati"."Yağız"] # hafızadaki adres nokları = index
ogrenciler = ["Burak","Necati","Yağız"]
# liste değerlerine ulaşma
print(ogrenciler) # listenin tamamı
print(ogrenciler[1]) # listenin 1 indexli elemanı
print(ogrenciler[2])
# print(ogrenciler[3]) # olmayan index = index out of range
ogrenciler.append("Nihat")
print(ogrenciler)
ogrenciler.insert(1,"Metehan") # araya eleman ekleme
print(ogrenciler)
ogrenciler.remove("Yağız")
print(ogrenciler)
ogrenciler.pop()
print(ogrenciler)
ogrenciler.pop(1)
print(ogrenciler)
