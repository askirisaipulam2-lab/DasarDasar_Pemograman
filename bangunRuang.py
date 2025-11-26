import math
# Rumus Kubus
def kubus(sisi):
    hasil = math.pow(sisi, 3)
    return hasil

# Rumus Balok
def balok(p, l, t):
    hasil = p * l * t
    return hasil

# Rumus Prisma
def prisma(luas_alas, tinggi):
    hasli = luas_alas * tinggi
    return hasli

# Rumus Tabung
def tabung(r, j, t):
    hasil = math.pi * (j**2)* t
    return hasil

# Rumus Kerucut
def kerucut(v, r, j, t):
    hasil = (1/3)* math.pi * (j**2)* t
    return hasil