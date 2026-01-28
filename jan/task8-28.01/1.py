from itertools import product

count = 0
digits = "0123456"
print(digits)

for p in product(digits, repeat=4):
    if p[0] == "0":
        continue

    if int(p[0]) % 2 == 0:
        continue

    if p.count("4") == 1:
        count += 1

print(count)
