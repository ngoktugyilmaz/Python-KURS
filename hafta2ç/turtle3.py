"""
import turtle, random

def sekilCiz(kenarsayisi=4, buyukluk=100, renk="red", yerx=0, yery=0):
    turtle.speed(10)
    turtle.color(renk)
    turtle.penup()
    turtle.goto(yerx,yery)
    turtle.pendown()
    for a in range(kenarsayisi):
        turtle.forward(100)
        turtle.right(360/kenarsayisi)

renkler=["red","green","blue","yellow"]

for a in range(10):
    k = random.randint(3,7)
    b = random.randint(50,200)
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    sekilCiz(k,b,random.choice(renkler),x,y)
"""


"""
import turtle

# Turtle oluşturma
t = turtle.Turtle()
s = turtle.Screen()

# Ekran ve kalem ayarları
s.bgcolor("black")
t.pencolor("red")
t.speed(100000)

a = 0
b = 0

t.penup()
t.goto(0, 200)
t.pendown()

while True:
    t.forward(a)
    t.right(b)
    a += 3
    b += 1

    if b == 210:
        break

t.hideturtle()
turtle.done()
input()

"""






"""
import turtle

t = turtle.Turtle()
screen = turtle.Screen()

screen.bgcolor("black")
t.speed(10000000)
t.pensize(2)

colours = ["red", "purple", "blue", "green", "orange", "yellow"]

for x in range(360):
    t.pencolor(colours[x % 6])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)

turtle.done()
input()
"""


