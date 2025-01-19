# Dictionary == sebuah tipe data yang bisa menampung banyak data, secara urut
# Bisa berupa angka, string, boolean, dan lainnya
# Yang membedakan dictionary ini ada konsep key-value

# Membuat dictionary
data_saya = {"nama": "Yamastio", "umur": 22, "jenis_kelamin": "Laki-laki"}

# Menampilkan semua isi dictionary
print(data_saya)

# Menampilkan elemen dari dictionary
print(data_saya["nama"]) # Yamastio

# Menambahkan elemen baru
data_saya["status"] = True
print(data_saya)

# Menghapus elemen dari dictionary
del data_saya["status"]
print(data_saya)

# Menampilkan semua keys
print(data_saya.keys())

# Menampilkan semua values
print(data_saya.values())

# mengecek apakah key ada di dictionary
print("nama" in data_saya)
