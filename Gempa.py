class Gempa:
    #konstruktor Inisialisasi atribut
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    #mathod menentu skala gempa 
    def dampak(self):
        #logika/statement
        if self.skala < 2:
            print('gempa tida berasa')
        elif 2<= self.skala <= 4:
            print('gempa berdambak bangunan rusak')
        elif 4 <= self.skala <= 6:
            print('gempa berdampak bangunan roboh')
        elif self.skala >6:
            print('Gempa Besar Berpotensi tsunami')

        # menampilkan lokasi dan skala gempa
        print(f'Lokasi Gempa: {self.lokasi}')
        print(f'Skala Gempa: {self.skala}')