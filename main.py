from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import SegiTiga

# POLYMORPHISM: Kemampuan object untuk merespon berbeda, terhadap pemanggilan method yang sama
p1 = PersegiPanjang(10, 6)
s1 = SegiTiga(20, 2)

print('Menggunakan for loop')
list1 = []
list1.append(p1)  # menambahkan object ke dalam list
list1.append(s1)

for i in list1:
    print(f'{i.info()}')
    print(f'{i.hitung_luas()}')

print('-' * 100)

print('Menggunakan function')
def bangun_ruang(bentuk):
    print(bentuk.info())
    print(bentuk.hitung_luas())


bangun_ruang(p1)  # object sebagai argumen
bangun_ruang(s1)
