nama = 'dicdina'
program = 'gerak lurus'
print(f'program {program} oleh {nama}')

def hitung_kecepatan(jarak, waktu):
    kecepatan = jarak/waktu
    print(f'jarak = {jarak / 1000}km di tempuh dalam waktu = {waktu / 60}menit')
    print(f'sehingga kecepatan = {kecepatan} m/s')
    return kecepatan

#jarak = 1000
#waktu = 5*60
kecepatan = hitung_kecepatan(1000, 5*60)
kecepatan = hitung_kecepatan(80000, 50*60)

def hitung_Energi(m, c):
    Energi = m*c*c
    print(f'm = {m / 1000}kg di tempuh dalam kecepatan cahaya = {c*c}m/s')
    print(f'sehingga Energi = {Energi} Joule')
    return Energi

Energi = hitung_Energi(0.6, 3*100000000)


