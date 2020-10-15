from geometri.bangunruang import BangunRuang


class SegiTiga(BangunRuang):
    # Type 1
    def __init__(self, alas, tinggi, p = None, l = None):
        super().__init__(p, l, alas, tinggi)

    # Type 2
    # def __init__(self, alas, tinggi):
    #     self.alas = alas
    #     self.tinggi = tinggi