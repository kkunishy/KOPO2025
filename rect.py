import random as rd
import turtle as t
a=0
b=0

def aRand():
    a = rd.randrange(1, 1000)

while True:
    aRand()
    t.forward(5+a)
    aRand()
    t.left(a)
