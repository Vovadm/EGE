from turtle import (
    dot,
    fd,
    rt,
    done,
    pendown,
    setpos,
    tracer,
    left,
    up,
)

pendown()
tracer(0)
left(90)

k = 20

for i in range(9):
    rt(80)
    fd(5 * k)


up()
for x in range(-100, 150):
    for y in range(-100, 100):
        setpos(x * k, y * k)
        dot(3)


done()
