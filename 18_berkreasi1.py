def hitung_persegi_panjang(panjang, lebar):
    return panjang * lebar


while True:
    print("Program Hitung Luas Persegi Panjang")
    panjang = float(input("Masukan panjang persegi: "))
    lebar = float(input("Masukan lebar persegi: "))

    if panjang <= 0:
        print("Nilai tidak boleh nol")
    if lebar <= 0:
        print("Nilai tidak boleh nol")

    print(f"Hasilnya adalah {hitung_persegi_panjang(panjang, lebar)}")

    ulang = input("Apakah ingin ulangi program? (Y/n): ")

    if ulang != "y":
        break
