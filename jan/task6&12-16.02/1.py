from turtle import dot, fd, rt, done, pendown, setpos, tracer, left, up

pendown()
tracer(0)
left(90)

k = 25

for i in range(7):
    fd(6 * k)
    rt(270)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(3)


done()
