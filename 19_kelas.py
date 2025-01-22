# Kelas = blueprint untuk membuat objek tertentu, misal tank, robot, dll
# Nama kelas diawali huruf kapital(PascalCase)
# Contoh = Mobil, MobilPerang

# Cara membuat kelas
class Mobil:
    # constructor, dengan atribute warna, merek, kecepatan
    # self = merujuk pada instance / objek yang sedang dibuat, mengakses atribute didalam kelas
    def __init__(self, warna, merek, kecepatan):  # constructor
        self.warna = warna  # variabel yang dimiliki kelas(Atribut)
        self.merek = merek
        self.kecepatan = kecepatan

    def hidup_mesin(self):  # Method
        print(f"Menghidupkan mesin mobil {self.merek}")

    def mematikan_mesin(self):  # Method
        print(f"Mematikan mesin mobil {self.merek}")

    def menjalankan_mobil(self):  # Method
        if self.kecepatan > 120:
            print(
                f"Mobil {self.merek} tidak bisa jalan di kecepatan {self.kecepatan} km/jam")
        else:
            print(
                f"Menjalankan mobil {self.merek}, dengan kecepatan {self.kecepatan} km/jam")


# Membuat object (Orientasi dari kelas)
mobil_saya = Mobil("Merah", "Toyota", 130)

mobil_saya.hidup_mesin()
mobil_saya.menjalankan_mobil()
mobil_saya.mematikan_mesin()

# Memanggil atribute
print(mobil_saya.merek)


# Class = blueprint untuk membuat objek tertentu, contoh mobil
# Constructor = metode khusus yang pertama kali dipanggil, untuk menginisialisasi objek, dibuat dengan = __init__
# Atribut = Variabel yang dimiliki kelas. Contoh warna, merek, kecepatan
# self.warna = Atribut milik instance (digunakan untuk menyimpan data di dalam objek).
# warna: Nilai dari parameter yang diterima saat objek dibuat.
# Instance = Objek yang dibuat dari kelas, contoh mobil_saya
# Metode = Fungsi yang dibuat dari kelas, contoh hidup_mesin, menjalankan_mobil, mematikan_mesin
# Objek = instansiasi dari kelas, contoh mobil_saya (instance)
