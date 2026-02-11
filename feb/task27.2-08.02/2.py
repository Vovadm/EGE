from math import dist


def visual(cluesters):
    from turtle import tracer, setpos, dot, done

    tracer(0)
    colors = ["green", "blue"]
    k = 20

    for i in range(len(cluesters)):
        for x, y in cluesters[i]:
            setpos(x * k, y * k)
            dot(5, colors[i])

    done()


with open("feb/task27.2-08.02/2.txt") as f:
    points = [list(map(float, s.replace(",", ".").split())) for s in f]
    clusters = []
    eps = 1
    while points:
        clusters.append([points[0]])
        del points[0]
        for p1 in clusters[-1]:
            for p2 in points[:]:
                if dist(p1, p2) < eps:
                    clusters[-1].append(p2)
                    points.remove(p2)

        if len(clusters[-1]) <= 3:
            del clusters[-1]


visual(clusters)
