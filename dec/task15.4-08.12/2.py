Q = list(range(12, 29))
P = list(range(5, 41))
A = []
for x in range(1, 100):
    if not (((x in A) and (x in P)) or (not (x in Q))):
        A.append(x)

print(A)
print(len(A))
