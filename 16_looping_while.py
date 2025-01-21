# While Loop == looping yang berulang, mengulangi kondisi tertentu bedanya
# looping ini berdasarkan kondisi tertentu, tidak mengetahui iterasinya

data_saya = [1,2,3,4,5,6]
i = 0

# Menggunakan while loop
while i < len(data_saya):
    print(data_saya[i])
    i += 1

# Membuat game tebak angka
angka_yang_ditebak = 10
tebakan = 0

while tebakan != angka_yang_ditebak:
    tebakan = int(input("Tebakan angka: "))
    if tebakan < angka_yang_ditebak:
        print("Tebakan terlalu kecil!")
    elif tebakan > angka_yang_ditebak:
        print("Tebakan terlalu besar!")
    else:
        print("Tebakan benar!")
