from turtle import *

lt(90)
tracer(0)
k = 15

for i in range(5):
    fd(8 * k)
    rt(120)
    for j in range(2):
        fd(4 * k)
        rt(60)
    fd(4 * k)
    rt(120)

up()
for x in range(-15, 15):
    for y in range(-15, 15):
        goto(x * k, y * k)
        dot(4)

done()