"""
import turtle
import random
import math

# --- EKRAN AYARLARI ---
ekran = turtle.Screen()
ekran.setup(width=800, height=600)
ekran.bgcolor("#0b0c10")
ekran.title("Galaktik Savunma - Büyük Turtle Projesi")
ekran.tracer(0)

# --- OYUN DEĞİŞKENLERİ ---
skor = 0
seviye = 1
can = 3
oyun_bitti = False

# --- SINIFLAR (OOP) ---
class OyunNesnesi(turtle.Turtle):
    def __init__(self, sekil, renk, x, y):
        super().__init__()
        self.speed(0)
        self.shape(sekil)
        self.color(renk)
        self.penup()
        self.goto(x, y)

class Oyuncu(OyunNesnesi):
    def __init__(self):
        super().__init__("triangle", "#66fcf1", 0, -250)
        self.setheading(90)
        self.hiz = 25

    def sola_git(self):
        if self.xcor() > -360:
            self.setx(self.xcor() - self.hiz)

    def saga_git(self):
        if self.xcor() < 360:
            self.setx(self.xcor() + self.hiz)

class Mermi(OyunNesnesi):
    def __init__(self):
        super().__init__("square", "#f39c12", 0, -400)
        self.shapesize(stretch_wid=0.2, stretch_len=0.8)
        self.setheading(90)
        self.hiz = 15
        self.durum = "hazir"  # hazir veya ateslendi

    def atesle(self, x, y):
        if self.durum == "hazir":
            self.durum = "ateslendi"
            self.goto(x, y + 15)
            self.showturtle()

    def hareket_et(self):
        if self.durum == "ateslendi":
            self.sety(self.ycor() + self.hiz)
            if self.ycor() > 290:
                self.sifirla()

    def sifirla(self):
        self.hideturtle()
        self.durum = "hazir"
        self.goto(0, -400)

class Dusman(OyunNesnesi):
    def __init__(self):
        x = random.randint(-350, 350)
        y = random.randint(150, 280)
        super().__init__("circle", "#e74c3c", x, y)
        self.hiz = random.uniform(1.0, 2.5)

    def hareket_et(self, mevcut_seviye):
        self.sety(self.ycor() - (self.hiz + (mevcut_seviye * 0.3)))
        if self.ycor() < -280:
            self.yeniden_dog()
            return True  # Alt sınıra ulaştı
        return False

    def yeniden_dog(self):
        self.goto(random.randint(-350, 350), random.randint(200, 320))

# --- BİLGİ PANELİ (HUD) ---
kalem = turtle.Turtle()
kalem.speed(0)
kalem.color("#c5c6c7")
kalem.penup()
kalem.hideturtle()
kalem.goto(-380, 260)

def paneli_guncelle():
    kalem.clear()
    kalem.write(f"Skor: {skor}   |   Seviye: {seviye}   |   Can: {'❤️' * can}", 
                align="left", font=("Courier", 14, "bold"))

def oyun_bitti_ekrani():
    kalem.goto(0, 0)
    kalem.color("#e74c3c")
    kalem.write("OYUN BİTTİ", align="center", font=("Courier", 36, "bold"))
    kalem.goto(0, -40)
    kalem.color("#ffffff")
    kalem.write(f"Toplam Skorun: {skor}", align="center", font=("Courier", 18, "normal"))

# --- ÇARPIŞMA KONTROLÜ ---
def carpisma_var_mi(nesne1, nesne2, mesafe=25):
    uzaklik = math.hypot(nesne1.xcor() - nesne2.xcor(), nesne1.ycor() - nesne2.ycor())
    return uzaklik < mesafe

# --- NESNELERİ OLUŞTURMA ---
oyuncu = Oyuncu()
mermi = Mermi()
mermi.hideturtle()
dusmanlar = [Dusman() for _ in range(6)]

# --- KLAVYE KONTROLLERİ ---
ekran.listen()
ekran.onkeypress(oyuncu.sola_git, "Left")
ekran.onkeypress(oyuncu.saga_git, "Right")
ekran.onkeypress(lambda: mermi.atesle(oyuncu.xcor(), oyuncu.ycor()), "space")

paneli_guncelle()

# --- ANA OYUN DÖNGÜSÜ ---
while not oyun_bitti:
    ekran.update()
    mermi.hareket_et()

    for dusman in dusmanlar:
        alt_sinira_ulasti = dusman.hareket_et(seviye)
        
        if alt_sinira_ulasti:
            can -= 1
            paneli_guncelle()
            if can <= 0:
                oyun_bitti = True

        # Mermi - Düşman Çarpışması
        if mermi.durum == "ateslendi" and carpisma_var_mi(mermi, dusman):
            mermi.sifirla()
            dusman.yeniden_dog()
            skor += 10
            if skor % 100 == 0:
                seviye += 1
            paneli_guncelle()

        # Oyuncu - Düşman Çarpışması
        if carpisma_var_mi(oyuncu, dusman, 30):
            dusman.yeniden_dog()
            can -= 1
            paneli_guncelle()
            if can <= 0:
                oyun_bitti = True

oyun_bitti_ekrani()
ekran.mainloop()
"""
import turtle

# Ekran ayarları
ekran = turtle.Screen()
ekran.title("Python Turtle - Minecraft Creeper")
ekran.bgcolor("#4CAF50")  # Creeper yeşili arka plan

kalem = turtle.Turtle()
kalem.speed(0)
kalem.penup()
kalem.hideturtle()


# Kare (piksel) çizme fonksiyonu
def piksel_ciz(x, y, boyut, renk):
  kalem.goto(x, y)
  kalem.fillcolor(renk)
  kalem.begin_fill()
  for _ in range(4):
    kalem.forward(boyut)
    kalem.right(90)
  kalem.end_fill()


boyut = 40  # Her bir pikselin boyutu

# Creeper yüzünün siyah piksel koordinatları (8x8 ızgara mantığı)
siyah_pikseller = [
    # Sol göz
    (-120, 120),
    (-80, 120),
    (-120, 80),
    (-80, 80),
    # Sağ göz
    (40, 120),
    (80, 120),
    (40, 80),
    (80, 80),
    # Burun / Ağız orta kısmı
    (-40, 40),
    (0, 40),
    (-80, 0),
    (-40, 0),
    (0, 0),
    (40, 0),
    (-80, -40),
    (-40, -40),
    (0, -40),
    (40, -40),
    # Ağız alt yanları
    (-80, -80),
    (40, -80),
]

# Yüzü çiz
for x, y in siyah_pikseller:
  piksel_ciz(x, y, boyut, "black")

ekran.mainloop()
