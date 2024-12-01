import math

def luaskubus(sisi):
    luas = 6 * sisi * sisi
    print(f'Luas Permukaan Kubus: {6} * {sisi} * {sisi} = {luas}')

def luasbalok(panjang,lebar,tinggi):
    luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
    print(f'Luas Permukaan Balok: {2} * {((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))} = {luas}')

def luasbola(r1,r2):
    luas = 4 * 3,14 * r1 * r2
    print(f'Luas Bola: {4} * {3,14} * {r1} * {r2} = {luas}')

def luastabung(r1,r2,tinggi):
    luas = 2 * 3,14 * r1 * (r2 + tinggi)
    print(f'Luas Permukaan Tabung: {2} * {3,14} * {r1} * {(r2 + tinggi)} = {luas}')

def luaskerucut(r, s):
    luas = math.pi * r * (r+s)
    print(f'Luas Kerucut: {math.pi} * {r} * {(r+s)} = {luas}')
    