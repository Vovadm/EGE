def moves(s):
    res = [s + 1, s + 2]
    if s % 3 == 0:
        res.append(s * 3)
    return res


def f(s, m):
    if s >= 56:
        return m % 2 == 0
    if m == 0:
        return False
    mv = moves(s)
    h = [f(ns, m - 1) for ns in mv]
    return any(h) if m % 2 == 1 else all(h)


def f2(s, k):
    max_ply = 2 * k
    from functools import lru_cache

    @lru_cache(None)
    def dfs(s, player, depth):
        if s >= 56:
            last_mover = "V" if player == "P" else "P"
            return last_mover == "V"
        if depth == 0:
            return False
        if player == "P":
            for ns in moves(s):
                if ns >= 56:
                    return False
                if not dfs(ns, "V", depth - 1):
                    return False
            return True
        else:
            for ns in moves(s):
                if ns >= 56:
                    return True
                if dfs(ns, "P", depth - 1):
                    return True
            return False

    return dfs(s, "P", max_ply)


task19 = min(
    [s for s in range(1, 56) if any(v >= 56 for p in moves(s) for v in moves(p))]
)
task20 = [s for s in range(1, 56) if (not f(s, 1)) and f(s, 3)]
task21 = [s for s in range(1, 56) if f2(s, 3) and not f2(s, 1) and not f2(s, 2)]

print(task19)
print(task20)
print(task21)
