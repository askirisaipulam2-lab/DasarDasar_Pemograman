import bangunRuang as br
import bangunDatar as bd
#as kata ganti

# Volum Bangun Ruang
print("_______BANGNUN RUANG________")
print(f'1. volume kubus dengan sisi 3 adalah {br.kubus(7)}')
print(f'2. volume balok dengan panjang * lebar * tinggi adalah {br.balok(5,6,5)}')
print(f'3. volume prisma adalah {br.prisma(9,7)}')
print(f'4. volume tabung adalah {br.tabung(9,7,6)}')
print(f'5. volume kerucut adalah {br.kerucut(4,7,5,4)}')

# Luas Bangun Datar
print("______BANGUN DATAR______")
print(f'1. Luas Persegi Adalah {bd.persegi(9)}')
print(f'2. Luas Persegi panjang Adalah {bd.persegiPanjang(5,4)}')
print(f'3. Luas Segitiga Adalah {bd.segitiga(7,5)}')
print(f'4. Luas Lingkaran Adalah {bd.lingkaran(8,9)}')
print(f'5. Luas Jajar Genjang Adalah {bd.jajarGenjang(8,8)}')