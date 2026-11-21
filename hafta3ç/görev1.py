import random
ogrenciS=int(input("Kaç kişilik oluşturacaksınız? "))
ogrenciL=[]
for a in range(0,ogrenciS):
    b=a+1
    ogrenciI=input(f"{b}. öğrencinin ismi nedir? ")
    ogrenciL.append(ogrenciI)
    print(ogrenciL)
print(random.choice(ogrenciL)) 