# Lambda Function = fungsi tanpa nama untuk membuat fungsi sederhana

# Lambda sederhana
def hasil_kalkulasi(nilai_x): return nilai_x * 12


print(hasil_kalkulasi(2))


# lambda dalam sorted
nilai_kita: list = [6, -10, 4, -20, 5]
nilai_urut: list = sorted(
    nilai_kita, key=lambda nilai_sorting: abs(nilai_sorting))

# Menghitung nilai absolut dari setiap elemen.
# Untuk daftar [6, -1, 4, -2, 5], nilai absolutnya menjadi: [6, 1, 4, 2, 5].

print(nilai_urut)

# Lambda dalam map = merubah setiap elemen
nilai_kita: list = [6, -10, 4, -20, 5]
nilai_map: list = list(map(lambda x: x ** 2, nilai_kita))

print(nilai_map)

# Lambda dalam filter = menyaring elemen tertentu
nilai_kita: list = [6, -10, 4, -20, 5]
nilai_filter: list = list(filter(lambda x: x > 0, nilai_kita))

print(nilai_filter)

nilai_campur: list = [7, -10, 4, -20, 5]
nilai_genap: list = list(filter(lambda x: x % 2 == 0, nilai_campur))
nilai_ganjil: list = list(filter(lambda x: x % 2 != 0, nilai_campur))

print(nilai_genap)
print(nilai_ganjil)
