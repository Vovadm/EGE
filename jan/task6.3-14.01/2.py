from turtle import dot, fd, rt, done, setpos, left, up, tracer

left(90)
tracer(0)
k = 5
for i in range(12):
    rt(90)
    fd(125 * k)
    rt(90)
    fd(17 * k)

up()

for x in range(-0, 150):
    for y in range(-20, 5):
        setpos(x * k, y * k)
        dot(3)


done()
