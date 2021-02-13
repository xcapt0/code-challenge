import math

def isPP(n):
    sqrt = math.sqrt(n)
    for i in range(2, round(sqrt) + 1):
        log = round(math.log(n, i))
        if pow(i, log) == n:
            return [i, log]
    return None