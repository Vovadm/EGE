from turtle import dot, fd, rt, done, pendown, setpos, tracer, left, up, down

pendown()
tracer(0)
left(90)

k = 20


for _ in range(4):
    fd(15 * k)
    rt(90)
    fd(19 * k)
    rt(90)

up()
fd(8 * k)
rt(90)
fd(6 * k)
left(90)
down()
for _ in range(2):
    fd(89 * k)
    rt(90)
    fd(77 * k)
    rt(90)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(3)


done()
