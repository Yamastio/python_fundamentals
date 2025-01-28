# Docstring = Teks khusus untuk memperjelas fungsi/kelas/modul
# Lebih paham lagi terkati kelas/fungsi/modul


class Orang:
    """
    Kelas yang mendeskripsikan sebuah nama
    """

    def __init__(self, nama: str):
        self.nama = nama

    def panggil(self):
        print(f"Hello {self.nama}")


def hitung_persegi_panjang(panjang: int, lebar: int) -> int:
    """
    Ini adalah fungsi hitung persegi panjang

    paramter:
        panjang (int): panjang dari suatu persegi
        lebar (int): lebar dari suatu persegi

    return:
        int: hasil dari panjang dikalikan dengan lebar
    """
    return panjang * lebar


print(hitung_persegi_panjang(2, 5))

# Akses docstring
print(hitung_persegi_panjang.__doc__)  # fungsi dunder


# Akses docstring dari kelas
print(Orang.__doc__)

person = Orang("Kyouma")
Orang.panggil(person)
