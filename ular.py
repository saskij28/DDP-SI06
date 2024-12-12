from Animal import *

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_motif, jenis_ular):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_motif = warna_motif
        self.jenis_ular = jenis_ular

    def cetak_ikan(self):
        super().cetak()
        print(f'warna atau motif dari ular ini adalah {self.warna_motif} dan hewan ini jenisnya {self.jenis_ular}')

sawah = Animal('ular sawah','tikus', 'sawah', 'bertelur', 'cokelat', 'tidak berbisa')
sawah.cetak_ular

cobra = Animal('ular Cobra','daging', 'hutan', 'bertelur', 'abu-abu', 'berbisa')
cobra.cetak_ular