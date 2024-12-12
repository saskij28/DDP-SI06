from Animal import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_ikan = warna_ikan
        self.jenis_ikan = jenis_ikan

    def cetak_ikan(self):
        super().cetak()
        print(f'warna ikan ini adalah {self.warna_ikan} dan hewan ini jenisnya {self.jenis_ikan}')

nemo = ikan('ikan Nemo', 'plangton', 'air', 'bertelur', 'orange', 'air laut')
nemo.cetak_ikan

dori = ikan('ikan Dori', 'plangton', 'air', 'bertelur', 'biru', 'air laut')
dori.cetak_ikan
