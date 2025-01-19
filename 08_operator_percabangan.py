# Operator percabangan == mengatur alur program dalam kondisi tertentu

nilai_pertama = 2
nilai_kedua = 3

# 1. Operator If
# Jika kondisi true, maka program dijalankan
if nilai_pertama < nilai_kedua:
    print("nilai pertama lebih kecil")

# 2. Operator Else
# Jika kondisi if == false, maka program ini dijalankan
# Pilihan terakhir dari suatu kondisi
if nilai_pertama == nilai_kedua:
    print("nilai pertama lebih besar")
else:
    print("nilai pertama lebih kecil")

# 3. Operator Elif
# Jika kondisi pertama tidak bernilai true, maka program dijalankan(Alternatif)
if nilai_pertama == nilai_kedua:
    print("nilai pertama sama dengan nilai kedua")
elif nilai_pertama < nilai_kedua:
    print("nilai pertama lebih kecil")
else:
    print("nilai tidak ada yang memenuhi kondisi")

# Percabangan dengan string
cuaca = "hujan"

if cuaca == "hujan":
    print("sediakan payung")
else:
    print("sediakan kaca mata")

# Percabangan dengan aritmatika
angka1 = 5
angka2 = 3
hasil = angka1 + angka2

if hasil == 8:
    print("Hasilnya adalah 8")
elif hasil == 7:
    print("Hasilnya adalah 7")
else:
    print("Hasilnya bukan 8")

