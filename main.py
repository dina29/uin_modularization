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

#tgs fungsi apa saja yang kalian tahu


