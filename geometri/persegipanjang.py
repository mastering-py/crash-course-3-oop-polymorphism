from geometri.bangunruang import BangunRuang


class PersegiPanjang(BangunRuang):
    # Type 1
    def __init__(self, p, l, alas = None, tinggi = None):
        super().__init__(p, l, alas, tinggi)

    # Type 2
    # def __init__(self, p, l):
    #     self.p = p
    #     self.l = l