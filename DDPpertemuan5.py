#tugas no.1
kendaraan = ["Motor", "Yamaha Fazzio Lux", "125cc", "LUX Prestige Silver", "roda 2"]
print(kendaraan)

kendaraan.append("22.190.000 Matic")
print(kendaraan)

kendaraan.insert(1,"Fazzio Lux")
print(kendaraan)

print("============================")
#tugas no.2
pilih = int(input("""selamat datang di aplikasi menghitung
1. Untuk menghitung luas persegi
2. Untuk menghitung luas lingkaran
3. Untuk menghitung luas segitiga 
                  
masukkan piliahan anda : \n""" ))

match pilih:
    case 1 :
        print("Kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("masukkan sisi persegi: "))
        luaspsg = sisi*sisi
        print("luas persegi yang sisinya ",sisi,"adalah", luaspsg )
    case 2 :
        print("kamu melilih 2 untuk menghitung lingkaran")
        jari2 = int(input("masukkan jari-jari: "))
        luaslingkaran = 3.14 * jari2 * jari2
        print("luas lingkaran yang jari-jari ",jari2,"adalah", luaslingkaran )
    case 3 :
        print("kamu melilih 3 untuk menghitung segitiga")
        alas = int(input("masukkan alas: "))
        tinggi = int(input("maukkan tinggi: "))
        luassegitiga = 0.5 * alas * tinggi
        print("luas segitiga yang alas ",alas,"dan tinggi",tinggi,"adalah", luassegitiga )
    case _:
        print("anda salah pilih")
