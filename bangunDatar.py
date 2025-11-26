import math
# Rumus Persegi
def persegi(sisi):
    luas = sisi**2
    return luas 

# Rumus Persegi Panjang
def persegiPanjang(panjang, lebar):
    luas = panjang * lebar
    return luas

# Rumus Segitiga
def segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

# Rumus Lingkaran
def lingkaran(r, jari_lingkaran):
    luas = math.pi * jari_lingkaran**2
    return luas

# Rumus Jajar Genjang
def jajarGenjang(alas, tinggi):
    luas = alas * tinggi
    return luas