from Animal import *

class burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu = jenis_bulu
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print(f'Hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi  {self.bunyi}')

beo = burung('Burung Beo', 'biji-bijian', 'udara', 'bertelur', 'biru dan oranye', 'kamu jelek')
beo.cetak_burung()

gagak = burung('Burung gagak', 'bangkai hewan', 'bertelur', 'udara dan darat', 'hitam', 'gakgakgakgakgakgak', )
gagak.cetak_burung()