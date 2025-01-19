# format string = mengatur format output dari string

nama_saya = "Yamastio"
umur_saya = 22

# 1. Dengan Separator
print("Nama saya adalah", nama_saya)
print("Umur saya adalah", umur_saya, "tahun")
print("Nama saya adalah", 10+12)

# 2. Dengan format string
# python versi 3.6 atau lebih tinggi bisa menggunakan format string
print(f"Nama saya adalah {nama_saya}")
print(f"Umur saya adalah {umur_saya} tahun")
print(f"Nama saya adalah {10+12}")
print(f"tipe data dari variabel {nama_saya} adalah {type(nama_saya)}")
print(f"{3+20} + {20-3} = {3+20+20-3}")

