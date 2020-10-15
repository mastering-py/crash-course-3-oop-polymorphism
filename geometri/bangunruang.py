class BangunRuang:
    def __init__(self, p, l, alas, tinggi):
        self.p = p
        self.l = l
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return f'Perhitungan luas {self.__class__.__name__}:'

    def hitung_luas(self):
        try:
            return f'{self.p * self.l}'
        except:
            return f'{self.alas * self.tinggi / 2}'


