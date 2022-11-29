import turtle
import random
from time import sleep
import functools

ikkuna = turtle.Screen()
ikkuna.title("Väistelypeli")
ikkuna.bgcolor("blue")

ikkuna.setup(width=1000,height=750)
ikkuna.tracer(0)

maara = random.randrange(10,21)

viholliset = []
nopeus = 10

alku_sijainti = -2000

pelaaja_sijainti = 0

#Luodaan satunnainen määrä vihollisia arpomalla niiden aloitus paikka.

for i in range(maara):
  viholliset.append(turtle.Turtle())
  viholliset[i].speed(0)
  viholliset[i].shape("square")
  viholliset[i].color("black")
  viholliset[i].shapesize(stretch_wid=8,stretch_len=4)
  viholliset[i].penup()
  viholliset[i].dy = nopeus
  if (i % 2 == 0):
    viholliset[i].goto(random.randrange(-400,400),alku_sijainti)
  else:
    viholliset[i].goto(random.randrange(-400,400),alku_sijainti)
  alku_sijainti += 100

#Luodaan pelaaja  
pelaaja = turtle.Turtle()
pelaaja.speed(0)
pelaaja.shape("square")
pelaaja.color("white")
pelaaja.penup()
pelaaja.shapesize(stretch_wid=8,stretch_len=4)


pelaaja.goto(0,350)
pelaaja.dx =10

def ohjaa(key):
  global pelaaja_sijainti
  if (key == "a" and pelaaja_sijainti > -400):
    pelaaja.setx(pelaaja.xcor()-pelaaja.dx)
    pelaaja_sijainti-=10

  elif (key == "d" and pelaaja_sijainti < 400):
    pelaaja.setx(pelaaja.xcor()+pelaaja.dx)
    pelaaja_sijainti+=10

def nopeuta():
  #Kierros suoritettu, seuraava erä on nopeampi
  global nopeus,maara,alku_sijainti
  alku_sijainti = -2000
  nopeus += 10
  for i in range(maara):
   viholliset[i].speed(0)

   viholliset[i].dy = nopeus
   if (i % 2 == 0):
     viholliset[i].goto(random.randrange(-400,400),alku_sijainti)
   else:
     viholliset[i].goto(random.randrange(-400,400),alku_sijainti)
   alku_sijainti += 100


ikkuna.listen()
kaynnissa = True
pisteet = 0
#Peli jatkuu niin kauan kunnes pelaaja törmää viholliseen.

while kaynnissa:
 for i in range(maara):
   viholliset[i].sety(viholliset[i].ycor()+viholliset[i].dy)
   if (abs(viholliset[i].ycor()-pelaaja.ycor()) < 50 and abs(viholliset[i].xcor()-pelaaja.xcor()) < 20):
        #törmätty viholliseen
        print(f"Hävisit, pisteet {pisteet}")
        kaynnissa = False
 ikkuna.onkeypress(functools.partial(ohjaa,"a"),key="a")
 ikkuna.onkeypress(functools.partial(ohjaa,"d"),key="d")
 if (viholliset[0].ycor() >=   600):
  print("Kierros")
  pisteet += 1
  nopeuta()

 sleep(0.1)
 ikkuna.update()
