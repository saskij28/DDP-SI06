#tugas 1: BILANGAN GENAP ATAU GANJIL
angka = int(input('masukkan bilangan bulat:'))
genap = 'bilangan genap'
ganjil ='bilangan ganjil'

if angka % 2 == 0:
    print('bilangan genap')
elif angka % 2 != 0:
    print('bilangan ganjil')
else:
    print('bilangan ganjil')
print()
print('======================')

#tugaas 2: NILAI UJIAN
nilaiujian = int(input('masukkan nilai ujian: '))
lulus = 'anda lulus'
tidaklulus = 'anda tidak lulus'

if nilaiujian >= 75:
    print('anda lulus')
else:
    print('anda tidak lulus')

print()
print('======================')

#tugas 3: CEK USIA DAN STATUS
usia = int(input('masukkan usia dan status: '))

if usia >= 18:
    print('Dewasa')
elif usia > 18 and usia < 13:
    print('Remaja')
else:
    print('Anak-anak')

print()
print('======================')

#tugas 4: CEK KEANGGOTAAN
statusanggota = input('masukkan status anggota: ')

if statusanggota == 'gold' or statusanggota == 'silver':
    print('selamat anda mendapatkan diskon')
elif statusanggota == 'bronze':
    print('maaf anda tida daptkan diskon')
else:
    print('input tidak valid')

print()
print('======================')

#tugas 5: PEMBELIAN DISKON
jumlahpembelian = int(input('masukkan jumlah pembelian: '))
hargaitem = 1000
hargaDISKON = hargaitem * jumlahpembelian * (10/100)
hargaTotal = hargaitem * jumlahpembelian
total = hargaTotal - hargaDISKON

print(f'anda mendapatkan diskon 10%, harga per item {hargaitem} jadi total yang harus dibayar {total} ') if jumlahpembelian > 100 else print(f'harga per item {hargaitem}, jadi total yang harus dibayar adalh {hargaTotal}')

print()
print('======================')