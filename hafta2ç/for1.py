for a in range(10):
    print("Ankara")
for b in range(10):
    print(b,".sayı")
for c in range(5,30,2):
    print(c)
print(["elma","armut","muz"])
print(*["elma","armut","muz"])
for q in range(5): print("Erdinç")
for x in "suluk":
    print(x)
for k in "selam":
    print(f"{k}",end="-")
for a,b in enumerate(["","Elma","Armut","Muz"],-9): print(a,b)
print([b*3 for b in "goktugg"])

for a in range(1,11):
   for b in range(1,11):
       if a>5:break
       if a==3:continue
       if b==1:print()
       print(f"{a} x {b} = {a*b}")
      
