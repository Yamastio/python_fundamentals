# Type hinting == menambahkan anotasi tipe pada variabel/parameter
# Tipe data statis yang membantu program untuk mengetahui tipe data yang diberikan


# cara membuat typehinting

nama: str = "Kyouma"
umur: int = 24
nilai: float = 80.5
kondisi: bool = False
nilai_complex: complex = 20j
daftar_belajar: list[str] = ["matematika", "fisika", "kimia"]
contoh_tuple: tuple[str, str] = ("bahasa inggris", "bahasa indonesia")
contoh_dict: dict = {"nama": "Yamastio",
                     "umur": 22, "jenis_kelamin": "Laki-laki"}


# cara menambahkan typehinting pada fungsi
def hitung(angka1: int, angka2: int) -> int:
    return angka1 + angka2


def panggil(nama: str) -> None:
    print(f"Halo {nama}")


print(panggil("Yamastio"))

# print(hitung(5, 2.5)) ## tetap bisa run, tapi nanti bisa pakai library tertentu untuk cek tipe data dari suatu fungsi
print(hitung(5, 5))
