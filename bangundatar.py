import math

def l_persegi(sisi):
    luas = sisi*sisi
    print(f'Luas Persegi : {sisi} * {sisi} = {luas}')

def l_persegipanjang(panjang,lebar):
    luas = panjang*lebar
    print(f'Luas Persegi panjang : {panjang} * {lebar} = {luas}')

def l_segitiga(alas,tinggi):
    luas = 1/2 * alas * tinggi
    print(f'Luas Segitiga : {1/2} * {alas} * {tinggi} = {luas}')

def l_lingkaran(r1,r2):
    luas = 3.14 * r1 * r2
    print(f'Luas lingkaran : {3.14} * {r1} * {r2} = {luas}')

def l_jajargenjang(alas,tinggi):
    luas = alas * tinggi
    print(f'LUas Jajargenjang : {alas} * {tinggi} = {luas}')

   