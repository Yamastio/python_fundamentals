# Fungsi == sebuah fungsi yang berfungsi untuk menjalankan beberapa tugas
# Memecah program besar jadi beberapa fungsi yang kecil, yang mudah dikelola
# Meningkatkan modularitas

# Cara membuat fungsi (Void Function)
def panggil_nama():
    print("Halo, nama saya adalah Yamastio")
    print("Selamat datang di sini!")
    print("ini adalah fungsi")

# Menjalankan fungsi
panggil_nama()

# Parameter di dalam fungsi
def panggil_aku(nama, umur):
    print(f"Halo, nama saya adalah {nama}, umur saya {umur} tahun")

# Menjalankan fungsi dengan parameter
panggil_aku("Miku", 21)
panggil_aku("Akane", 20)

# Fungsi yang mengembalikan nilai
def perhitungan_tambah (angka, angka2):
    return f"{angka} + {angka2} = {angka + angka2}"

print(perhitungan_tambah(2, 3))

# fungsi di dalam variabel
hasil_angka = perhitungan_tambah(2, 2)

print(hasil_angka)

# Membuat kalkulator
def kalkulator(angka1, angka2, operator):
    if operator == "+":
        return angka1 + angka2
    elif operator == "-":
        return angka1 - angka2
    elif operator == "*":
        return angka1 * angka2
    elif operator == "//":
        return angka1 // angka2
    else:
        return "Salah operasi"

angka1 = int(input("Masukan angka1: "))
angka2 = int(input("Masukan angka2: "))
operator = input("Masukan operator: ")

print(kalkulator(angka1, angka2, operator))
