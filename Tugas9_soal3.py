# Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
# nilai (80) #lulus
# nilai(60) #gagal

def nilai(n = 0):
    if n <= 60:
        print('Tidak Lulus')
    elif n >= 60:
        print('Lulus')
    else:
        print('Tidak diketahui')

nilai(89)