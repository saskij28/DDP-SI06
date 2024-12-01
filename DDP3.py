
#soal 1
nama = 'Saskia Julaika'
nim = '0110124231'
rombel = 'SI06'
no_tlp = 6285714522787
alamat = 'Cilodong, Depok'

print('nama saya:', nama)
print('nim saya:', nim)
print('rombel sayya:', rombel)
print('no telepon saya:', no_tlp)
print('alamat saya:', alamat)
print('=========================')

#soal2
nama = 'Fara Nabila'
nim = '0110124216'
rombel = 'SI06'
no_tlp = 6285780136980
alamat = 'Depok, Cisalak'

print('nama teman saya:', nama)
print('nim teman saya:', nim)
print('rombel teman saya:', rombel)
print('no telepon teman saya:', no_tlp)
print('alamat teman saya:', alamat)
print('=========================')

#soal3
#mencari berat badan ideal
#rumus = (tinggi badan - 100) - (tinggi badan - 100) * 0.15
TB = int(input('masukan tinggi badan :'))
bb_ideal = (TB - 100) - (TB - 100) * 0.15

print('berat badan ideal adalah :',bb_ideal)

print('=========================')

#soal4
#mencari nilai konversi dari celcius ke fahreinheit 
CL = float(input('masukan suhu celcius :'))
FR = (9/5*CL)+ 32

print('nilai suhu fahreinheit adalah :', FR)

print('=========================')

#soal5
#mencari keliling dan luas tabung
print('LUAS DAN KELILING TABUNG:')
phi = 22/7
r = int(input('masukkam jari jari:'))
t = int(input('masukkan tinggi:'))
p = int(input('masukkan panjang:'))

luas = 2*phi*r*(r+t)
keliling = 2*(p+t)

print('hasil luas:',luas)
print('hasil keliling:',keliling)
