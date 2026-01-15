from turtle import lt, done, rt, fd, bk

k = 18

lt(90)
for i in range(12):
    rt(60)
    fd(5 * k)
    lt(30)
    bk(5 * k)


done()
