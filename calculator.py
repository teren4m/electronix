def ml(x):
    return x * 1000

def u(x):
    return ml(x) * 1000

def n(x):
    return u(x) * 1000

C = 1e-6
V = 5

E = (C * V ** 2) / 2

print(ml(E))