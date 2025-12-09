Q = list(range(8, 16))
P = list(range(12, 28))
A = list(range(1, 100))
for x in range(1, 100):
    if not ((x in A) <= ((x in P) and (not (x in Q)))):
        A.remove(x)  # наибольшая длина

print(A)
print(len(A))
