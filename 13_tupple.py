# Tupple == sebuah tipe data indeks, yang bisa menampung banyak data, secara urut
# Perbedaan dengan list, tupple tidak bisa diubah(immutable)

# Membuat tupple
data_saya = ("Yamastio", "Miku", "Akane", 10, 3.14, True)

# Menampilkan semua isi tupple
print(data_saya)

# Menampilkan elemen dari tupple
print(f"Nama saya adalah {data_saya[0]}") # Yamastio
print(data_saya[1]) # Miku

# menggabungkan denga operasi aritmatika
print(data_saya[0] + data_saya[1]) # YamastioMiku

# jika mengakses elemen yang tidak ada, akan menghasilkan error
# print(data_saya[3]) # index out of range

# Tidak bisa mengubah elemen dari tupple

# Menambahkan elemen baru
data_saya += ("Eren",)
# data_saya.append("Eren") # error
print(data_saya)

# Menghitung panjang tupple
print(len(data_saya))

# Tidak bisa menghapus elemen dari tupple
