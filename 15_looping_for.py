# Looping == sebuah konstruksi yang digunakan untuk melakukan operasi berulang
# secara otomatis, tanpa menulis manual

data_saya = ["Yamastio", "Miku", "Akane", "Eren"]

# Menggunakan for loop
for elemen_saya in data_saya:
    print(elemen_saya) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# Print setiap character dalam string
for karakter in "Yamastio":
    print(karakter) # Y, a, m, a, s, t, i, o
## sebenarnya string itu adalah character yang ada dalam list
kata_saya = ['Y', 'a', 'm', 'a', 's', 't', 'i', 'o']

# Menerapkan looping untuk data tuple
tupple_saya = (1,2,3,4,5)

for elemen_tupple in tupple_saya:
    print(elemen_tupple) # 1, 2, 3, 4, 5

# Menerapkan dengan operator aritmatika
data_angka = [2,4,6]
for elemen_list in data_angka:
    print(elemen_list ** 2)
