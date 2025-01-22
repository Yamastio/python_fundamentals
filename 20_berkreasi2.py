class DataMahasiswa:
    def __init__(self, nama, jurusan, ipk):
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkan_nama(self):
        return self.nama

    def ganti_nama(self, nama_baru):
        self.nama = nama_baru

    def ganti_ipk(self, ipk_baru):
        self.ipk = ipk_baru

    def tampilkan_jurusan(self):
        return self.jurusan

    def cetak_data_mahasiswa(self):
        print(f"Nama: {self.nama}")
        print(f"Jurusan: {self.jurusan}")
        print(f"IPK: {self.ipk}")


data_mahasiswa_1 = DataMahasiswa("Miku", "Teknologi Informasi", 4.0)

print(data_mahasiswa_1.tampilkan_nama())
print(data_mahasiswa_1.tampilkan_jurusan())
data_mahasiswa_1.cetak_data_mahasiswa()
data_mahasiswa_1.ganti_nama("Naka")
data_mahasiswa_1.ganti_ipk(2.9)
data_mahasiswa_1.cetak_data_mahasiswa()
