from turtle import dot, fd, rt, done, setpos, tracer, left, up

tracer(0)
left(90)

k = 50

for i in range(9):
    fd(5 * k)
    rt(90)

up()
for x in range(-100, 150):
    for y in range(-20, 100):
        setpos(x * k, y * k)
        dot(3)


done()
