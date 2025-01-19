# List == sebuah tipe data yang bisa menampung banyak data, secara urut
# Bisa berupa angka, string, boolean, dan lainnya

# Membuat list
list_1 = ["Yamastio", "Kyouma", "Akane" ]
list_2 = ["Yamastio", True, 3.14 ]

# Menampilkan semua isi list
print(list_1)
print(list_2)

# Menampilkan elemen dari list
print(list_1[0]) # Yamastio

# jika mengakses elemen yang tidak ada, akan menghasilkan error
# print(list_1[3]) # index out of range


# List bersifat mutable, elemen bisa dirubah
list_1[0] = "Miku"
print(list_1[0])

# Menambahkan elemen baru
list_2.append("Eren")
print(list_2)

# Menghitung panjang list
print(len(list_2))

# Menghapus elemen dari list
list_2.pop(3) # menghapus elemen ke-3
print(list_2) # ['Yamastio', True, 3.14]
