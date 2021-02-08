def dbl_linear(n):
    u = {0: 1}
    for e in range(n*5):
        x = 2*u[e] + 1
        z = 3*u[e] + 1
        u.update({e*2 + 1: x})
        u.update({e*2 + 2: z})
    
    u = {k: v for k, v in enumerate(sorted(set(u.values())))}
    return u[n]