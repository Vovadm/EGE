from turtle import tracer, lt, rt, fd, up, down, done, setpos, dot

tracer(0)
lt(90)

k = 12
for i in range(4):
    fd(28 * k)
    rt(90)
    fd(26 * k)
    rt(90)

up()

fd(8 * k)
rt(90)
fd(7 * k)
lt(90)
down()

for i in range(4):
    fd(67 * k)
    rt(90)
    fd(98 * k)
    rt(90)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(3)

done()
